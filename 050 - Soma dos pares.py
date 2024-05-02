soma  = 0
cont = 0

for Digite in range(0, 6):
    
    primeiro = int(input("Digite o {}º valor = ".format(Digite)))
    
    if primeiro % 2 == 0:
        soma += primeiro
        cont += 1
print("Você me informou {} números PARES é a soma deles é = {}".format(cont, soma))
