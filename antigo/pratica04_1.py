while True:
    try:
        numero1 = float(input("Digite o primeiro número "))
        numero2 = float(input("Digite o segundo número "))
        operacao = input("Digite a operação (+, -, *, /)")

        if operacao == "+":
            print("Resultado: ", numero1 + numero2)
            break
        elif operacao == "-":
            print("Resultado: ", numero1 - numero2)
            break
        elif operacao == "*":
            print("Resultado: ", numero1 * numero2)
            break
        elif operacao == "/":
            if numero2 == 0:
                print("ERROR!!!! Divisão por zero")
            else:
                print("Resultado: ", numero1 / numero2)
                break
        else:
            print("Operação inválida")
    except:
        print("Error!!! Entrada inválida")
