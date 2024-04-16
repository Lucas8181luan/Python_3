# COMO DESCOBRIR A POSIÇÃO DE UMA LETRA 

# Entrada, da frase
frase = str(input("Digite uma frase = ")).upper().strip()

# Rastreando uma letra
quantas_vezes = frase.count("E")
primeira_vez = frase.find("E")
ultima_vez = frase.rfind("E")
# Posso colocar +1 para que a posição fique da formar como lemos

print("A letra E apareceu {} vezes na frase\nA primeira letra E apareceu na posição {}\nA última letra E apareceu na posição {}".format(quantas_vezes, primeira_vez, ultima_vez))
