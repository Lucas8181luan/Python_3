def titulo():
    print("Controle de Terrenos")

def linha():
    print("=" * 20)

def soma_area():
    l = float(input("LARGURA (m) = "))
    c = float(input("COMPRIMENTO (m) = "))
    soma = l * c
    print(f"A área de um terreno {l:.1f}x{c:.1f} é de {soma:.1f}m².")


titulo()
linha()
soma_area()
