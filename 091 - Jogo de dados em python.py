import time
import random
dado = {}
cont = 0
for i in range(1, 5):
    j_dado = random.randint(1, 7)
    print(f"Jogador {i} tirou {j_dado} no dado")
    dado[f"jogador {i}"] = j_dado
    time.sleep(1)
print("=" * 40)
print("  == RANKING DOS JOGADORES ==")
ordem = dict(sorted(dado.items(), key = lambda item: item[1], reverse = True))
for i, r in ordem.items():
    cont += 1
    print(f"  {cont}º lugar: {i} com {r}.")
print("=" * 40)
