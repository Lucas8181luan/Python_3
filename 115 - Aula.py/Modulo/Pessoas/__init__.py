def cdst_pessoas():
    import csv
    import os
    nome = str(input("Nome = "))
    idade = int(input("Idade = "))
    pessoa = f"{nome},{idade}"
    arquivo = "115 - Aula.py/Modulo/Pessoas/Pessoas.csv"
    with open(arquivo, mode="a", newline='') as arquivo_csv:
        arquivo_csv.write(pessoa + '\n')
    print(f"Novo registro de {nome} adiconado.")
