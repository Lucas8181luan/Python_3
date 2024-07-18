def criar_arquivo():
    try:
        import os
        diretoria = "115 - Aula.py/Modulo/Pessoas"
        nome = "Pessoas.csv"
        caminho_completo = os.path.join(diretoria, nome)
        with open(caminho_completo, "x") as arquivo:
            arquivo.write(f"")
        
        print(f"O arquivo {nome} foi criado com sucesso.")
    except FileExistsError:
        return 
