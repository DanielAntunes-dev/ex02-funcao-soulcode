import re
from collections import Counter

def analisar_texto(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto).lower()
    
    palavras = texto_limpo.split()
    num_palavras = len(palavras)

    frases = re.split(r'[.!?]+', texto)
    frases = [frase.strip() for frase in frases if frase.strip()]  
    num_frases = len(frases)
    
    num_caracteres = len(texto)
    
    frequencia_palavras = Counter(palavras)
   
    print(f"Número de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")
    print(f"Número de caracteres: {num_caracteres}")
    print("\nFrequência das palavras:")
    for palavra, frequencia in frequencia_palavras.items():
        print(f"'{palavra}': {frequencia} vez(es)")

texto_exemplo = """
Aprender análise de dados é essencial no mundo moderno. 
Com a análise de dados, podemos descobrir padrões, tomar decisões informadas, e prever tendências. 
A análise de dados é usada em diversas áreas, desde o marketing até a ciência. 
Ela envolve coletar, processar e interpretar grandes volumes de informação. 
Com as ferramentas certas, podemos transformar dados brutos em insights valiosos. 
A análise de dados exige habilidades em estatística, programação e pensamento crítico. 
À medida que a demanda por analistas de dados cresce, aprender essas habilidades abre portas 
para muitas oportunidades no mercado de trabalho.
"""

analisar_texto(texto_exemplo)
