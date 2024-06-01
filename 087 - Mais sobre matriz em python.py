par = []

lista = [[0, 0, 0], [0, 0 , 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c]= int(input(f"Digite um valor para [{l}, {c}] = "))

print("-=" *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{lista[l][c]:^5}]",end=" ")
    print()

print("-=" * 30)

for i in lista[0]:
    n0 = i
    if i % 2 == 0:
        par.append(i)
for i in lista[1]:
    n1 = i
    if i % 2 == 0:
        par.append(i)
for i in lista[2]:
    n2 = i
    if i % 2 == 0:
        par.append(i)     

print(f"A soma dos valores pares é = {sum(par)}")
print(f"A soma dos valores da terceira coluna é = {n0 + n1 + n2}")
print(f"O maior valor da segunda linha é = {max(lista[1])}")
