print("-=-" * 8)
print("10 TERMOS DE UMA PA")
print("-=-" * 8)

primeiro_termo = int(input("Primeiro termo = "))

razao = int(input("Razão = "))

decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print("{}".format(c))
print("ACABOU")
