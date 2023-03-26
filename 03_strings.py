### Strings ###
my_string = "My String"
my_other_string = "My Other String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)


my_new_line_string = "Este es un string\ncon salto de linea" # \n este comando genera un salto de linea
my_new_tab_string = "\tEste es un string con tabulación" # \t genera una tabulación 
my_new_scape_string = "\\t Este es un string \\n con espaciado"
print(my_new_line_string)
print(my_new_tab_string)
print(my_new_scape_string)



# Formateo
name , lastname, age = "Camila" , "Cosentino" , 22
# %s es para formatear un string, %d es para un entero. %f es para un float 
print("Mi nombre es {} {} y mi edad es {}".format(name, lastname, age)) # para utilizar .format() tienen que incluir {} en los lugares donde va el valor/es. (la mejor manera cuando estamos tirando datos tal cual)
print("Mi nombre es %s %s y mi edad es %d" %(name, lastname, age)) # De esta manera, funciona poniendo %x donde se ubican los valores y la x es dependiendo el tipo de dato (# %s es para formatear un string, %d es para un entero. %f es para un float). 
# La opción anterior es la mejor manera cuando hay que formatear datos, y así generar sistemas seguros y evitar errores.
print("Mi nombre es "+ name + " " + lastname  + " y mi edad es" + " " + str(age)) # Manera menor recomendable por al sistema le cuesta más leearlo a comparación de las opciones anteriores, además que es más largo para escribirlo.

#Inferencia de datos
print(f"Mi nombre es {name} {lastname} y mi edad es {age}") # la f funciona para formatear.

# Desempaquetado de caracteres
language = "python"
a, b, c,d,e,f= language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# División
language_slice_two_argument = language[1:3] # devulve la primera posición hasta la última posición que pasamos no incluive. Ej 1:4 devulve las posiciones 1,2,3 la 4 no. 
print(language_slice_two_argument)

language_slice_one_argument = language[1:] # devulve desde la primera posición para adelanta.
print(language_slice_one_argument)

language_slice_only_one_argument = language[-2] # si el número es negativo empieza a contar de atras a adelante.
print(language_slice_only_one_argument)

not_language = language[0:4:3]
print(not_language)
# Reverse 
reversed_language = language[::-2] # devulve el orden de las letras de forma reversa.
print(reversed_language)

# Métodos

print(language.capitalize()) # pone la primer caracter en mayúscula
print(language.upper()) # pone TODO en mayúscula
print(language.count("t")) # cuentas cuanta cant. de el caracter mencionado hay en toda la cadena de texto.
print(language.isnumeric()) # te dice si el sting es un número, devuelve True o False
print("1".isnumeric()) 
print(language.lower()) # pone TODO en minúsculas
print(language.upper().isupper()) # pone TODO en mayúscula y devuelve si es True o False
print(language.startswith("py")) # Valida si el string empieza con "py", devuelve True o False. Es exacto, si tiene mayúsculas devuelve False
