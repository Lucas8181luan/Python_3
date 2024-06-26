def ficha_jogador():
    nome = str(input("Nome do Jogador = "))
    if nome == "":
       nome = "<desconhecido>"
    try:
        gols = int(input("Números de Gols = "))
    except ValueError:
        gols = 0
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


ficha_jogador()
