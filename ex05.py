def ordenar(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        lesser = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return ordenar(lesser) + [pivot] + ordenar(greater)

def ordenar_lista(lista, ordem='crescente'):
    if ordem == 'crescente':
        return ordenar(lista)
    elif ordem == 'decrescente':
        return ordenar(lista)[::-1]
    else:
        raise ValueError("A ordem deve ser 'crescente' ou 'decrescente'.")

# Exemplo de uso:
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
strings = ["banana", "laranja", "uva", "maçã", "abacaxi"]

print("Lista de números ordenada em ordem crescente:", ordenar_lista(numeros))
print("Lista de números ordenada em ordem decrescente:", ordenar_lista(numeros, ordem='decrescente'))
print("Lista de strings ordenada em ordem crescente:", ordenar_lista(strings))
print("Lista de strings ordenada em ordem decrescente:", ordenar_lista(strings, ordem='decrescente'))
