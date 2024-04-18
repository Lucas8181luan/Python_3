# COMO DESCOBRIR O PREÇO DA PASSAGEM

distancia_da_viagem = float(input("Qual a distância da viagem = "))

if distancia_da_viagem <= 200:
    preço = distancia_da_viagem * 0.50 
    
    print("Você está prestes a comecar uma viagem de = R${:.2f}".format(preço))

else:
    desconto = distancia_da_viagem * 0.45

    print("Você está prestes a comecar uma viagem, com o desconto de = R${:.2f}".format(desconto))
