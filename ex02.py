def conversor_de_temperatura():
    celsius_para_fahrenheit = lambda c: (c * 9/5) + 32
    fahrenheit_para_celsius = lambda f: (f - 32) * 5/9
    
    valor = float(input("Digite um valor: "))
    print("Ao escolher Celsius, a conversão será para Fahrenheit, e vice-versa")

    while True:
        temperatura = input("Converter para (1 - Celsius/2 - Fahrenheit): ")
        if temperatura in ["1", "2"]:
            break
        else:
            print("Opção inválida")

    if temperatura == "1":
        resultado = celsius_para_fahrenheit(valor)
        unidade_original = 'ºC'
        unidade_convertida = 'ºF'
    else:
        resultado = fahrenheit_para_celsius(valor)
        unidade_original = 'ºF'
        unidade_convertida = 'ºC'

    print(f"{valor}{unidade_original} convertido para {unidade_convertida} é {resultado:.1f}{unidade_convertida}")

conversor_de_temperatura()
