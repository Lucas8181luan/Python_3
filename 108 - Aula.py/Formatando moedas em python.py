import Import_somar

usuário = float(input("Digite o preço = R$"))

usuárioR = Import_somar.moeda(usuário)

taxa = float(input("Taxa = "))

print(f"A metade de {usuárioR} é {Import_somar.metade(usuário)}")

print(f"O dobro de {usuárioR} é {Import_somar.dobro(usuário)}")

print(f"Aumentando 10%, temos {Import_somar.aumentar(usuário, taxa)}")

print(f"Diminuindo 10%, temos {Import_somar.diminuir(usuário, taxa)}")
