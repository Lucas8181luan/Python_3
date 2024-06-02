import random
import time 

lista = []
cont = 0

print("=" * 30)
jogo = "JOGA NA MEGA SENA"
print(f"{jogo:^30}")
print("=" * 30)

jogos = int(input("Quantos jogos você quer que eu sorteie = "))

print(f"========== SORTEANDO {jogos} JOGOS ==========")
time.sleep(3)

for i in range(jogos):
    numeros = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    lista.append(numeros[:])
    numeros.clear()

for n in lista:
    cont += 1
    print(f"Jogo {cont} = {n}")
print("============ < BOA SORTE! > ============")
