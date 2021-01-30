f = open("date.in")
s = f.readline()
t = f.readline()
f.close()

lmax = [[0]*len(s) for i in range (len(t))]

for i in range(len(s)):
    for j in range(len(t)):
        if i == 0 or j == 0:
            lmax[i][j] = 0
        else:
            if s[i-1] == t[j-1]:
                lmax[i][j] = lmax[i-1][j-1] + 1
            else:
                lmax[i][j] = max(lmax[i][j-1], lmax[i-1][j])
for i in range (len(s)):
    print (*lmax[i])

sol = []
poz = lmax[len(s)-1][len(t)-1]
print (poz)
i = len(s)-1
j = len(t)-1
while i != 0 or j != 0:
    if lmax[i-1][j] == lmax[i][j]:
        i -= 1
    elif lmax[i][j] == lmax[i][j-1]:
        j -= 1
    else:
        sol.append(t[j-1])
        i -= 1
        j -= 1
print (sol[::-1])