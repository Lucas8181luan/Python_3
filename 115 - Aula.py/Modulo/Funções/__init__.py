def criar_arquivo():
    try:
        import os
        diretoria = "115 - Aula.py/Modulo/Pessoas"
        nome = "Pessoas.csv"
        caminho_completo = os.path.join(diretoria, nome)
        with open(caminho_completo, "x") as arquivo:
            arquivo.write("")
        
        print(f"O arquivo {nome} foi criado com sucesso.")
    except FileExistsError:
        return 


def menu():
    criar_arquivo()
    while True:
        # PARTE 1
        cont = 0
        print("-" * 40)
        print(f"{"MENU PRINCIPAL":^40}")
        print("-" * 40)
        opcs = ["Ver pessoas cadastradas", "Cadastrar nova Pessoa", "Sair do Sistema"]
        for i in opcs:
            cont += 1
            print(f"\033[33m{cont} - \033[0m",end="")
            print(f"\033[34m{i}\033[0m")
        print("-" * 40)
        # PARTE 1 - FINAL

        # PART 2
        usuario = 0
        while usuario != 1 and usuario != 2 and usuario != 3:
            try:
                usuario = int(input("Sua opção = "))
            except ValueError:
                print("\033[31mERRO: Digite uma opção válida\033[0m")
            if usuario > 3:
                print("\033[31mERRO: Digite um número inteiro válida\033[0m")
                break
        # PARTE 2 - FINAL

        # PARTE 3
        if usuario == 1 or usuario == 2:
            print("-" * 40)
            opção = f"Opção {usuario}"
            print(f"{opção:^40}")
            print("-" * 40)
            if usuario == 1:
                import pandas as pd
                caminho_aqv = "115 - Aula.py/Modulo/Pessoas/Pessoas.csv"
                df = pd.read_csv(caminho_aqv)
                print(f"{df.to_string(index=False)}")

        elif usuario == 3:
            print("-" * 40)
            print("Saindo do sistema... Até logo!")
            print("-" * 40)
            break
        # PARTE 3 - FINAL
