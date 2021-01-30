from fractions import Fraction
f = open ("date.in")
G = int(f.readline())
obiecte = []
for linie in f:
    obiecte.append((int(linie.split()[0]), int(linie.split()[1])))
    # greutate, valoare
f.close()

def cmp(t):
    return t[0]/t[1]

obiecte.sort( key = cmp, reverse = True)
profit = 0
#mesaj_1 = "Greutate:\n" + str(G) + " = "
#mesaj_2 = "Valoare obiecte: \n"

for x in obiecte:
    if G >= x[1]:
        #mesaj_1 += str(x[0])
        #mesaj_2 += str(x[1])
        G -= x[1]
        profit += x[0]
        #if G:
        #    mesaj_1 += " + "
        #    mesaj_2 += " + "
        #else:
         # #  mesaj_1 += "\n\n"
         #   mesaj_2 += " = " + str(profit)
    else:
        p = G / x[1]
        #mesaj_1 += "(" + str(Fraction(p).limit_denominator()) + ")" + " * " + str(x[0]) + "\n\n"
        #mesaj_2 += "(" + str(Fraction(p).limit_denominator()) + ")" + " * " + str(x[1])
        G -= p*x[1]
        profit += p*x[0]
        #mesaj_2 += " = " + str(profit)

print (int(profit))