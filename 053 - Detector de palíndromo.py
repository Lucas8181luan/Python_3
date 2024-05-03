frase = str(input("Digite uma frase = ")).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("E UM PALÍNDROMO!")
else:
    print("NÃO e um PALÍNDROMO!")
