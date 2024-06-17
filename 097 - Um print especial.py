def escreva():
    lista = ["Gustavo Guanabara", "Curso de Python no Youtube", "CeV"]
    for i in lista:
        cont = 0
        a = i
        for v in a:
            cont += 1
        v_a = cont
        print("~" * v_a)
        print(a)
        print("~" * v_a)


escreva()
