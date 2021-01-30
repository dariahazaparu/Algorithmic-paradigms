f = open("date.in")
G = int(f.readline())
obiecte = []
for linie in f:
    obiecte.append((int(linie.split()[0]), int(linie.split()[1])))

solutie =[]
def pivot(x):
    if len(x) <= 5:
        return sorted(x)[len(x)//2]
    subliste = [sorted(x[i:i+5], key = lambda t: t[0]/t[1]) for i in range (0, len(x), +5) ]
    mediane = [sl[len(sl)//2] for sl in subliste]
    return pivot(mediane)

def rucsac( obiecte, G, solutie):
    p = pivot(obiecte)

    L = [x for x in obiecte if x[1]/x[0] < p[1]/p[0]]
    E = [x for x in obiecte if x[1]/x[0] == p[1]/p[0]]
    H = [x for x in obiecte if x[1]/x[0] > p[1]/p[0]]

    if sum(x[0] for x in H) > G:
        return rucsac(H, G, solutie)
    else:
        solutie.extend([*x, 1] for x in H)
        G -= sum([x[0] for x in H])
        i = 0
        while G > 0 and i < len(E):
            if E[i][0] <= G:
                solutie.append((*E[i], 1))
                G -= E[i][0]
                i += 1
            else:
                solutie.append((*E[i], (G/E[i][0])/100*100))
                G = 0
        if G > 0:
            return rucsac(L, G, solutie)


rucsac(obiecte, G, solutie)
print (*solutie)
print (sum([x[1]* x[2] for x in solutie]))