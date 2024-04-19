
casa = float(input("Qual o valor da casa = "))
salario = float(input("Qual seu salário = "))
anos = int(input("Em quantos anos = "))


prestação = casa / (anos * 12)

minimo_de_salario = salario * 30 / 100


print("Para pagar uma casa de {:.2f} em {:.2f} anos".format(casa, anos,))

print("A prestação será de = R${:.2f}".format(prestação))

if prestação <= minimo_de_salario:
    print("O empréstimo pode ser CONCEDIDO!")

else:
    print("Enpréstimo NEGADO!")