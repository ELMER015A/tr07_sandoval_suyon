# validar la ganancia de un bodega menor  a 500 mensual
import os
ganancia=0.0
ganancia_invalidad=True

while (ganancia_invalidad):
    ganancia=int(os.sys.argv[1])
    ganancia_invalidad=(ganancia < 500 )

print("fin del bucle")
