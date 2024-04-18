# COMO DESCOBRIR O MAIOR E O MENOR VALOR

primeiro_n = int(input("Digite o 1° valor = "))
segundo_n = int(input("Digite o 2° valor = "))
terceiro_n = int(input("Digite o 3° valor = "))
#--------------------------------#
# MENOR
menor = primeiro_n

if segundo_n < primeiro_n and segundo_n < terceiro_n:
    menor = segundo_n

if terceiro_n < primeiro_n and terceiro_n < segundo_n:
    menor = terceiro_n
#----------------------------------#
# MAIOR
maior = primeiro_n

if segundo_n > primeiro_n and segundo_n > terceiro_n:
    maior = segundo_n

if terceiro_n > primeiro_n and terceiro_n > segundo_n:
    maior = terceiro_n
#-----------------------------------#

print("=" * 12)
print("O menor número é = {}".format(menor))
print("O maior número é = {}".format(maior))
print("=" * 12)
