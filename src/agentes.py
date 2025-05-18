# 1. Agente de Monitoramento de Saúde
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types  # Para criar conteúdos (Content e Part)
from datetime import date
import textwrap # Para formatar melhor a saída de texto
from IPython.display import display, Markdown # Para exibir texto formatado no Colab
import requests # Para fazer requisições HTTP
import warnings
from pydantic import Field
import os
from google.colab import userdata
os.environ["GOOGLE_API_KEY"] = "AIzaSyAGoguzNWPMcyQlVNFFr1VYGCG2x3JOB9A"
from google import genai
client = genai.Client()

MODEL_ID = "gemini-2.0-flash"

warnings.filterwarnings("ignore")

def call_agent(agent: Agent, message_text: str) -> str:
    """Envia uma mensagem para um agente e retorna a resposta final."""
    session_service = InMemorySessionService()
    session = session_service.create_session(
        app_name=agent.name, user_id="user1", session_id="session1"
    )
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    for event in runner.run(user_id="user1", session_id="session1", new_message=content):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text
                    final_response += "\n"
    return final_response.strip()  # Adicionado .strip() para remover espaços extras


class AgenteMonitoramentoSaude(Agent):
    def __init__(self):
        super().__init__(
            name="agente_monitoramento_saude",
            model=MODEL_ID,
            instruction="""
            Você é um especialista em monitoramento de saúde. Analise os dados dos sensores fornecidos
            (pressão, batimentos, SpO2) e identifique se há sinais de alerta com base em limites predefinidos.
            """,
            description="Agente que monitora dados de saúde e identifica alertas."
        )

    def handle_message(self, message: types.Content) -> types.Content:
        dados = eval(message.parts[0].text)  # Converte a string do dicionário para um dicionário Python
        pressao = dados.get("pressao")
        batimentos = dados.get("batimentos")
        spo2 = dados.get("spo2")
        alerta = "Nenhum alerta detectado."

        if pressao > 140 or batimentos > 100 or spo2 < 95:
            alerta = "Sinais vitais fora da faixa normal."
        elif pressao > 160 or batimentos > 120 or spo2 < 90:
            alerta = "ALERTA: Sinais vitais de emergência!"

        return types.Content(role="model", parts=[types.Part(text=alerta)])
    

# 2. Agente de Interação e Lembretes ---
class AgenteInteracaoLembretes(Agent):
    lembretes: dict = Field(default_factory=dict) # Declara 'lembretes' como um campo

    def __init__(self):
        super().__init__(
            name="agente_interacao_lembretes",
            model=MODEL_ID,
            instruction="""
            Você interage com o usuário por áudio (texto simulado). Realiza checagens de bem-estar e gerencia lembretes.
            """,
            description="Agente para interação de áudio e lembretes."
        )
        # self.lembretes = {} # Não precisa inicializar aqui, Field cuida disso

    def handle_message(self, message: types.Content) -> types.Content:
        entrada_usuario = message.parts[0].text.lower()
        resposta = None

        if "como estou me sentindo" in entrada_usuario:
            prompt_bem_estar = f"Atue como um assistente de bem-estar amigável e pergunte ao usuário como ele está se sentindo."
            resposta_gerada = model.generate_content(prompt_bem_estar).text
            resposta = f"Você disse '{message.parts[0].text}'. {resposta_gerada}"
        elif entrada_usuario.startswith("lembrar de") or entrada_usuario.startswith("adicionar lembrete") or entrada_usuario.startswith("definir lembrete"):
            texto_lembrete = entrada_usuario.replace("lembrar de", "").replace("adicionar lembrete", "").replace("definir lembrete", "").strip()
            partes = texto_lembrete.split(" às ")
            if len(partes) == 2:
                remedio = partes[0].strip()
                horario = partes[1].strip()
                self.lembretes[horario] = remedio
                resposta = f"Você disse '{message.parts[0].text}'. Lembrete para tomar {remedio} às {horario} adicionado."
            else:
                resposta = f"Você disse '{message.parts[0].text}'. Formato de lembrete incorreto. Tente 'Lembre-me de [medicamento] às [horário]'."
        elif entrada_usuario == "tudo bem":
            resposta = f"Você disse '{message.parts[0].text}'. Que bom ouvir isso!"
        elif "que horas sao" in entrada_usuario or "qual a hora" in entrada_usuario:
            resposta = f"Você disse '{message.parts[0].text}'. Agora são {time.strftime('%H:%M')}."
        else:
            resposta = f"Você disse '{message.parts[0].text}'. Como posso te ajudar?"

        return types.Content(role="model", parts=[types.Part(text=resposta)])
    
# --- Agente de Alerta e Emergência ---
class AgenteAlertaEmergencia(Agent):
    def __init__(self):
        super().__init__(
            name="agente_alerta_emergencia",
            model=MODEL_ID,
            instruction="""
            Você lida com situações de alerta e emergência, notificando cuidadores.
            """,
            description="Agente para alertas de emergência."
        )

    def handle_message(self, message: types.Content) -> types.Content:
        alerta = message.parts[0].text
        mensagem_alerta = f"ALERTA: {alerta}. Notificando Emanuel (filho) via SMS (simulado)." # Simulação de envio de SMS
        print(f"🚨 Enviando alerta para Emanuel: {mensagem_alerta}")
        # Aqui, em um sistema real, você integraria uma API de SMS
        return types.Content(role="model", parts=[types.Part(text="Alerta de emergência enviado.")])



# --- Agente de Relatórios ---
class AgenteRelatorios(Agent):
    def __init__(self):
        super().__init__(
            name="agente_relatorios",
            model=MODEL_ID,
            instruction="""
            Você gera relatórios periódicos de saúde.
            """,
            description="Agente para geração de relatórios de saúde."
        )

    def handle_message(self, message: types.Content) -> types.Content:
        historico_dados = message.parts[0].text # Converte a string do histórico para lista de dicionários
        if not historico_dados:
            relatorio = "Ainda não há dados suficientes para gerar um relatório."
        else:
            # Simulação de geração de um relatório simples
            historico_dados = eval(historico_dados)
            pressao_media = sum(d.get("pressao", 0) for d in historico_dados) / len(historico_dados) if historico_dados else 0
            batimentos_media = sum(d.get("batimentos", 0) for d in historico_dados) / len(historico_dados) if historico_dados else 0
            relatorio = f"Relatório de saúde (simulado):\nPressão Arterial Média: {pressao_media:.2f}\nBatimentos Cardíacos Médios: {batimentos_media:.2f}"
            print(f"📧 Enviando relatório por e-mail (simulado): {relatorio}")
            # Aqui, em um sistema real, você integraria uma API de e-mail
        return types.Content(role="model", parts=[types.Part(text=relatorio)])