import math

def calculadora_cientifica(escolha, numero1=None, numero2=None):
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
        '10': ('Raiz quadrada', raiz_quadrada)
    }

    if escolha in operacoes:
        
        valor, funcao = operacoes[escolha]
        if escolha == "0":
            print("Saindo...")
            return None
        elif escolha in ['1', '2', '3', '4', '8']:
            resultado = funcao(numero1, numero2)
        else:
            resultado = funcao(numero1)
        
            
        print(f"{valor} resultado: {resultado}")
        return resultado
    else:
        print('Operação inválida!')
        return None


def teste_calculadora():
    calculadora_cientifica('1', 10, 5) 
    calculadora_cientifica('3',10, 4)
    calculadora_cientifica('0')

teste_calculadora()
