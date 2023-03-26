# Las variables tienen operaciones/funciones con las que se puede utlizar las variables. Ej: type()
# las variables se nombran todo en minusculas, no hay mayusculas y lo más recomendable es usar _
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 1
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Con str() se puede convertir un variable de cualquier tipo a una variable de tipo String
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Print acepta + de 1 argumento
# Concatenacion de Variables imprimidas
print(my_string_variable , my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable) # las comas ayudan a concatenar

# Funciones del sistema
print(len(my_string_variable)) # apreviatura de length (ayuda a cantidad el largo de la variable), solo toma un argumento


#Variables en una sola linea (aunque no es 100% recomedable, es fácil generar errores)
name, lastname, alias, age = "Camila", "Cosentino", "Cami", 22
print("Me llamo", name, lastname,",mi edad es",age, "y me dicen", alias)

# Nombrando con el mismo nombre una variable lo que va a suceder que el valor de la anterior va a ser remplazado por el nuevo.
# En este caso se utiliza la funcion input()

name = input("¿Cuál es tu nombre? ")
age =  input("¿Cuántos años tienes? ")
print(name)
print(age) 


# Cambiamos el tipo de dato
name = 23
age = "Camila"
print(name)
print(age)

# ¿Forzamos el tipo?
address : str = "mi dirección"
address = 34
print(address)
print(type(address))


