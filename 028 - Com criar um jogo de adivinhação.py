# Como montar um jogo de adivinhação

# if = se
# else = senão
import random
import time

numero = random.randint(0, 5)
print("-=--=-" * 8)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=--=-" * 8)

resposta = int(input("Que número pensei = "))

print("PROCESSANDO...")
time.sleep(3)

if resposta == numero:
    print("Ganhou")
else:
    print("Perdeu, você digitou {} mas o número certo é = {}".format(resposta, numero))   






