def numero_formatado(valor):
    import locale
    locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
    return locale.currency(valor, grouping=True, symbol="R$")


def metade(valor):
    somar = valor / 2 
    return numero_formatado(somar)


def dobro(valor): 
    somar = valor * 2
    return numero_formatado(somar)


def aumentar(valor, taxa):
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor + somar_porcentagem
    return numero_formatado(somar_porcentagem_final)


def diminuir(valor, taxa):
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor - somar_porcentagem
    return numero_formatado(somar_porcentagem_final)
