# COMO FAZER UM ANALISADOR DE TEXTOS

# strip eliminar os espaços

# Entrada do nome
nome = str(input("Digite seu nome = ")).strip()

# Fazendo a analise
maiusculo = nome.upper()
minusculo = nome.lower()
# Count eliminar os restos dos espaços
quantas_letras = len(nome) - nome.count(" ")
primeiro_nome = nome.find(" ")

print("Seu nome em maiúsculo é = {}".format(maiusculo))
print("Seu nome em minúsculo é = {}".format(minusculo))
print("Seu nome tem ao todo = {} letras".format(quantas_letras))
print("Seu primeiro nome tem = {} letras".format(primeiro_nome))

# Outra forma de fazer
separa_o_nome = nome.split()
quantidades_de_letras = len(separa_o_nome[0])
print("Seu primeiro nome é {} e ele tem {} letras".format(separa_o_nome[0], quantidades_de_letras))
