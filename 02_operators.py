### Operadores  Aritméticos ###

print(2 + 3) # Suma
print(2 - 3) # Resta
print(2 * 3) # Multiplicación
print(2 / 3) # División
print(10 % 2) # Multiplo (resto de la división)
print(2 // 3) # Flor división (siempre da un número entero porque redondeo, si es decimal)
print(2 ** 3) # Exponente
print(2 ** 3 + 2 - 3 / 1 //4) 


print("Hola " + "Python " + "¿Qué tal?") 
# No se puede incluir un entero con suma
# print("Hola " + "Python " + 5) 
# Pero si podes si usar las funciones de las variables
print("Hola " + str(10)) 
print("Hola " * 4) # Se multiplica la cantidad de veces que dice el número ENTERO no puede ser decimal
print("Hola " * (2 ** 3))  # se puede incluir un calculo sencillo y si el resultado es entero, funciona

my_float = 4.5 * 2
print("Hola " * int(my_float))  # se utiliza la funcion int() para convertir el número decimal en etero y que se puedan repetir los textos


### Operadores  Comparativos ###
print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)
print(2 == 3)
print(2 != 3)
print(2 > 3 == 3)

# Cuando comparamos strings, comprueba la ordenación alfabéticas por ACSII  y si se quiere contar carateres se usa len()
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "aaba")
print(len("Hola") <= len("Hola"))
print("AAAA" >= "aaaa") # Tiene en cuenta los mayúsculas
print("Hola" != "Python")

### Operadores  Lógicos ###


print(3 > 4 and "Hola" > "Python" ) # true and true = true - true and false = false | Si una devuelve false, el resultado es False
print(3 < 4 or  "Hola" > "Python" ) # true or false  =  true | Si al menos  una es true, el resultado es true   
print(3 < 4 and  "Hola" > "Python" and 3 == 4) # Se puede incluir más de 2 argumentos
print(3 < 4 or  ("Hola" > "Python" or 4 > 3) ) # se agrupan en parantesis para separar las operaciones 

print(not(3 > 4))