print("_" * 30)
print("     LOJA DO SUPER BARATÃO     ")
print("_" * 30)

some_compras = cont_custando = cont_barato = cont = 0
nome_do_produto_barato = ''

while True:
    produto = str(input("Nome do Produto = "))
    
    preço = float(input("Preço = R$"))
    
    cont += 1
    
    some_compras += preço

    if preço > 1000:
        cont_custando += 1

    if cont == 1 or preço < cont_barato:
        cont_barato = preço
        nome_do_produto_barato = produto

    continuar = ' '
    while continuar not in "NS":
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]
    
    if continuar == "N":
        break

print("========== FIM DO PROGRAMA ==========")

print(f"-> O total de compras foi R${some_compras:.2f}\n-> Temos {cont_custando} produtos custando mais de R$1000.00\n-> O produto mais barato foi {nome_do_produto_barato} que custa R${cont_barato:.2f}")
