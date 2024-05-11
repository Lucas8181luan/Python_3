while True:
    
    print("-=-" * 12)
    usuario = int(input("Quer ver a tabuada de qual valor = "))
    print("-=-" * 12)

    if usuario < 0:
        break

    for tabuada in range(1, 11):
        soma = usuario * tabuada

        print(f"{usuario} x {tabuada} = {soma}")

print("PROGRAMA VER A TABUADA ENCERRADO. Volte sempre!")

print("-=-" * 12)
