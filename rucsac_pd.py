f = open("date.in")
G = int(f.readline())
obiecte = []
for linie in f:
    obiecte.append((int(linie.split()[0]), int(linie.split()[1])))
print (*obiecte)
f.close()
cmax = [[0]*(G+1) for i in range (len(obiecte)+1)]


for i in range(1, len(obiecte)+1):
    for j in range(1, G+1):
        if obiecte[i-1][0] > j:
            cmax[i][j] = cmax[i-1][j]
        else:
            cmax[i][j] = max (cmax[i-1][j], obiecte[i-1][1] + cmax[i-1][j-obiecte[i-1][0]])

print (cmax[len(obiecte)][G])

i = len(obiecte)
j = G
sol = []
while i != 0 and j != 0:
    if cmax[i][j] == cmax[i-1][j-1]:
        i -= 1
        j -= 1
    elif cmax[i][j] == cmax[i-1][j]:
        i -= 1
    elif cmax[i][j] == cmax[i][j-1]:
        j -= 1
    else:
        sol.append(obiecte[i-1])
        j -= obiecte[i-1][0]
        i -= 1
print (sol)