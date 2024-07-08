def moeda(valor):
    """
    Formata o valor numérico para uma string no formato de moeda brasileira.

    Args:
    - valor (float): O valor numérico a ser formatado.

    Returns:
    - str: Uma string formatada como moeda brasileira (R$ X.XX.XX,XX).

    Exemplo:
    >>> moeda(1000.50)
    'R$ 1.000,50'
    """
    import locale
    locale.setlocale(locale.LC_ALL,"pt_BR.utf-8")
    return locale.currency(valor, grouping=True, symbol="R$")


def metade(valor, show=False):
    """
    Calcula a metade de um valor.

    Args:
    - valor (float): O valor a ser dividido pela metade.
    - show (bool, optional): Se True, retorna o resultado formatado como moeda brasileira.

    Returns:
    - float or str: Se show=True, retorna a metade formatada como moeda brasileira. Caso contrário, retorna o valor numérico da metade.

    Exemplo:
    >>> metade(100, show=True)
    'R$ 50,00'
    """
    somar = valor / 2 
    if show == True:
        return moeda(somar)
    else:
        return somar


def dobro(valor, show=False): 
    """
    Calcula o dobro de um valor.

    Args:
    - valor (float): O valor a ser multiplicado por dois.
    - show (bool, optional): Se True, retorna o resultado formatado como moeda brasileira.

    Returns:
    - float or str: Se show=True, retorna o dobro formatado como moeda brasileira. Caso contrário, retorna o valor numérico do dobro.

    Exemplo:
    >>> dobro(50, show=True)
    'R$ 100,00'
    """
    somar = valor * 2
    if show == True:
        return moeda(somar)
    else:
        return somar


def aumentar(valor, taxa, show=False):
    """
    Calcula o aumento percentual de um valor.

    Args:
    - valor (float): O valor base ao qual o aumento será aplicado.
    - taxa (float): A taxa de aumento em percentagem.
    - show (bool, optional): Se True, retorna o resultado do aumento formatado como moeda brasileira.

    Returns:
    - float or str: Se show=True, retorna o valor aumentado formatado como moeda brasileira. Caso contrário, retorna o valor numérico aumentado.

    Exemplo:
    >>> aumentar(100, 10, show=True)
    'R$ 110,00'
    """
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor + somar_porcentagem
    if show == True:
        return moeda(somar_porcentagem_final)
    else:
        return somar_porcentagem_final


def diminuir(valor, taxa, show=False):
    """
    Calcula a redução percentual de um valor.

    Args:
    - valor (float): O valor base ao qual a redução será aplicada.
    - taxa (float): A taxa de redução em percentagem.
    - show (bool, optional): Se True, retorna o resultado da redução formatado como moeda brasileira.

    Returns:
    - float or str: Se show=True, retorna o valor reduzido formatado como moeda brasileira. Caso contrário, retorna o valor numérico reduzido.

    Exemplo:
    >>> diminuir(100, 10, show=True)
    'R$ 90,00'
    """
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor - somar_porcentagem
    if show == True:
        return moeda(somar_porcentagem_final)
    else:
        return somar_porcentagem_final