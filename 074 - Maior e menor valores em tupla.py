import random

sorteio = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)

print(f"Os valores sorteados foram = {sorteio}")

maior = max(sorteio)
menor = min(sorteio)

print(f"O maior valor sorteado foi = {maior}")
print(f"O menor valor sorteado foi = {menor}")
