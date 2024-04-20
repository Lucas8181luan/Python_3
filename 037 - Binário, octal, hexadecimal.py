numero = int(input("Digite um número inteiro = "))

bases = int(input('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
Sua opção = '''))

if bases == 1:
    print("{} Convertido para BINÁRIO é igual a = {}".format(numero, bin(numero)[2:]))

elif bases == 2:
    print("{} Convertido para OCTAL é igual a = {}".format(numero, oct(numero)[2:]))

elif bases == 3:
    print("{} Convertido para HEXADECIMAL é igual a = {}".format(numero, hex(numero)[2:]))

else:
    print("Opção inválida, TENTE NOVAMENTE!")

