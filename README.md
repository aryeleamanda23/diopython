# Pipeline de ETL com Python: Geração de Mensagens Personalizadas

## 📝 Descrição do Projeto
Este projeto demonstra um fluxo completo de **ETL (Extract, Transform, Load)** desenvolvido em Python. O objetivo é simular um cenário real de marketing bancário, onde dados de clientes são extraídos, processados por uma lógica de negócio (simulando uma IA) e carregados em um relatório final.

Este desafio faz parte do bootcamp "Explorando IA Generativa em um Pipeline de ETL com Python" da DIO.

## ⚙️ O Fluxo ETL

### 1. Extract (Extração)
Os dados foram estruturados em uma lista de dicionários Python, simulando a extração de uma base de dados de clientes contendo:
- ID do cliente
- Nome
- Saldo Bancário

### 2. Transform (Transformação)
Foi aplicada uma lógica de transformação para segmentar os clientes:
- **Saldos acima de R$ 10.000,00:** Recebem uma mensagem sobre investimentos Premium.
- **Saldos abaixo de R$ 10.000,00:** Recebem um incentivo para começar a poupar.
Esta etapa simula o enriquecimento de dados que poderia ser feito através de uma API de IA Generativa.

### 3. Load (Carregamento)
Os dados transformados são exportados para um arquivo de texto (`mensagens_clientes.txt`), consolidando o relatório final pronto para ser utilizado por outras equipes ou sistemas.

## 🚀 Como executar
1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório.
3. Execute o comando:
   ```bash
   python etl.py
