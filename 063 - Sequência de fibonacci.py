print("-=-" * 8)
print("Sequência de Fibonacci")
print("-=-" * 8)

termos = int(input("Quantos termos você quer mostar = "))

termo_1 = 0
termo_2 = 1

print("{} > {}".format(termo_1, termo_2),end='')

cont = 3
while cont <= termos:
    
    termo_3 = termo_1 + termo_2

    print(" > {}".format(termo_3),end='')
   
    termo_1 = termo_2
    termo_2 = termo_3

    cont += 1

print(" > FIM")
