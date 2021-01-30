def bkt_perm(k):
    global X, n
    for v in range (1, n+1):
        x[k] = v
        if v not in x[:k]:
            if k == n-1:
                print (*x[:k+1])
            else:
                bkt_perm(k+1)

def bkt_aranj(k):
    global x, n, p
    for v in range (1, n+1):
        x[k] = v
        if v not in x[:k]:
            if k == p-1:
                print (*x[:k+1])
            else:
                bkt_aranj(k+1)

def bkt_comb(k):
    global x, n, p
    for v in range (1 if k == 0 else x[k-1]+1, n+1):
        x[k] = v
        if k == p-1:
            print (*x[:k+1])
        else:
            bkt_comb(k+1)

n = 4
p = 3
x = [0] * n
bkt_comb(0)