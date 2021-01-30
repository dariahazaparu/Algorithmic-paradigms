def afisare_timpi(lista):
    lungime = len(lista)
    suma = 0
    suma2 = 0
    for i in range (lungime):
        suma += lista[i][1]
        print(f"{lista[i][0]}\t{lista[i][1]}\t{suma}")
        suma2 += suma
    print (suma2/lungime)



f = open("date.in")
n = int(f.readline())
timpi_initiali = [int (x) for x in f.readline().split()]
f.close()
ordine = []
for i in range(n):
    ordine.append((i+1, timpi_initiali[i]))
afisare_timpi(ordine)
ordine_new = sorted(ordine, key = lambda t: t[1])
afisare_timpi(ordine_new)
