def calc_juros_compostos(principal, taxa_juros, num_periodos):
    valor = principal * (1 + taxa_juros) ** num_periodos
    return valor


valor_inicial = 1000 
taxa_juros_anual = 0.05   
num_anos = 10            

valor = calc_juros_compostos(valor_inicial, taxa_juros_anual, num_anos)
print(f"O valor futuro do investimento é: R${valor:.2f}")