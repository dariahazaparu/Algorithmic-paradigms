def bkt_1(k):
    global x, n
    for v in range (1, n-k+2):
        x[k] = v
        scrt = sum (x[:k+1])
        if scrt <= n:
            if scrt == n:
                print (*x[:k+1])
            else:
                if k < n-1:
                    bkt_1(k+1)

def bkt_2(k):
    global x, n
    for v in range (1 if k == 0 else x[k-1], n-k+2):
        x[k] = v
        scrt = sum (x[:k+1])
        if scrt <= n:
            if scrt == n:
                print (*x[:k+1])
            else:
                if k < n-1:
                    bkt_2(k+1)

def bkt_3(k):
    global x, n
    for v in range (1 if k == 0 else x[k-1]+1, n-k+2):
        x[k] = v
        scrt = sum (x[:k+1])
        if scrt <= n:
            if scrt == n:
                print (*x[:k+1])
            else:
                if k < n-1:
                    bkt_3(k+1)

n = 4
x = [0]*n
bkt_3(0)