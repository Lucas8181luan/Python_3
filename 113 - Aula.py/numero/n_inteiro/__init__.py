def numero_inteiro_float():
    while True:
        try:
            usuario = int(input("Digite um Inteiro = "))
        except ValueError:
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[0m")
        else:
            break
    while True:
        try:
            usuario_ = float(input("Digite um Real = "))
        except ValueError:
            print("\033[31mERRO: por favor, digite um número real válido.\033[0m")
        else:
            break
    print(f"O valor inteiro digitado foi {usuario} e o real foi {usuario_}")
