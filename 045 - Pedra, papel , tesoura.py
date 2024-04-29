import random
import emoji
import time

escolha = int(input('''Digite um número para a opção escolhida:
Pedra = [1]
Papel = [2]
Tesoura = [3]
Escolha = '''))

Pedra = emoji.emojize("Pedra :mountain:")
Papel = emoji.emojize("Papel :page_facing_up:")
Tesoura = emoji.emojize("Tesoura :scissors:")

lista = [Pedra, Papel, Tesoura]

jogo = random.choice(lista)

if escolha == 1:
    time.sleep(1)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO!!!")
    time.sleep(1)
    print("-=-" * 8)
    print("Você escolheu = PEDRA")
    print("A maquina escolheu = {}".format(jogo))
    print("-=-" * 8)
elif escolha == 2:
    time.sleep(1)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO!!!")
    time.sleep(1)
    print("-=-" * 8)
    print("Você escolheu = PAPEL")
    print("A maquina escolheu = {}".format(jogo))
    print("-=-" * 8)
elif escolha == 3:
    time.sleep(1)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO!!!")
    time.sleep(1)
    print("-=-" * 8)
    print("Você escolheu = TESOURA")
    print("A maquina escolheu = {}".format(jogo))
    print("-=-" * 8)
else:
    print("Escolha uma das opções TENTE NOVAMENTE")
if escolha == 1 and jogo == Pedra :
    print("EMPATE")
    print("-=-" * 8)
elif escolha == 2 and jogo == Papel :
    print("EMPATE")
    print("-=-" * 8)
elif escolha == 3 and jogo == Tesoura :
    print("EMPATE")
    print("-=-" * 8)
elif escolha == 1 and jogo == Papel or escolha == 2 and jogo == Tesoura or escolha == 3 and jogo == Pedra:
    print("Você PERDEU")
    print("-=-" * 8)
else:
    print("Você GANHOU")
    print("-=-" * 8)
