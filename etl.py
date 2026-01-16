#1 EXTRACT
def extract():
    # Simulando dados que viriam de uma lista ou API
    return [
        {"id": 1, "nome": "Ana", "saldo": 500.0},
        {"id": 2, "nome": "Bruno", "saldo": 15000.0},
        {"id": 3, "nome": "Carla", "saldo": 0.0}
    ]

#2 TRANSFORM
def transform(usuarios):
    for usuario in usuarios:
        nome = usuario['nome']
        saldo = usuario['saldo']
        if saldo > 10000:
            usuario['mensagem'] = f"Olá {nome}! Investimento Premium disponível para você."
        else:
            usuario['mensagem'] = f"Olá {nome}! Comece a poupar hoje mesmo."
    return usuarios

#3 LOAD
def load(usuarios):
    print("Gerando relatório...")
    with open('mensagens_clientes.txt', 'w', encoding='utf-8') as f:
        for u in usuarios:
            f.write(f"ID: {u['id']} - Msg: {u['mensagem']}\n")
    print("Sucesso! O arquivo 'mensagens_clientes.txt' foi criado.")

# EXECUÇÃO DO PIPELINE ---
dados = extract()
dados_com_mensagens = transform(dados)
load(dados_com_mensagens)