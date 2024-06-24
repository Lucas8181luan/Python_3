def voto(nascimento):
    from datetime import datetime
    print("=" * 40)
    ano_atual = datetime.now().year
    idade = nascimento - ano_atual
    idade_ = abs(idade)
    if idade_ >= 18 and idade_ < 70:
        return f"Com {idade_} anos: VOTO OBRIGATÓRIO."
    if idade_ > 15 and idade_ < 18:
        return f"Com {idade_} anos: VOTO OPICIONAL."
    if idade_ >= 70:
        return f"Com {idade_} anos: VOTO OPICIONAL."
    if idade_ < 16:
        return f"Com {idade_} anos: NÃO VOTA."   
    

print(voto(nascimento = int(input("Em que ano você nasceu = "))))
