f = open ("date.in")
triunghi = [x.split() for x in f.readlines()]

n = len(triunghi)

smax = [[0]*i for i in range (1, n+1)]
for i in range(0, n):
    for j in range (0, i):
        if i == n-1:
            smax[i][j] = triunghi[i][j]
        else:
            smax[i][j] = triunghi[i][j] + max(smax[i+1][j], smax[i+1][j+1])

print (smax[0][0])
