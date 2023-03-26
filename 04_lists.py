### Listas ###
# las listas ya no es tipo base (string, inter, float, boolean), es para estructurar datos, pareciddas que las arrays pero con más operaciones, no tan manual.
# las listas funcionan también con las funciones de las variables
# las listas son más dinámicas que las arrays, es decir que es un super conjunto de una array.
my_list = list() 
my_other_list = [] 
# Dos maneras de crear Listas..
print(len(my_list))


my_list = [22,23,24,25, 25, 26]
print(my_list)
print(len(my_list))


my_other_list = [23, 1.66, "Camila", "Cosentino"] # Se puede incluir cualquier tipo de datos, y pueden ser diferentes.
print(type(my_other_list)) 


print(my_other_list[0]) # el primer elemento es el 0
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Camila")) #Cuenta la cantidad de veces que contiene ese valor
# print(my_other_list[4])  IndexError - no existe index en esa posición
# print(my_other_list[-5]) IndexError - no existe index en esa posición


age, height, name, surname = my_other_list
# Devuelve en orden, de la lista. Necesita todo los elementos, es decir, si la lista contiene 4 posiciones tiene que decontruir en 4 no menos o más. 
print(name)
# Forma más rebuscada de hacerlo. Más posibilidad de que sucedan errores.
name, height, age, surname = my_other_list[2], my_other_list[1] , my_other_list[0] , my_other_list[3] 
print(age)


print(my_list + my_other_list) # Se puede concatenar/agrupar los elementos. Solo acepta la operación de suma 


print([1,2,3,4]) 

print(list([1,2,3,4])) 

my_other_list.append("CCportfolio") # append() se usa para agregar un elemento al final de la lista
print(my_other_list) 

my_other_list.insert(1, "Aqua") # insert() se le envian 2 argumentos la posición y el elemento a agregar.
print(my_other_list) 

my_other_list[1] = "Aquamarine" # Para remplazar un valor
print(my_other_list)

my_other_list.remove("CCportfolio") # remove() elimana el valor que se envuentra dentro los parentesis
print(my_other_list) 

my_list.remove(25) # remove() elimana el valor que se envuentra dentro los parentesis, este caso el valor se repite, entonces elimina solo el primero encontrado con ese valor. 
print(my_list) 

print(my_list.pop()) # pop() elimina el último elemento, por defecto y si por lo necesitamos devuelve el valor eliminado
print(my_list) 

my_pop_element = my_list.pop(3)
print(my_pop_element) # si al pop(arg1) se le pasa un argumento, elimina el valor de ese index.
print(my_list) 

del my_list[1] # el del se utiliza para eliminar el valor en el index mencionado pero sin retornarlo. Eliminación por índice.
print(my_list)

my_new_list= my_list.copy() # copy() sirve para copiar la lista en esa instancia.

my_list.clear() # es para vaciar la lista.
print(my_list)
print(my_new_list)

my_new_list.reverse() # reverse() invierte la lista. Primero hay que ejecutar reverse()
print(my_new_list)

my_new_list.sort() # sort() por defecto, ordena de menor a mayor.
print(my_new_list) 

print(my_new_list[1:3]) # devuelve los valores entre esos índices.

# Cambio el tipo de dato
my_list = "Hola Python"
print(my_list)
print(type(my_list))

