def iniciar_votacao(opcoes):
    votos = {opcao: 0 for opcao in opcoes}
    return votos

def registrar_voto(votos, opcao):
    if opcao in votos:
        votos[opcao] += 1
    else:
        print(f"A opção '{opcao}' não é válida.")

def exibir_vencedor(votos):
    vencedor = max(votos, key=votos.get)
    max_votos = votos[vencedor]
    
    empate = [opcao for opcao, voto in votos.items() if voto == max_votos]
    
    if len(empate) > 1:
        print("Houve um empate entre as seguintes opções:")
        for opcao in empate:
            print(f"{opcao} com {votos[opcao]} votos.")
    else:
        print(f"O vencedor é '{vencedor}' com {max_votos} votos.")

def sistema_de_votacao():
    opcoes = ["Opção A", "Opção B", "Opção C"]
    votos = iniciar_votacao(opcoes)

    while True:
        print("\nOpções disponíveis para votação:")
        for opcao in opcoes:
            print(opcao)
        
        voto = input("Digite sua opção (ou 'fim' para encerrar a votação): ")
        
        if voto.lower() == 'fim':
            break
        
        registrar_voto(votos, voto)
    
    exibir_vencedor(votos)

sistema_de_votacao()
