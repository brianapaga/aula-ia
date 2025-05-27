#1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
#* Valor em reais: R$ 100.00
#* Taxa do dólar: R$ 5.20
#* Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valoremreais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valordolar = valoremreais / taxa_dolar
valor_euro = valoremreais / taxa_euro

print (f"Valor em Reais: {valoremreais:.2f}")
print (f"Valor em Dolar: {valordolar:.2f}")
print (f"Valor em Euros: {valor_euro:.2f}")
print ("--------------------------------------------------------------")
#2- Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#* Nome do produto: "Camiseta"
#* Preço original: R$ 50.00
#* Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

produto = "Camiseta"
precooriginal  = 50.00
precodesconto = 20

valordesconto = precooriginal * (precodesconto / 100)
preco_final = precooriginal - valordesconto

print(f"produto: {produto}")
print(f"preço original: R$ {precooriginal:.2f}")
print(f"Desconto: {precodesconto}%")
print(f"Valor do desconto: R$ {valordesconto:.2f}")
print(f"Preço com desconto R$ {preco_final:.2f}")
print ("--------------------------------------------------------------")

#3- Calculadora de Média Escolar
#Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

#* Nota 1: 7.5
#* Nota 2: 8.0
#* Nota 3: 6.5
#O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"nota1: {nota1:.2f} ")
print(f"nota2: {nota2:.2f} ")
print(f"nota3: {nota3:.2f} ")
print(f"Média final: {media:.2f} ")
print ("--------------------------------------------------------------")
#4- Calculadora de Consumo de Combustível
#Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

#* Distância percorrida: 300 km
#* Combustível gasto: 25 litros
#O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais

print("Calculadora de Consumo de Combustível")

distanciaPercorrida = 300
combustivelgasto = 25

consumomedio = distanciaPercorrida / combustivelgasto
print(f"A distancia percorrida foi {distanciaPercorrida} km")
print(f"O combustível gasto foi {combustivelgasto} litros")
print(f"Consumo médio foi {consumomedio} litros")

