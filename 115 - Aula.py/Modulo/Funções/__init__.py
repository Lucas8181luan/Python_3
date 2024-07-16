def menu():
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
        elif usuario == 3:
            print("-" * 40)
            print("Saindo do sistema... Até logo!")
            print("-" * 40)
            break
        # PARTE 3 - FINAL
