### Modules ###
# un modulo es un código externo que se puede incluir. (libreria, código de los ficheros, etc)
# forma de vincular ficheros.
# evitar replicar código
import my_module 
my_module.sumValue(3,5, 6) # hay q poner el nombre del module.sum() para que funcione, es decir acceder a esa función
my_module.printValue("Camila", 22,"Cosentino")

# from import 10_function my_sum_two_values() no se puede por no tiene un tipo de nombreclatura valido para los modulos
from  my_module import sumValue , printValue # se puede descontracturar el modulo y así traer funciones expecificas
sumValue(3,5, 6) # hay q poner el nombre del module.sum() para que funcione, es decir acceder a esa función
printValue("Camila", 22,"Cosentino")

import math # Python tiene modulos nativos como math
pi = math.pi
print(pi)
pow = math.pow(2,4)
print(pow)

from math import pi as PI_VALUE # Se puede poner el as para ponerle un alias
print(PI_VALUE)