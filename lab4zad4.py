import numpy as np
a = input("Podaj liczbe:")
a =int(a)
print(a)
b = input("Podaj ilość kolejnych potęg do wygenerowania:")
b = int(b)
c = int(a**b)
d = int(b*(a**2))
tab = np.logspace(a,a**b,num=b+1)
print(tab)

