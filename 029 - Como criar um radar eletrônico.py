# COMO CRIAR UM RADAR ELETRÔNICO

carro = float(input("Qual a velocidade do carro = "))

limite = 80

multa = (limite - carro) * 7

if carro <= limite:
    print("Boa viagem!")
else:
    print("Você foi multado por ultrapassar a velocidade de 80km/h com uma multa de: R${:.2f}".format(multa))


