def validador():
    cpf = input("Digite o CPF: ")

    numeros = [int(digito) for digito in cpf if digito.isdigit()]

    if len(numeros) != 11 or numeros == numeros[0] * 11:
        print(f"O CPF {cpf} não é válido, tente novamente ..")
        return

    # Cálculo do primeiro dígito verificador
    soma_produtos = 0
    for i in range(9):
        soma_produtos += numeros[i] * (10 - i)

    digito_esperado = (soma_produtos * 10) % 11
    if digito_esperado == 10:
        digito_esperado = 0

    if numeros[9] != digito_esperado:
        print(f"O CPF {cpf} não é válido, tente novamente ..")
        return

    # Cálculo do segundo dígito verificador
    soma_produtos1 = 0
    for i in range(10):
        soma_produtos1 += numeros[i] * (11 - i)

    digito_esperado1 = (soma_produtos1 * 10) % 11
    if digito_esperado1 == 10:
        digito_esperado1 = 0

    if numeros[10] == digito_esperado1:
        print(f"O CPF {cpf} é válido.")
    else:
        print(f"O CPF {cpf} não é válido, tente novamente ..")

validador()
