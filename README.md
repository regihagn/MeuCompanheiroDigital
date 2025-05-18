
# Meu Companheiro Digital - Protótipo Inicial

## Autor
**Regiane Ribeiro**

## Versão
**1.0**

---

## 🎯 Objetivo

Sistema de IA vestível projetado para auxiliar pessoas da terceira idade em seu dia a dia, promovendo bem-estar, segurança e conexão. Este sistema é composto por múltiplos agentes especializados em tarefas específicas, interagindo com o usuário principalmente por voz.

---

## 🧠 Descrição

**Meu Companheiro Digital** é uma solução de inteligência artificial concebida para capacitar a população sênior, ajudando-os a manter sua independência e qualidade de vida.

O sistema utiliza múltiplos agentes de IA para fornecer assistência personalizada, proativa e contínua. Ele monitora a saúde do usuário, fornece lembretes, facilita a comunicação com cuidadores e familiares e promove o envelhecimento ativo e seguro.

---

## 🌍 Relevância do Projeto

O envelhecimento populacional é uma tendência global. Este projeto responde diretamente a esse desafio, oferecendo uma solução tecnológica que:

- Monitora a saúde
- Facilita a comunicação
- Garante a segurança

Beneficiando tanto os idosos quanto seus cuidadores e familiares.

---

## ⚙️ Funcionalidades

O sistema é composto por agentes especializados:

- **Agente de Monitoramento de Saúde**  
  Analisa sensores vestíveis (pressão arterial, batimentos cardíacos, SpO2) em tempo real e identifica sinais de alerta.

- **Agente de Interação e Lembretes**  
  Interage com o usuário por voz (simulada como texto), gerencia lembretes e verifica o bem-estar do usuário.

- **Agente de Alerta e Emergência**  
  Trata pedidos de ajuda e situações de emergência, notificando cuidadores ou serviços de socorro.

- **Agente de Relatórios**  
  Gera relatórios de saúde periódicos e os envia a cuidadores e profissionais autorizados.

---

## 🚀 Potencial Inovador

- Abordagem **proativa** e centrada no usuário
- Uso de **múltiplos agentes** especializados
- Modularidade e escalabilidade
- Promove **envelhecimento ativo, saudável e independente**

---

## 💡 Aplicações e Benefícios

### 👵 Para o Público da Terceira Idade
- Maior autonomia e independência
- Lembretes personalizados
- Monitoramento contínuo da saúde
- Comunicação facilitada
- Suporte emocional e companhia

### 👨‍⚕️ Para Cuidadores e Familiares
- Tranquilidade e segurança
- Alertas em tempo real
- Relatórios de saúde para acompanhamento
- Comunicação simplificada

### 🌐 Para a Sociedade
- Redução de custos com saúde
- Promoção do envelhecimento saudável
- Melhoria da qualidade de vida da população +60

---

## 🧪 Como Executar a Simulação

### 1. Configurar o Google Colab
Abra um novo notebook e execute a primeira célula:

```python
%pip -q install google-genai google-adk
```

### 2. Configurar a API Key do Google Gemini

```python
import os
from google.colab import userdata
os.environ["GOOGLE_API_KEY"] = userdata.get('GOOGLE_API_KEY')
```

> **Importante**: Adicione sua chave da API do Google AI Studio no menu `Runtime > Manage User Secrets`.

### 3. Copiar o Código
Cole o código Python completo nas células do Colab.

### 4. Executar a Simulação
Execute as células para simular interações com o usuário e os agentes.

---

## 🎤 Interação com a Simulação

A simulação gera dados de sensores e permite comandos de voz (simulados por texto). Exemplos:

### 🕑 Lembretes
```
Lembre-me de tomar o remédio às 9 da manhã  
Adicionar lembrete: Caminhada às 10h  
Definir lembrete: Consulta médica às 15h30  
```

### ❤️ Saúde
```
Como estou me sentindo?  
```

### 🆘 Emergência
```
Ajuda  
Emergência  
```

### 📅 Informações
```
Que dia é hoje?  
Que horas são?  
```

### ❌ Sair
```
Sair  
```

---

## 📝 Observações

Este é um **protótipo inicial**. A versão final deverá incluir:

- Integração com sensores reais
- Reconhecimento de voz real
- APIs de comunicação

Apesar disso, a simulação demonstra o potencial do sistema em promover segurança e bem-estar contínuos para pessoas idosas com necessidade de acompanhamento.
