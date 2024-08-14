import math


def calculadora_cientifica():
    
    soma = lambda x, y: x + y
    subtracao = lambda x, y: x - y
    multiplicacao = lambda x, y: x * y
    divisao = lambda x, y: x / y if y != 0 else "Erro: Divisão por zero!"
    raiz_quadrada = lambda x: math.sqrt(x)
    seno = lambda x: math.sin(x)
    coseno = lambda x: math.cos(x)
    tangente = lambda x: math.tan(x)
    exponenciacao = lambda x, y: math.pow(x, y)
    logaritmo = lambda x: math.log(x) if x > 0 else "Erro: Logaritmo de número não positivo!"

    operacoes = {
        '0': ("Sair", None),
        '1': ('Soma', soma),
        '2': ('Subtracao', subtracao),
        '3': ('Multiplicação', multiplicacao),
        '4': ('Divisão', divisao),
        '5': ('Seno', seno),
        '6': ('Coseno', coseno),
        '7': ('Tangente', tangente),
        '8': ('Exponenciação', exponenciacao),
        '9': ('Logaritmo Natural', logaritmo),
        '10': ("Raiz quadrada", raiz_quadrada)
    }

    print("Calculadora Científica - Menu")
    for chave, (valor, _) in operacoes.items():
        print(f"{chave}. {valor}")

    while True:
        escolha = input("Digite o número da operação desejada ou 'sair' para encerrar: ").lower()
        
        if escolha == "sair":
            print("Saindo...")
            break
        
        if escolha in operacoes:
            valor, funcao = operacoes[escolha]
            
            if funcao is None:
                print("Saindo...")
                break
            
            if escolha in ['1', '2', '3', '4', '8']:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: ")) if escolha != '8' else float(input("Digite o expoente: "))
                resultado = funcao(numero1, numero2)
            else:
                numero = float(input("Digite o número: "))
                resultado = funcao(numero)
                
            print(f"{valor} resultado: {resultado}")
        else:
            print('Operação inválida!')

calculadora_cientifica()
