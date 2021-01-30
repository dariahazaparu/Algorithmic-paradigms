f = open ("date.in")
proiecte = []
for linie in f:
    proiecte.append((linie.split()[0], (int(linie.split()[1]), int(linie.split()[2])), int(linie.split()[3])))
proiecte.sort (key = lambda t: t[1][1])
print (*proiecte, sep = '\n')
f.close()
cmax = [0] * (len(proiecte) +1)
ult = [0] * (len(proiecte) +1)

for i in range (len(proiecte)+1):
    for j in range (i):
        if proiecte[i-1][1][0] >= proiecte[j][1][1]:
            ult[i] += 1

for i in range (len(proiecte)+1):
    if i == 0:
        cmax[i] = 0
    else:
        cmax[i] = max(cmax[i-1], proiecte[i-1][2] + cmax[ult[i]])
print (*cmax)
solutie = []
print ("profit maxim: " + str(cmax[len(proiecte)]))
x = len(proiecte)
while x != 0:
    if cmax [x] != cmax[x-1]:
        solutie.append(proiecte[x-1][0])
        x = ult[x]
    else:
        x -= 1

print (solutie[::-1])

