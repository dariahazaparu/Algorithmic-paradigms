def interclasare(lst, ldr):
    i=j=0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mijloc = len(lista)//2
        lst = mergesort (lista[:mijloc])
        ldr = mergesort (lista[mijloc:])
        return interclasare (lst, ldr)

lista = [ 5, 2, 10, 8, 5, 4, 1]
print (mergesort(lista))