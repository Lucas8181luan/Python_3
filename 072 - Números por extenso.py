from num2words import num2words

usuario = int(input("Digite um número entre 0 e 20 = "))

while usuario > 20:

    usuario = int(input("Tente novamente. Digite um número entre 0 e 20 = "))
        
numero_extenso = num2words(usuario, lang='pt_BR')

print(f"Você digitou o número {numero_extenso}")

#--------------------------------------------------#
# OUTRA FORMAR

numeros_da_lista = ("zero", "um" , "dois", "três", "quatro", "cinco", "seis", "sete","oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezonove", "vinte")

while True:
    usuario_numero = int(input("Digite um número entre 0 e 20 = "))
    
    if usuario_numero < 20:
        break

    print("Tente novamente .", end=" ")

print(f"Você digitou o número = {numeros_da_lista[usuario_numero]}")
