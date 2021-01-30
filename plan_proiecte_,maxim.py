f = open("date.in")
lista = []
for x in f:
    p = x.split()
    lista.append((p[0], int (p[1]), float(p[2])))
    # nume proiect, termen imita, profit
f.close()
lista.sort( key = lambda t: t[2], reverse = True)
termen_maxim = max (lista, key = lambda t: t[1])[1]
d = { x: None for x in range (1, termen_maxim + 1)}
profit = 0

for p in lista:
    for z in range (p[1], 0, -1):
        if d[z] == None:
            d[z] = p
            profit += p[2]
            break
for z in d:
    if d[z] != None:
        print("Ziua " + str(z) + ": " + str(d[z][0]))
print (profit)