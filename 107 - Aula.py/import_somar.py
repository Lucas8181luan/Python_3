def metade(valor):
    somar = valor / 2 
    return somar


def dobro(valor): 
    somar = valor * 2
    return somar


def aumentar(valor, taxa):
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor + somar_porcentagem
    return somar_porcentagem_final


def diminuir(valor, taxa):
    taxa_ = taxa / 100
    somar_porcentagem = valor * taxa_
    somar_porcentagem_final = valor - somar_porcentagem
    return somar_porcentagem_final
