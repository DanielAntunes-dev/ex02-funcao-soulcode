from datetime import datetime

def converter_data(data):
    try:
        data = datetime.strptime(data, "%d/%m/%Y")
        return data.strftime("%Y-%m-%d")
    except ValueError:
        return "Data inválida, insira no formato DD/MM/YYYY."

data = "25/08/2024"
data_formatada = converter_data(data)
print(f"Data convertida: {data_formatada}")
