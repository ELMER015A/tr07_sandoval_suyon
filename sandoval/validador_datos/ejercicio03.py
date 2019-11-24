# validar la distancia de un ciclista mayoa 1000 kilometros
import os
distancia=0.0
distancia_invalida=True
while (distancia_invalida):
    distancia=int(os.sys.argv[1])
    distancia_invalida=(distancia > 1000)

# fin del bucle
print("fin del bucle")
