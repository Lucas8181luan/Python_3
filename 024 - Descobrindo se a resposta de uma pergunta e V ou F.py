# COMO DESCOBRIR SE UMA RESPOSTA E VERDADEIRA OU FALSA

# Entrada, uma pergunta qual quer
cidade = str(input("Em que cidade você nasceu = ")).strip() # Tira os espaços

# Criando a resposta em maiusculo
resposta = "BRASILIA" 

print(cidade[:8].upper() == resposta)

# upper() e tudo maiusculo