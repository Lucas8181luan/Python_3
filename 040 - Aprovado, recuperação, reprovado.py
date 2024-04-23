nota_1 = float(input("Digite a 1° nota = "))
nota_2 = float(input("Digite a 2° nota = "))

soma = (nota_1 + nota_2) / 2

print("Tirando {:.1f} e {:.1f}, a média do aluno é = {:.1f}".format(nota_1, nota_2, soma))

print("-=-" * 12)

if soma >= 7:
    print("O aluno está APROVADO.")
elif soma >= 5 and soma < 7:
    print("O aluno está em RECUPERAÇÃO.")
else:
    print("O aluno está REPROVADO")

print("-=-" * 12)
