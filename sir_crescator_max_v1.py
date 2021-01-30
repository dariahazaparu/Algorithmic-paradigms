f = open("date.in")
sir = [int (x) for x in f.readline().split()]
f.close()

lmax = [1] * len(sir)
succ = [-1] * len(sir)

for x in range(len(sir), -1, -1):
    for y in range (x+1, len(sir)):

        if sir[x] <= sir[y] and 1 + lmax[y] > lmax[x]:
            lmax[x] = 1 + lmax[y]
            succ[x] = y
print (lmax)
print (succ)
print (max(lmax))

poz = 0
sol = []
for x in range(len(sir)):
    if lmax[poz] < lmax[x]:
        poz = x
while poz != -1:
    sol.append(sir[poz])
    poz = succ[poz]

print (*sol)