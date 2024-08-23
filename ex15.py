import random

def lancamento_dados(num_dados, jogadas):
    frequencias = {i: 0 for i in range(1, 7)}

    for _ in range(jogadas):
        for _ in range(num_dados):
            res = random.randint(1, 6)
            frequencias[res] += 1

    for face, frequencia in frequencias.items():
        print(f"Face {face}: {frequencia} vezes")

num_dados = 2
jogadas = 100

lancamento_dados(num_dados, jogadas)