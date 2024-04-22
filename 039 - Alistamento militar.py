import datetime

ano_de_nascimento = int(input("Ano de nascimento = "))

genero = input("Seu sexo e MASCULINO (sim) ou (não) = ")

atual = datetime.date.today().year

soma_idade = atual - ano_de_nascimento

print("-=-" * 12)
print("Quam nasceu em {} tem {} anos em {}.".format(ano_de_nascimento, soma_idade, atual))
print("-=-" * 12)

if genero == "não" or "nao" or "Não" or "NÃO":
    print("alistamento para MULHERES não e obrigatório")
    print("-=-" * 12)
elif soma_idade == 18:
    print("Você tem que alistar IMEDIATAMENTE!")
elif soma_idade < 18:
    faltam = 18 - soma_idade
    print("Você ainda devera se alistar em {} anos".format(faltam))
    ano = atual + faltam
    print("-=-" * 12)
    print("Seu alistamento sera no ano de {}".format(ano))
else:
    passou = soma_idade - 18
    print("Você já passou do prazo de alistamento há {} anos".format(passou))
    ano = passou - atual
    print("-=-" * 12)
    print("Você deveria te se alistado no ano de {}".format(ano))
