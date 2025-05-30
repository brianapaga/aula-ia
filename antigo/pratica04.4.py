contador_par = 0
contador_impar = 0

while True:
    numero = input("Insira um número inteiro: ")

    if numero.lower() == "sair":
        break

    try:
        inteiro = int(numero)
        if int(numero) % 2 == 0:
            print(f"numero {numero} é par")
            contador_par += 1
        else:
            print(f"numero {numero} é impar")
            contador_impar += 1
    except ValueError:
        print("Por favor digite um número inteiro")




print(f"total de número pares: {contador_par}")
print(f"total de número impares: {contador_impar}")