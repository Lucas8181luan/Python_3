número = cont = soma = 0


while número != 999:
   
    número = int(input("Digite um número [999 para parar] = "))

    cont += 1
    soma += número

print("-=-" * 8)
print("Você digitou tantos {} números e a soma entre eles foi {}".format(cont - 1, soma - 999))
print("-=-" * 8)
print("FIM!")
