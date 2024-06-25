def fatorial(n, show=False):
    """
    Calcula o fatorial de um número e opcionalmente mostra os passos.

    Args:
    -> n (int): O número inteiro positivo para o qual calcular o fatorial.
    - show (bool, optional): Se True, mostra os passos do cálculo. Padrão é False.

    Returns:
    -> str: Uma string formatada indicando o cálculo do fatorial e o resultado.

    Exemplo:
    >>> print(calcular_fatorial(5))
    5 x 4 x 3 x 2 x 1 = 120
    >>> print(calcular_fatorial(5, show=True))
    5 x 4 x 3 x 2 x 1 = 120
    """
    print("=" * 40)
    lista = []
    import math
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        lista.append(i)
    if show == True:
        for i in reversed(lista):
            if i != 1:
                print(f"{i} x ",end="")
            else:
                print(f"{i} ",end="")
        return f"= {resultado}"
    else:
        return resultado


print(fatorial(5, True))
