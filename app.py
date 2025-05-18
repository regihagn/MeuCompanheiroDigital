from src.agentes import AgenteAlertaEmergencia, AgenteInteracaoLembretes, AgenteMonitoramentoSaude, AgenteRelatorios, call_agent
from src.utils import simular_dados_sensor, simular_entrada_audio
from google.genai import types  # Para criar conteúdos (Content e Part)
import random
import time

# --- Inicialização dos Agentes ---
agente_monitor = AgenteMonitoramentoSaude()
agente_interacao = AgenteInteracaoLembretes()
agente_alerta = AgenteAlertaEmergencia()
agente_relatorio = AgenteRelatorios()

# --- Loop Principal de Simulação ---
print("🚀 Iniciando Simulação Interativa do 'Meu Companheiro Digital' Vestível 🚀")

historico_saude = []

while True:
    # Simular coleta de dados do sensor a cada X segundos
    time.sleep(5)
    dados_sensor = simular_dados_sensor()
    historico_saude.append(dados_sensor)
    print(f"\n⌚ Dados do sensor: {dados_sensor}")

    # Enviar dados para o Agente de Monitoramento de Saúde
    mensagem_monitoramento = types.Content(role="user", parts=[types.Part(text=str(dados_sensor))]) # Garante que dados_sensor seja string
    resposta_monitoramento = call_agent(agente_monitor, mensagem_monitoramento)
    print(f"⚕️ Agente de Monitoramento de Saúde: {resposta_monitoramento}")

    # Solicitar input do usuário
    entrada_usuario = input("🗣️ Você: ")
    entrada_usuario_lower = entrada_usuario.lower()
    mensagem_interacao = types.Content(role="user", parts=[types.Part(text=entrada_usuario)])
    resposta_interacao = call_agent(agente_interacao, mensagem_interacao)
    print(f"💬 Agente de Interação e Lembretes: {resposta_interacao}")

    # Simular detecção de alerta na fala
    if "ajuda" in entrada_usuario_lower or "dor forte" in entrada_usuario_lower or "emergencia" in entrada_usuario_lower:
        mensagem_alerta = types.Content(role="user", parts=[types.Part(text="Alerta detectado na fala do usuário.")]) # Garante que a string seja passada
        resposta_alerta = call_agent(agente_alerta, mensagem_alerta)
        print(f"🚨 Agente de Alerta: {resposta_alerta}")

    # Simular detecção de alerta nos dados do sensor
    dados = simular_dados_sensor() # Obtém dados atualizados para a verificação de alerta
    if dados["pressao"] > 160 or dados["pressao"] < 90 or dados["batimentos"] > 120 or dados["batimentos"] < 50 or dados["spo2"] < 90:
        mensagem_alerta_sensor = types.Content(role="user", parts=[types.Part(text="Sinais vitais de emergência detectados nos sensores.")]) # Garante que a string seja passada
        resposta_alerta_sensor = call_agent(agente_alerta, mensagem_alerta_sensor)
        print(f"🚨 Agente de Alerta (Sensor): {resposta_alerta_sensor}")

    # Simular geração de relatório periódico
    if len(historico_saude) > 10 and random.random() < 0.1:
        mensagem_relatorio = types.Content(role="user", parts=[types.Part(text=str(historico_saude))]) # Garante que a string seja passada
        resposta_relatorio = call_agent(agente_relatorio, mensagem_relatorio)
        print(f"📊 Agente de Relatórios: {resposta_relatorio}")

    # Condição de saída (você pode ajustar conforme necessário)
    if entrada_usuario_lower == "sair":
        print("\n🛑 Fim da simulação interativa.")
        break