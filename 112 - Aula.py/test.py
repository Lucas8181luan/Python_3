from Utilidades import Moedas, Dados

usuário = str(input("Digite o preço = R$"))

try:
    N_usuário = Dados.verificar(usuário)

    R_usuário = Moedas.moeda(N_usuário)

    v = True

    taxa = float(input("Taxa = "))

    print(f"A metade de {R_usuário} é {Moedas.metade(N_usuário, v)}")

    print(f"O dobro de {R_usuário} é {Moedas.dobro(N_usuário, v)}")

    print(f"Aumentando 10%, temos {Moedas.aumentar(N_usuário, taxa, v)}")

    print(f"Diminuindo 10%, temos {Moedas.diminuir(N_usuário, taxa, v)}")

except ValueError:
    print(f"ERRO! {usuário} é um preço inválido!")
