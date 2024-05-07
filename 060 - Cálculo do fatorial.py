from math import factorial

número = int(input('''Digite um número para
calcular seu fatorial: '''))

soma = factorial(número)

print("O fatorial de {} é = {}".format(número, soma))
