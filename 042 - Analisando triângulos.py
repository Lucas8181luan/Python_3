primeiro = int(input("Primeiro segmento = "))
segundo = int(input("Segundo segmento = "))
terceiro = int(input("Terceiro segmento = "))

if primeiro < segundo + terceiro and segundo < terceiro + primeiro and terceiro < primeiro + segundo:
    print("Os segmentos podem formar um TRIÂNGULO")
    if primeiro == segundo and segundo == terceiro:
        print("EQUILÁTERO!")
    elif primeiro != segundo and segundo != terceiro and terceiro != primeiro:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Os segmentos acima NÃO formar um TRIÂNGULO")
