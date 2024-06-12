import copy
futebol = {}
lista_futebol = []
gols = []
cont = cont_n = cont_g = 0
while True:
    futebol["nome"] = str(input("Nome do jogador = "))
    futebol["partidas"] = int(input(f"Quantas partidas {futebol['nome']} jogou = "))
    for i in range(0, futebol["partidas"]):
        gols.append(int(input(f"Quantos gols na partida {i + 1} = ")))
        copia_gols = copy.deepcopy(gols)
        futebol["gols"] = copia_gols
        futebol["total de gols"] = sum(gols)
    copia = copy.deepcopy(futebol)
    lista_futebol.append(copia)
    gols.clear()
    while True:
        continuar = str(input("Quer continuar [S/N] = ")).upper().strip()[0]
        if continuar == "N":
            break
        elif continuar == "S":
            break
        else:
            print("ERRO! Escolha apenas [S/N]")
    if continuar == "N":
        break
print("=" * 40)
print(f"{"Code nome":^0}        gols        total")
print("_" * 40)
for i in lista_futebol:
    cont += 1
    print(f"{cont:^0}    {i['nome']}       {i['gols']}       {i['total de gols']}")
print("_" * 40)
while True:
    mostrar = int(input("Mostrar dados de qual jogador: (999 para parar) = "))
    mostrar_e = mostrar
    mostrar -= 1
    if mostrar < len(lista_futebol):
        print(f"-- LEVANTAMENTO DO JOGADOR {lista_futebol[mostrar]['nome']}--")
        for i in range(len(lista_futebol[mostrar]["gols"])):
            cont_n += i + 1
            cont_g = i    
            print(f"   No jogo {cont_n} fez {lista_futebol[mostrar]['gols'][cont_g]} gols")
            cont_n = 0
            cont_g = 0
    if mostrar_e > len(lista_futebol) and mostrar_e != 999:
        print(f'Erro! Não existe jogador com código {mostrar + 1}!')
    if mostrar == 998:
        break
print("<< VOLTE SEMPRE >> ")
