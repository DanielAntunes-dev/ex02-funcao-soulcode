def analisar_sentimento(texto):
    palavras_positivas = ["bom", "feliz", "alegre", "ótimo", "maravilhoso", "excelente", "positivo", "sucesso"]
    palavras_negativas = ["ruim", "triste", "horrível", "péssimo", "terrível", "negativo", "falha", "problema"]

    contagem_positiva = 0
    contagem_negativa = 0

    palavras = texto.lower().split()

    for palavra in palavras:
        if palavra in palavras_positivas:
            contagem_positiva += 1
        elif palavra in palavras_negativas:
            contagem_negativa += 1

    if contagem_positiva > contagem_negativa:
        return "Sentimento Positivo"
    elif contagem_negativa > contagem_positiva:
        return "Sentimento Negativo"
    else:
        return "Sentimento Neutro"

texto1 = "Este é um dia maravilhoso e ótimo!"
texto2 = "Estou me sentindo muito triste e horrível hoje."
texto3 = "Hoje é um dia comum, nada de especial."

print(analisar_sentimento(texto1))  
print(analisar_sentimento(texto2))  
print(analisar_sentimento(texto3))  
