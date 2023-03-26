### SETS ###
# Un set de base tiene un lista. 
# Un set no es una estructura ordenada.
my_set = set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) # inicialmente es un "dict"


my_other_set = {"Camila","Cosentino", 22} # Pero la sintáxis de un set es así, el diccionario es diferente.
print(type(my_other_set)) 

print(len(my_other_set))

# print(my_other_set[2])  TypeError: 'set' object is not subscriptable


my_other_set.add("CC0905") # add(arg) agrega un valor.
print(my_other_set)

my_other_set.add("CC0905") # Básicamente no admine elementos repetidos
print(my_other_set)


print("CC0905" in my_other_set) # Devuelve un boolean si esta el elemento en el set, en este caso es TRUE
print("CC0503" in my_other_set)  # Devuelve un boolean si esta el elemento en el set, en este caso es FALSE

my_other_set.remove("Cosentino")  # remove(arg) elemina es elemento que se encuentra como argumento de método.
print(my_other_set)

my_other_set.clear()
print(my_other_set) # clear() vacia el set.
# para ver las funciones de las variables se le incluye un .
del my_other_set # NameError: name 'my_other_set' is not defined, elimina la variable del sistema.
# print(my_other_set) 

my_set = {"Camila", "Cosentino", 22}
# No es recomendable, ya que en cada vez que ejecutamos el sistema, es otro valor. Es arriesgado
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Node.js", "Python", "JavaScript"}

my_new_set = my_set.union(my_other_set) # union(set) une dos sets 
print(my_new_set)

print(my_new_set.union(my_new_set)) # No se agrega nuevamente, porque los set no te acepta repetidos, no importa cuentas veces se pase union, si los datos no son diferentes no va a funcionar
print(my_new_set.union({"React.js","Next.js"})) # De está forma si funciona también pero dentro de los () hay que incluir {} y después los valores.

print(my_new_set.difference(my_set)) # diferencia() devuelve los valores sin contar los elementos que se encuentran en set enviado, y lo que se envio anteriormente con el .union() porque se envio dentro del print
