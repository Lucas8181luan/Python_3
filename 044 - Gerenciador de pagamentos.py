print("======== LOJA ========")

compra = int(input(("Preço das compras = R$")))

print('''FORMAS DE PAGAMENTO:
[1] á vista dinheiro/cheque
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input("Qual é a opção = "))

if opção == 1:
    n1 = compra - (compra * 10 / 100)
    print("Sua compra vai custar R${:.2f}".format(n1))
elif opção == 2:
    n2 = compra - (compra * 5 / 100)
    print("Sua compra vai custar R${:.2f}".format(n2))
elif opção == 3:
    soma = compra / 2
    print("Sua compra sera parcelada em 2x de R${:.2f}".format(soma))
    print("Sua compra vai custar R${:.2f} SEM JUROS".format(compra))
elif opção == 4:
    parcelas = int(input("Quantas parcelas = "))
    n4 = compra + (compra * 20 / 100)
    soma = n4 / parcelas
    print("Sua compra sera parcelada em {}X de R${:.2f} COM JUROS".format(parcelas, soma))
    print("Sua compra de R${:.2f} vai custar R${:.2f} NO FINAL".format(compra, n4))
else:
    print("Digite uma das opções que aparecer TENTE NOVAMENTE")
