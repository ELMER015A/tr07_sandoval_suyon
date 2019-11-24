# validad la altura de de una manzana de un arbol
import os
altura=0.0
altura_invalidad=True

while (altura_invalidad):
    altura=float(os.sys.argv[1])
    altura_invalidad=(altura<20 or altura>50)

print("fin del bucle")
