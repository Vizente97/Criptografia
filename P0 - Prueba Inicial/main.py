import fileinput
import math

suma = 0.0

for line in fileinput.input():
    suma = suma + float(line)

parte_decimal, parte_entera = math.modf(suma)

if(parte_decimal > 0):
    print(suma)
else:
    print(int(suma))
