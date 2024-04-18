# COMO SABER SE O ANO E BISSEXTO, E QUAL E O ANO DO PC

# Para descobrir a data do PC
import datetime

ano = int(input("Que ano quer analisar? Coloque 0 para nalisar o ano atual = "))

soma = ano % 4 
soma_1 = ano % 100
soma_2 = ano % 400

# Data do PC
if ano == 0:
   ano = datetime.date.today().year

if soma == 0 and soma_1 != 0 or soma_2 == 0:
    print("O ano {} é BISSEXTO".format(ano))
else:
    print("O ano {} NÃO e BISSEXTO".format(ano))
