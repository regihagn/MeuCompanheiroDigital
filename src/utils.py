import random

# --- Simulação de Dados do Dispositivo Vestível ---
def simular_dados_sensor():
    # Simula a leitura de dados dos sensores
    pressao = random.randint(100, 140)  # Exemplo de pressão sistólica
    batimentos = random.randint(60, 100)
    spo2 = random.randint(95, 99)
    # Adicionar simulação para outros sensores
    return {"pressao": pressao, "batimentos": batimentos, "spo2": spo2}

# --- Simulação de Entrada de Áudio do Usuário ---
def simular_entrada_audio():
    # Simula a transcrição da fala do usuário
    comandos_possiveis = ["como estou me sentindo", "lembrar de tomar remédio", "ajuda", "tudo bem", "que horas sao"]
    return random.choice(comandos_possiveis)

