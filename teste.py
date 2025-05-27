try:
    Numerador = int(input("Digite o numerador "))
    Denominador = int(input("Digite o denominador "))
    Resultado = Numerador / Denominador
    print(f"O resultado é: {Resultado}")
except ValueError:
    print("Valor Inválido ")
except ZeroDivisionError:
    print("Error! Não é possivel dividir por zero  ")
