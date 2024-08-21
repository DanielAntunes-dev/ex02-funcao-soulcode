def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)
        
def atualizar_tabuleiro(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Posição já ocupada. Escolha outra.")
        return False

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True

    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def jogar():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é a sua vez.")
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        if atualizar_tabuleiro(tabuleiro, linha, coluna, jogador_atual):
            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Parabéns, Jogador {jogador_atual}! Você venceu!")
                break
            elif verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"

jogar()
