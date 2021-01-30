f = open ("date.in")
lista = []

for x in f:
    linie = x.replace("-", " ", 1)
    linie_new = linie.split(" ", 2)
    lista.append (tuple(linie_new))
spectacole = sorted(lista, key = lambda t: t[1])
f.close()
ora_final = spectacole[0][1]
print (*spectacole[0], end="")
lungime = len(spectacole)

for i in range (1, lungime):
    if spectacole[i][0] > ora_final:
        print (*spectacole[i], end="")
        ora_final = spectacole[i][1]
