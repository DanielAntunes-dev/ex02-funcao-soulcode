import random
from collections import Counter

def gerar_numeros_aleatorios(quantidade, inicio, fim):
    return [random.randint(inicio, fim) for _ in range(quantidade)]

def calcular_media(numeros):
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    numeros_ordenados = sorted(numeros)
    meio = len(numeros_ordenados) // 2
    
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    else:
        return numeros_ordenados[meio]

def calcular_moda(numeros):
    contagem = Counter(numeros)
    frequencia_maxima = max(contagem.values())
    modas = [numero for numero, frequencia in contagem.items() if frequencia == frequencia_maxima]
    
    if len(modas) == len(numeros):
        return "Não há moda"
    else:
        return modas

def analisar_numeros_aleatorios(quantidade, inicio, fim):
    numeros = gerar_numeros_aleatorios(quantidade, inicio, fim)
    
    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    
    print(f"Números gerados: {numeros}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    
analisar_numeros_aleatorios(20, 1, 10)
