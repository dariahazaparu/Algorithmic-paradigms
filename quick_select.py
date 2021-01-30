import random
def quickselect(A, k, f_pivot = random.choice):
    pivot = f_pivot(A)
    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    G = [x for x in A if x > pivot]
    if k <= len (L):
        return quickselect(L, k, f_pivot)
    elif k <= len(L) + len(E):
        return E[0]
    else:
        return quickselect(G, k-len(E)-len(L), f_pivot)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls = quickselect(L, 5)
print (ls)