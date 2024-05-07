import time

primeiro = int(input("Primeiro valor = "))
segundo = int(input("Segundo valor = "))

sair_do_programa = False

while not sair_do_programa:
    
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input("Qual sua opção = "))

    if opção == 1:
        somar = primeiro + segundo
        print("A soma entre {} + {} é = {}".format(primeiro, segundo, somar))
        print("-=-" * 8)
    elif opção == 2:
        multiplicar = primeiro * segundo
        print("O resultado de {} x {} é = {}".format(primeiro, segundo, multiplicar))
        print("-=-" * 8)
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print("Entre {} e {} o maior valor é = {}".format(primeiro, segundo, maior))
        print("-=-" * 8)
    elif opção == 4:
        print("Informe novos números:")
        primeiro = int(input("Primeiro valor = "))
        segundo = int(input("Segundo valor = "))
    elif opção == 5:
        time.sleep(1)
        print("Finalizando...")
        time.sleep(1)
        sair_do_programa = True
    else:
        print("Escolha uma opção valida!")
        print("-=-" * 8)
print("Fim do programa! Volte sempre!")
