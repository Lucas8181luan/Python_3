lista = []

for valor in range(0, 5):

    usuario = int(input("Digite um valor = "))

    if valor == 0 or usuario > lista[-1]:
        lista.append(usuario)
        print("Adicionado ao final da lista..")
    else:
        proximo = 0
        while proximo < len(lista):
            if usuario <= lista[proximo]:
                lista.insert(proximo, usuario)
                print(f"Valor adicionado na posição {proximo} da lista ...")
                break
            proximo =+ 1

print("-=" * 30)
print(f"Os valores digitados em ordem foram = {lista}")
