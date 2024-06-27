def leiaInt():
    while True:
        print("=" * 40)
        try:
            valor = int(input("Digite um número = "))
            if isinstance(valor, int):
                print(f"Você acabou de digitar o número {valor}")
                break
        except ValueError:
            print("\033[91m" + "ERRO! Digite um número inteiro válido" + "\033[0m")


leiaInt()
