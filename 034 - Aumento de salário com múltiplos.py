# AUMENTO DE SALÁRIO COM MÚLTIPLOS

funcionario = float(input("Qual é o salário do funcionário = "))

# Não colocar . no número en if
if funcionario <= 1250:
   # Outra formar de calcular
   soma_final = funcionario + (funcionario * 15 / 100)

else:
    soma_1 = (10/100)
    soma_2 = soma_1 * funcionario
    soma_final = soma_2 + funcionario
 
print("O salário do funcionário era {:.2f} é agora é = R${:.2f}".format(funcionario, soma_final))


