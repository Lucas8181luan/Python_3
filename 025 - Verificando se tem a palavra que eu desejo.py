# VERIFICANDO SE TEM A PALAVRA QUE EU DESEJO

# Entrada da pergunta
pergunta = str(input("Informe seu nome completo = ")).strip()


# A palavra desejada
palavra_desejada = "SILVA" in pergunta.upper()

print("Seu nome tem Silva = {}".format(palavra_desejada))

# Pode usar upper() ou lower()