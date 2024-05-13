import random

print("-=-" * 8)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=-" * 8)

cont = 0

while True:
    usuario = int(input("Digite um valor = "))

    p_ou_i = str(input("Par ou ímpar [P/I] = ")).upper().strip()[0]

    pc_resposta = random.randint(0, 10)

    soma = usuario + pc_resposta

    if soma % 2 == 0 and p_ou_i in "Pp":
        print("-=-" * 8)
        
        print(f"Você jogou {usuario} e o computador {pc_resposta}. Total de {soma} DEU PAR")

        print("-=-" * 8)

        print("WIN!")
        print("Vamos jogar novamente...")
        print("-=-" * 8)


        cont += 1

    elif soma % 2 == 0 and p_ou_i in "Ii":
        print("-=-" * 8)
        
        print(f"Você jogou {usuario} e o computador {pc_resposta}. Total de {soma} DEU PAR")

        print("-=-" * 8)

        print("Você PERDEU")

        break

    elif soma % 2 != 0 and p_ou_i in "Ii":
        print("-=-" * 8)
                
        print(f"Você jogou {usuario} e o computador {pc_resposta}. Total de {soma} DEU IMPAR")

        print("-=-" * 8)

        print("WIN!")
        print("Vamos jogar novamente...")
        print("-=-" * 8)

        cont += 1
            
    elif soma % 2 != 0 and p_ou_i in "Pp":
        print("-=-" * 8)
                
        print(f"Você jogou {usuario} e o computador {pc_resposta}. Total de {soma} DEU IMPAR")

        print("-=-" * 8)

        print("Você PERDEU")

        break
    
    elif p_ou_i != "PpIi":
        print("Escolha PAR ou ÍMPAR")
        print("-=-" * 8)

print(f"GAMER OVER! Você venceu {cont} vezes")
