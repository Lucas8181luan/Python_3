valor = list(str(input("Digite a expressão = ")))
n1 = "("
n2 = ")"
cont1 = valor.count(n1)
cont2 = valor.count(n2)
soma = cont1 + cont2
if soma % 2 == 0:
    print("Sua expressão está válida!") 
else:
    print("Sua expressão está errada!")
