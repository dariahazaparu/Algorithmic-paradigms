def bkt_nr(k):
    global x, n
    for v in range(1 if k == 0 else 0, 11):
        x[k] = v
        suma = sum(x[:k+1])
        if v not in x[:k]:
            if suma <= n:
                if suma == n:
                    print(*x[:k+1])
                    if 0 not in x[:k+1]:
                        print(*x[:k+1], 0)
                else:
                    if k <= n-1:
                        bkt_nr(k+1)


n = 3
x = [0] * 11
bkt_nr(0)