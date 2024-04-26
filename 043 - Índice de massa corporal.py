peso = float(input("Qual seu peso (kg) = "))

altura = float(input("Qual a sua altura (m) = "))

soma = peso / (altura ** 2)

print("O IMC dessa pessoa é de {:.1f}".format(soma))

if soma >= 18.5 and soma < 25:
    print("PARABÉNS, você eatá na faixa de PESO NORMAL")
elif soma >= 25 and soma < 30:
    print("Você está com SOBREPESO!")
elif soma < 18.5:
    print("Você está ABAIXO DO PESO normal!")
elif soma >= 30 and soma < 40:
    print("Você está em OBESIDADE!")
elif soma >= 40:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")
