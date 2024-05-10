resposta = "S"
soma = quantidade = média = maior = menor =0

while resposta in "Ss":
    numero = int(input("Digite um número = "))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("Quer continuar? [S/N] = ")).upper().strip()[0]

média = soma / quantidade
print("Você digitou {} números e a média foi {}".format(quantidade, média))
print("O maior valor foi {} e o manor foi {}".format(maior, menor))
