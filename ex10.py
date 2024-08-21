import random

def simular_temperaturas(cidades, dias=7):
    dados_temperatura = {}
    
    for cidade in cidades:
        temperaturas = [random.randint(-10, 40) for _ in range(dias)]
        dados_temperatura[cidade] = temperaturas
    
    return dados_temperatura

def calcular_estatisticas(dados_temperatura):
    estatisticas = {}
    
    for cidade, temperaturas in dados_temperatura.items():
        media = sum(temperaturas) / len(temperaturas)
        max_temp = max(temperaturas)
        min_temp = min(temperaturas)
        estatisticas[cidade] = {
            'media': media,
            'max': max_temp,
            'min': min_temp
        }
    
    return estatisticas
  
def exibir_estatisticas(estatisticas):
    for cidade, dados in estatisticas.items():
        print(f"\nCidade: {cidade}")
        print(f"Temperatura Média: {dados['media']:.2f}°C")
        print(f"Temperatura Máxima: {dados['max']}°C")
        print(f"Temperatura Mínima: {dados['min']}°C")


def sistema_de_simulacao_de_temperatura():
    cidades = ["Rio de Janeiro", "São Paulo", "Belo Horizonte", "Curitiba", "Porto Alegre"]
    dados_temperatura = simular_temperaturas(cidades)
    estatisticas = calcular_estatisticas(dados_temperatura)
    
    exibir_estatisticas(estatisticas)

sistema_de_simulacao_de_temperatura()
