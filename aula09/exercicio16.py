from random import randint
n, l = [], []
for y in range(5):
    for x in range(5):
        l.append(randint(1,100))
    m.append(l)
    l = []
print(n)
soma = 0
qtd = 0
for y in range(0,5,2):
    for x in range(5):
        soma = soma + n[y][x]
        qtd = qtd + 1

    media = soma / qtd
    print(f"{media=}")
