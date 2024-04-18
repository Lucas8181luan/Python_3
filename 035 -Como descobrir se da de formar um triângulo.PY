# COMO DESCOBRIR SE DA DE FORMAR UM TRIÂNGULO

print("-=-" * 8)
print("ANALISADOR DE TRIÂNGULO")
print("-=-" * 8)

primeiro = float(input("Primeiro segmento = "))
segundo = float(input("Segundo segmento = "))
terceiro = float(input("Terceiro segmento = "))

if primeiro < segundo + terceiro and segundo < terceiro + primeiro and terceiro < primeiro + segundo:
    print("Isso FORMAR um triângulo!")

else:
    print("Isso NÃO FORMAR um triângulo!")
