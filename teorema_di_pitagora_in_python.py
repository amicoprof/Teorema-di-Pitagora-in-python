cateto_1 = float(input("Inserisci il valore del primo cateto:"))
cateto_2 = float(input("Inserisci il valore del secondo cateto:"))

from math import sqrt

ipotenusa = sqrt( cateto_1**2 + cateto_2**2)
print("Ipotenusa =", ipotenusa)