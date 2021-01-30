f = open("date.in")
sir = [int(x) for x in f.readline().split()]
f.close()

lmax = [1] * len(sir)
pred = [-1] * len(sir)

for x in range (1, len(sir)):
    for y in range(x):
        if sir[x] > sir[y] and lmax[y] + 1 > lmax[x]:
            lmax [x] = 1 + lmax[y]
            pred[x] = y
print (lmax)
print(pred)
print (max(lmax))

m = max(lmax)
poz = 0
sol = []
for x in range(len(sir)):
    if lmax[x] > lmax[poz]:
        poz = x
while poz != -1:
    sol.append(sir[poz])
    poz = pred[poz]
print(*sol[::-1])