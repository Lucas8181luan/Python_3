def ajuda():
    while True:
        n_l = "SISTEMA DE AJUDA PyHELP"
        cont_1 = cont_2 = cont_3 = 0
        for i in n_l:
            cont_1 += 1
        print("\033[92m" + "~" * cont_1)
        print(n_l)
        print("~" * cont_1 + "\033[0m")
        resp = str(input("Função ou Biblioteca > "))
        if resp == "fim":
            fim = "ATÉ LOGO"
            for i in fim:
                cont_3 += 1
            print("\033[91m" + "~" * cont_3)
            print(fim)
            print("~" * cont_3 + "\033[0m")
            break
        else:
            a_m = f"Acessando o manual do comando '{resp}'"
            for i in a_m:
                cont_2 += 1
            print("\033[94m" + "~" * cont_2)
            print(a_m)
            print("~" * cont_2 + "\033[0m")
            print(help(resp))


ajuda()
