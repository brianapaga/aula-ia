import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        dados = response.json()
        user = dados['results'][0]
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']
        print(f"\n nome: {nome}, email: {email}, pais {pais}")
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")

gerar_usuario_aleatorio()
        
