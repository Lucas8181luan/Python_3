tupla_com_entrada = (int(input("Digite um número = ")),
                     int(input("Digite outro número = ")),
                     int(input("Digite mais um número = ")),
                     int(input("Digite o último número = ")))

print(f"Você digitou od valores = {tupla_com_entrada}")
print(f"O valor 9 apareceu {tupla_com_entrada.count(9)} vezes")
if 3 in tupla_com_entrada:
   print(f"O valor 3 apareceu na {tupla_com_entrada.index(3) + 1}º posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")
print("Os valores pares digitados foram = ", end=" ")
for n in tupla_com_entrada:
    if n % 2 == 0:
        print(n, end=" ")
