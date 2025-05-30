def verifica_palindromo(palavra):
    palavra = palavra.lower()
    palavra_reverso = palavra[::-1]
    if palavra == palavra_reverso:
        print("Sim")
    else:
        print("Não")
verifica_palindromo("ovo ovo")