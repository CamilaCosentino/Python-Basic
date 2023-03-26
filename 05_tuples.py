### Tuplas ###
# Las tuplas son valores contantes, no pueden ser modificados my_tuple[1] = 1.65 como en las lista. 
# Una tupla es inmutable, inmodificable
my_tuple = tuple()
my_other_tuple= (34,52,51,20)
# 2 formas de definirlas.

my_tuple = (23, 1.63, "Alexis Gabriel" , "Gomez")
print(my_tuple)
print(type(my_tuple))

# Puede seleccionarse como las listas, seleccionando el índice.
print(my_tuple[0])
print(my_tuple[-1])

# Esto salta error ya que no existen elementos en esos índices
#print(my_tuple[4])
#print(my_tuple[-6])
# Soporta estos 2 métodos
print(my_tuple.count("Gomez")) # funciona de la misma manera que en las listas, cuanta la cantidad de veces que aparece ese valor.
print(my_tuple.index("Alexis Gabriel")) # devuelve la posición donde se encuentra esa elemento.

# my_tuple[1] = 1.65  TypeError: 'tuple' object does not support item assignment

mysum_tuple =  my_tuple + my_other_tuple
print(mysum_tuple ) # Se pueden sumar 2 tuplas


print(mysum_tuple[3:6]) # devuelve los elementos entre esos índices.

# CASO EXCLUSIVO. Una tupla se puede convetir a una lista para poder modificar/mutar los datos (para que el sistema sea más seguro), no es recomedable estar convirtiendo.
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Gómez"
my_tuple.insert(1,"Negro")

print(my_tuple)

my_tuple = tuple(my_tuple)
print(type(my_tuple))

# del my_tuple[2] # Error, no se puede eliminar un valor porq una tupla es inmutable.
del my_tuple # del elimina la variable, NO es un clear()
# print(my_tuple) NameError: name 'my_tuple' is not defined

