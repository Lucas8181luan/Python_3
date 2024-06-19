import random 
import time
v = [6, 3, 2, 1, 0]
n = []

def descobre_o_maior_numero():
    cont_clear = 0
    while True:
        for nv in v:
            while True:
                s = random.randint(1, 10)
                if s == s in n:
                    pass
                else:
                    n.append(s)
                if len(n) == nv:
                    break
            print("=" * 50)
            print("Analisando os valores passados...")
            time.sleep(1)
            for i in n:
                print(f"{i} ",end="")
            print(f"Foram informados {len(n)} valores ao todo.")
            print(f"O maior valor informado foi {max(n)}.")
            n.clear()
            cont_clear += 1
            if cont_clear == 4:
                print("=" * 50)
                print("Analisando os valores passados...")
                time.sleep(1)
                print(f"Foram informados 0 valores ao todo.")
                print(f"O maior valor informado foi 0.")
                print("=" * 50)
                print("FIM!")


descobre_o_maior_numero()
