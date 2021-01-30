f = open ("date.in")
lista = []

for x in f:
    linie = x.replace("-", " ", 1)
    linie_new = linie.split(" ", 2)
    lista.append (tuple(linie_new))
lista.sort()
f.close()
print (*lista)
from queue import PriorityQueue

pq = PriorityQueue()
sol = dict()

for i in lista:
    if pq.qsize() == 0:
        pq.put((i[1], 1))
        sol[i[2]] = 1
    else:
        minim = pq.get()
        if minim[0] <= i[0]:
            pq.put((i[1], minim[1]))
            sol[i[2]] = minim[1]
        else:
            pq.put(minim)
            pq.put((i[1], pq.qsize()+1))
            sol[i[2]] = pq.qsize()
print (sol)