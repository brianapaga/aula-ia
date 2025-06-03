import requests

def consulta_cep(cep:str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url)
        dados = response.json()
        if "erro" in dados:
            print("CEP não encontrado")
        else:
            print(f"\n logradouro: {dados['logradouro']}")
            print(f"\n Bairro: {dados['bairro']}")
            print(f"\n Cidade: {dados['localidade']}")
            print(f"\n Estado: {dados['uf']}")
    except Exception as e:
        print(f"Erro na consulta: {e}")
    

cep = input("Digite seu cep: ")
consulta_cep(cep)
