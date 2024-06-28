def notas(*num, show=False):
    """
    Calcula estatísticas básicas (total de números, maior valor, menor valor e média) 
    a partir de uma lista de números e exibe essas estatísticas em um dicionário.
    
    Parâmetros:
    *num (float): Uma sequência de números para os quais as estatísticas serão calculadas.
    show (bool, opcional): Se True, adiciona a situação da média (RUIM, RAZOÁVEL ou BOA) ao dicionário.
                           Default é False.
    
    Retorna:
    None: A função imprime o dicionário contendo as estatísticas calculadas.
    """
    dics = {}
    cont = soma = 0
    for i in num:
        cont += 1
        soma += i
    dics["total"] = cont
    maior = max(num)
    dics["maior"] = maior
    menor = min(num)
    dics["menor"] = menor
    média = soma / cont
    dics["média"] = média
    if show == True:
        if média < 5:
            dics["situação"] = "RUIM"
        if média >= 5 and média < 7:
            dics["situação"] = "RAZOÁVEL"
        if média >= 7:
            dics["situação"] = "BOA"
    print("=" * 70)
    print(dics)
    print("=" * 70)


help(notas)
