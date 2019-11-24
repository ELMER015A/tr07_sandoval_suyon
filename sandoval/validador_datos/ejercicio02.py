# validar la velocidad de un automovil mayor a 30 m/s .
import os
velocidad=int(os.sys.argv[1])
velocidad_invalidad= (velocidad<50)

while(velocidad_invalidad==True):
    velocidad=int("ingrese velocidad:")
    velocidad_invalidad= (velocidad>50)

# fin_while

print("fin del bucle")
