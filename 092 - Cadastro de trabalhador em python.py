import datetime

tb = {}
tb["Nome"] = str(input("Nome = "))
idade = int(input("Ano de Nascimento = "))
ano_atual = datetime.date.today().year
soma_idade = idade - ano_atual
tb["Idade"] = soma_idade
carteira = int(input("Carteira de Trabalho (0 não tem) = "))
tb["Ctps"] = carteira
if carteira == 0:
    print("=" * 40)
    print(f''' - Nome tem valor = {tb["Nome"]}
 - Idade tem o valor = {tb["Idade"]}
 - Ctps tem o valor = {tb["Ctps"]}''')
if carteira > 0:
    tb["Contratação"] = int(input("Ano de Contratação = "))
    tb["Salário"] = float(input("Salário = R$"))
    ap = 65
    apst = ap - (ano_atual - tb["Contratação"])
    tb["Aposentadoria"] = apst
    print("=" * 40)
    print(f''' - Nome tem valor = {tb["Nome"]}
 - Idade tem o valor = {tb["Idade"]}
 - Ctps tem o valor = {tb["Ctps"]}
 - Contratação tem o valor = {tb["Contratação"]}
 - Salário tem o valor = {tb["Salário"]}
 - Aposentadoria tem o valor = {tb["Aposentadoria"]}''')
print("="  * 40)
