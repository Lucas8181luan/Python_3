futebol = {}
gols = []
soma_gol = 0
cont = 0
jogador = str(input("Nome do Jogador = "))
futebol["nome"] = jogador
partidas = int(input(f"Quantas partidas {jogador} jogou = "))
for i in range(0, partidas):
    gol = int(input(f"  Quantos gols na partida {i + 1} = "))
    soma_gol += gol
    gols.append(gol)
futebol["gols"] = gols[:]
futebol["total"] = soma_gol
print("=" * 40)
print(futebol)
print("=" * 40)
for k, v in futebol.items():
    print(f"O campo {k} tem o valor {v}")
print("=" * 40)
print(f"O jogador {futebol['nome']} jogou {partidas} partidas.")
for i in futebol["gols"]:
    cont += 1
    print(f"  => Na partida {cont}, fez {i} gols.")
print(f"Foi um total de {futebol['total']} gols.")
