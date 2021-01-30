def bkt_regine(k):
    global x, n
    for v in range (1, n+1):
        x[k] = v
        for i in range (k):
            if x[k] == x[i] or abs(x[k] - x[i]) == abs (k - i):
                break
        else:
            if k == n-1:
                print (*x[:k+1])
            else:
                bkt_regine(k+1)


n = 5
x = [0] * n
bkt_regine(0)