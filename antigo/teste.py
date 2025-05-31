import requests

cep = "06455000"
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()

print(dados)

