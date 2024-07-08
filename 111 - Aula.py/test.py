from Utilidades import Moedas

usuário = float(input("Digite o preço = R$"))

usuárioR = Moedas.moeda(usuário)

v = True

taxa = float(input("Taxa = "))

print(f"A metade de {usuárioR} é {Moedas.metade(usuário, v)}")

print(f"O dobro de {usuárioR} é {Moedas.dobro(usuário, v)}")

print(f"Aumentando 10%, temos {Moedas.aumentar(usuário, taxa, v)}")

print(f"Diminuindo 10%, temos {Moedas.diminuir(usuário, taxa, v)}")
