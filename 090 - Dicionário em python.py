alunos = {}

nome = str(input("Nome = "))
media = float(input(f"Média de {nome} = "))
alunos["nome"] = nome
alunos["nota"] = media

if media < 7:
    alunos["situação"] = "recuperação"
if media < 5:
    alunos["situação"] = "reprovado"
if media >= 7:
    alunos["situação"] = "aprovado"

print("=" * 40)

print(f" - nome é igual a {alunos["nome"]}")
print(f" - média é igual a {alunos["nota"]}")
print(f" - situação é igual a = {alunos["situação"]}")
