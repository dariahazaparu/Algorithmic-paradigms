def pivot_mediana(A):
    if len(A) <=1 :
        return sorted(A)[len (A)//2]
    subliste = [sorted(A[i:i+5]) for i in range (0, len (A), 5)]
    mediane = [sl[len(sl)//2] for sl in subliste]
    return pivot_mediana(mediane)

#import random
def quickselect(A, k):
    pivot = pivot_mediana(A)
    print(pivot)
    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    G = [x for x in A if x > pivot]
    if k <= len (L):
        return quickselect(L, k)
    elif k <= len(L) + len(E):
        return E[0]
    else:
        return quickselect(G, k-len(E)-len(L))


L = [1, 2, 8, 4, 5, 6, 7, 3, 9]
ls = quickselect(L, 5)
print (ls)