print("=" * 20)
print("       BANCO CEV       ")
print("=" * 20)

sacar = int(input("Quer valor você quer sacar = R$"))

total = sacar

cedulas = 50

cont_cedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        cont_cedulas+= 1
    else:
        if cont_cedulas > 0:
            print(f"Total de {cont_cedulas} cédulas de R${cedulas}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        cont_cedulas = 0
        if total == 0:
            break
