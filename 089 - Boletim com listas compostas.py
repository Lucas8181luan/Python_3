import time
alunos = []
lista = []
cont = 0
while True:
    nome = str(input("Nome = "))
    nota_1 = float(input("Nota 1 = "))
    nota_2 = float(input("Nota 2 = "))
    lista.append(nome)
    lista.append(nota_1)
    lista.append(nota_2)
    alunos.append(lista[:])
    lista.clear()

    continuar = ' '
    while continuar not in "NS":
        continuar = str(input("Quer continuar [N/S] = ")).strip().upper()[0]
    print("=" * 30)

    if continuar == "N":
        break
print("=" * 30)
print(f"Nº.  NOME / MÉDIA")
print("=" * 30)
for i in alunos:
    soma = i[1] + i[2]
    media = soma / 2
    cont += 1
    print(f"{cont}    {i[0]} = {media:.1f}")
print("=" * 30)

while True:
    mostrar = int(input("Mostrar notas de qual aluno: (999 interrompe) = "))
    mostrar -= 1
 
    if mostrar <= len(alunos) - 1:    
        print(f"Notas de {alunos[mostrar][0]} são = [{alunos[mostrar][1]}, {alunos[mostrar][2]}]")

    if mostrar == 998:
        break

print("FINALIZANDO...")
time.sleep(2)
print("<<<<<  VOLTE SEMPRE  >>>>>")
