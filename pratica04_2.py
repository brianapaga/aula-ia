soma = 0
cont = 0
while True:
    entrada = (input("Digite uma nota entre 0 e 10 ou digite 'fim' "))
    if entrada.lower() == "fim":
        break
    try:
        nota = float(entrada)
    except ValueError:
        print("Você deve digitar um numero")
        continue
    if nota >= 0 and nota <= 10:
        soma = soma + nota
        cont = cont + 1
    else:
        print("Digite notas entre 0 e 10")
media = soma / cont
print(f"media da turma = {media:.2f}")

