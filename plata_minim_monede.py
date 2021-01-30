f = open ("date.in")
s = int (f.readline())
v = [int(x) for x in f.readline().split()]
f.close()

nrmin = [float ("inf")] * (s+1)
nrmin[0] = 0

pred = [-1] * (s+1)

for i in range (1, s+1):
    for m in v:
        if m <= i and nrmin[i-m] +1 < nrmin[i]:
            nrmin[i] = nrmin[i-m] + 1
            pred [i] = m
if pred [s] == -1:
    print ("suma nu a putut fi obtinuta")
else:
    print (f"suma {s} a fost obtinuta din {nrmin[s]} monede:")
    while s!= 0:
        print (pred[s], end=' ')
        s = s - pred[s]
