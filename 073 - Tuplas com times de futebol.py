times = ("Vasco", "Palmeiras", "Flamengo", "Botafogo", "Santos", "Fluminense", "Cuiaba", "São Paulo", "Cruzeiro", "Internacional")

times_ordem_alfabética = tuple(sorted(times))

posição = times.index("Vasco") + 1

print("-=" * 20)
print(f"Lista de times do Brasileirão = {times}")
print("-=" * 20)
print(f"Os 5 primeiros são = {times[0:5]}")
print("-=" * 20)
print(f"Os 4 últimos são = {times[- 4:]}")
print("-=" * 20)
print(f"Times em ordem alfabética = {times_ordem_alfabética}")
print("-=" * 20)
print(f"O Vasco está na {posição}º posição")
