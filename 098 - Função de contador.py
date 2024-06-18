import time
inicio_ = []
fim_ = []
valores = []

def cont1():
    print("=" * 40)
    print("Contagem de 1 até 10 de 1 em 1")
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in n:
        print(f"{i} ",end='', flush=True)
        time.sleep(0.5)
    print("FIM!")

def cont2():
    print("=" * 40)
    print("Contagem de 10 até 0 de 2 em 2")
    n = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
    for i in reversed(n):
        if i % 2 == 0:
            print(f"{i} ",end='', flush=True)
            time.sleep(0.5)
    print("FIM!")

def cont_usuario():
    print("=" * 40)
    print("Agora é sua vez de personalizar a contagem!")
    início = int(input("Início = "))
    fim = int(input("Fim = "))
    passo = int(input("Passo = "))
    print("=" * 40)
    passo_p = abs(passo)
    if passo_p == 0:
        passo_p = 1
    print(f"Contagem de {início} até {fim} de {passo_p} em {passo_p}")
    if início >= 0:
        for i in range(início + 1):
            inicio_.insert(0, i)
    else:
        for i in range(início, 1):
            inicio_.index(0, i)
    if fim >= 0:
        for i in range(fim + 1):
            fim_.insert(0, i)
    else:
        for i in range(fim, 1):
            fim_.insert(0, i)
    for i in inicio_:
        valores.append(i)
    for i in fim_:
        valores.append(i - 1)
    for i in range(0, len(valores), passo_p):
        print(f"{valores[i]} ",end='',flush=True)
        time.sleep(0.5)
    print("FIM!")


cont1()
cont2()
cont_usuario()
