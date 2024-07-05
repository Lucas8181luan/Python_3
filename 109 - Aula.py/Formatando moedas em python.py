import Import_somar

usuário = float(input("Digite o preço = R$"))

usuárioR = Import_somar.moeda(usuário)

v = True

taxa = float(input("Taxa = "))

print(f"A metade de {usuárioR} é {Import_somar.metade(usuário, v)}")

print(f"O dobro de {usuárioR} é {Import_somar.dobro(usuário, v)}")

print(f"Aumentando 10%, temos {Import_somar.aumentar(usuário, taxa, v)}")

print(f"Diminuindo 10%, temos {Import_somar.diminuir(usuário, taxa, v)}")
