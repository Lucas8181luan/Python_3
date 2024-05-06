import random

print("Sou seu computador...")
print("-=-" * 8)

pc_resposta = random.randint(0, 10)

print('''Acabei de pensar em um número de 0 a 10. Será que você consegue adivinhar qual foi?''')

acertou = False

cont = 0

while not acertou:
    
    print("-=-" * 8)
    resposta = int(input("Qual é seu palpite = "))
    print("-=-" * 8)
    
    cont += 1
    
    if resposta == pc_resposta:
        acertou = True
    else:
        if resposta < pc_resposta:
            print("Mais...Tente mais uma vez")
           
        elif resposta > pc_resposta:
            print("Menos...Tente mais uma vez")
           
print("Acertou com {} tentativas. Parabéns!".format(cont))
