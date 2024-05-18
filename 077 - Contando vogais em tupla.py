palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")


for n in palavras:
    print(f"\nNa palavra {n.upper()} temos = ",end=" ")
    for letra in n:
        if letra.upper() in "AÁÂEÉIOU":
            print(letra,end=" ")

