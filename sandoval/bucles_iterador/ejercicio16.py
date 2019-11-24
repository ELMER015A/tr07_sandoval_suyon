# Decodificar interacion de un mensaje
import os
# A= Hello
# B= Que cuentas
# C= Como esta la familia
# D= Cuidate mucho

msg=os.sys.argv[1]

for letra in msg:
    if letra == "A":
        print("hello")
    if letra == "B":
        print("Que cuentas")
    if letra == "C":
        print("Como esta la familia")
    if letra == "D":
        print("cuiadte mucho")

# fin_iterador
print("Fin bucle")
