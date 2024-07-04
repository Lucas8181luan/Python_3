import import_somar

usuário = float(input("Digite o preço = R$"))

taxa = float(input("Taxa = "))

print(f"A metade de R${usuário} é R${import_somar.metade(usuário)}")

print(f"O dobro de R${usuário} é {import_somar.dobro(usuário)}")

print(f"Aumentando 10%, temos R${import_somar.aumentar(usuário, taxa):.1f}")

print(f"Diminuindo 10%, temos R${import_somar.diminuir(usuário, taxa):.1f}")
