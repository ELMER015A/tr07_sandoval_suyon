# validar la gravedad de la tierra a la gravedad (9.8)
import os
gravedad=float(os.sys.argv[1])
gravedad_invalidad=(gravedad != 9.8)

while(gravedad_invalidad):
    gravedad=float(input("ingrese gravedad:"))
    gravedad_invalidad= (gravedad != 9.8)

# fin while

print("fin del bucle")




