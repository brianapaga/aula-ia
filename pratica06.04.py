import requests

def consultar_cotacao_moeda():
    print("Conveção de modas para Real brasileiro: BRL")
    while True:
        codigo_moeda = input("Digite o codigo da moeda (exemplo USD, EUR, ETÇ) ou 'SAIR' para encerrar:").strip().upper()
        if codigo_moeda == 'sair':
            print("Saindo do programa.")
            break
        url_api = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"
        try:
            print(f"Buscando cotação para {codigo_moeda}/BRL...")
            resposta = requests.get(url_api)
            resposta.raise_for_status()
            dados_cotacao = resposta.json()
            if not dados_cotacao or f"{codigo_moeda}brl" not in dados_cotacao:
                print(f"Não foi possivel encontra a cotação para '{codigo_moeda}'. verificar codigo da moeda ou tente outra.")
                continue
            cotacao = dados_cotacao[f"{codigo_moeda}brl"]
            valor_compra = float(cotacao.get('bid', 0.0))
            valor_venda = float(cotacao.get('ask', 0.0))
            valor_maximo = float(cotacao.get('haigh', 0.0))
            valor_minimo = float(cotacao.get('low', 0.0))
            data_atualizacao = cotacao.get('create_date','data/hora não disponivel')
            print(f"cotação de {codigo_moeda}/brl")
            print(f"Valor de compra(BID): R$ {valor_compra:.4f}")
            print(f"Valor de venda (ASK): R$ {valor_venda:.4f}")
            print(f"Valor de máximo: R$ {valor_maximo:.4f} 24 horas")
            print(f"Valor de minimo: R$ {valor_minimo:.4f}")
            print(f"Ultima atualização: R$ {data_atualizacao}")
        except:
            print("Moeda inválida, digite o codigo correto: ")
if __name__ == "__main__":
    consultar_cotacao_moeda()

