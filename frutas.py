v = []
while len(v) < 5:
    x = str(input("Escreva uma fruta: "))
    if x in v:
        print("Nao pode escrever essa fruta.")
    else:
        v.append(x)

v.sort()
print(v)

