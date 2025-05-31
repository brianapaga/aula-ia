import requests

cep = "01001000"
url = f"https://viacep.com.br/ws/{cep}/json/"

# Faz a requisição
dados = requests.get(url).json()

# Verifica se a cidade é São Paulo
if dados["localidade"] == "São Paulo":
    # Escreve no arquivo se for São Paulo
    with open("teste.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("O CEP pertence à cidade de São Paulo.\n")
        arquivo.write(f"Logradouro: {dados['logradouro']}\n")
        arquivo.write(f"Bairro: {dados['bairro']}\n")
        arquivo.write(f"UF: {dados['uf']}")
    print("✅ Arquivo criado com sucesso.")
else:
    print("❌ A cidade não é São Paulo.")
