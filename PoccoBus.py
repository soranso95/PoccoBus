# Função para gerar a matriz de assentos de forma dinâmica
def gerar_matriz_assentos():
    matriz = []
 
    # Primeira linha: motorista e corredor
    matriz.append(["Mot", "Corr", "Corr", "Corr", "Corr"])
 
    # Gerar as demais fileiras dinamicamente
    assento = 1
 
    for _ in range(12):  # 12 fileiras
        linha = []
        for j in range(5):  # 5 colunas
            if j == 2:  # Corredor no meio
                linha.append("Corr")
            else:
                linha.append(f"A{assento:02}")  # Formata "A01", "A02", etc.
                assento += 1
        matriz.append(linha)
 
    return matriz
 
# Função para exibir o mapa atual dos assentos com emojis coloridos
def mostrar_assentos_coloridos(matriz):
    print("\nMapa atual dos assentos:")
    for linha in matriz:
        linha_colorida = []
        for assento in linha:
            if assento == "Mot":
                linha_colorida.append("🟦 Mot ")  # Azul para o motorista
            elif assento == "Corr":
                linha_colorida.append("🔲 Corr ")  # Branco/Cinza para o corredor
            elif assento.startswith("X-"):
                linha_colorida.append("🟥 " + assento[2:] + " ")  # Vermelho para assentos vendidos
            else:
                linha_colorida.append("🟩 " + assento + " ")  # Verde para assentos disponíveis
        print("".join(linha_colorida))
    print()
 
# Função que vende o assento solicitado, se ele estiver disponível
def vender_assento(matriz, assento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == assento:
                matriz[i][j] = "X-" + assento  # Marca como vendido
                print(f"Assento {assento} vendido com sucesso!")
                return True
    print("Assento inválido ou indisponível. Tente novamente.")
    return False
 
# Função para salvar o status final dos assentos em um arquivo .txt
def salvar_status_em_arquivo(matriz):
    with open("status_assentos.txt", "w") as arquivo:
        arquivo.write("Status final dos assentos:\n\n")
        for linha in matriz:
            arquivo.write(" ".join(linha) + "\n")
    print("Status dos assentos salvo em 'status_assentos.txt'.")
 
# Função principal que gerencia o fluxo de vendas
def principal():
    matriz_assentos = gerar_matriz_assentos()  # Gera a matriz inicial
 
    # Extrai automaticamente os assentos disponíveis
    assentos_disponiveis = {assento for linha in matriz_assentos for assento in linha if assento not in ("Mot", "Corr")}
 
    while True:
        mostrar_assentos_coloridos(matriz_assentos)
        assento_escolhido = input("Digite o assento que deseja comprar (ou 'sair' para encerrar): ").upper()
 
        if assento_escolhido == "SAIR":
            break
 
        if assento_escolhido in assentos_disponiveis:
            venda_realizada = vender_assento(matriz_assentos, assento_escolhido)
            if venda_realizada:
                assentos_disponiveis.remove(assento_escolhido)
        else:
            print("Entrada inválida! Digite um assento disponível (por exemplo, A01) ou 'sair'.")
 
    salvar_status_em_arquivo(matriz_assentos)
    print("Encerrando o sistema. Obrigado por usar a PoccoBus!")
 
# Executar o programa principal
print(principal())