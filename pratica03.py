# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).

idade = 10

if (idade >= 0 and idade <=12):
    print("Criança")
elif  (idade<17):
     print("adolescente")
elif(idade<59):
     print("Adulto")
else:
     print("Idoso")

print("----------------------------------------------------------------------------")
# 2- Calculadora de IMC

# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# < 18.5: classificacao = "Abaixo do peso"
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"

peso = 180
altura = 1.70

imc = peso/(altura **2)

print(f"Seu imc(kg/m²) é {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")

print("----------------------------------------------------------------------------")

# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = 10.0
origem = "C"
temperaturafinal = "K"

if origem==temperaturafinal:
    resultado = temperatura
elif origem == "C" and temperaturafinal == "F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and temperaturafinal == "K":
    resultado = temperatura + 273.15
elif origem == "F" and temperaturafinal == "C":
    resultado = (temperatura - 32) * 5/9
elif origem == "F" and temperaturafinal == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K" and temperaturafinal == "C":
    resultado = temperatura - 273.15
elif origem == "K" and temperaturafinal == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = None

if resultado is not None:
    print(f"{temperatura}°{origem} = {resultado:.2f}°{temperaturafinal}")
else:
    print("unidade inválida, use apenas C, F ou K.")

# 4- Verificador de Ano Bissexto

# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.


ano = int(input("Digite uma data no formado AAAA: "))
if ano%4 != 0:
    print("Não é um ano bissexto.")
elif ano%100 == 0:
    if ano%400 == 0:
        print("E um ano bissexto.")
    else:
        print("Não é um ano bissexto.")
else:
    print("É um ano bissexto.")