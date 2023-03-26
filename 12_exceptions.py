### Exceptions Handling ###
# Manejo de errores 
# no es lo mismo un condicional que un try except
# controlar el programa para evitar que la app se rompa 
# se puede no poner el else o el finally pero el TRY y EXCEPT son Obligatorios
number_one,number_two = 5, 1
number_two = "1"

# try except
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
    
    
# try except else(opcional)
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce un error
    print("Se ha producido un error")
else: 
    # si se produce una excepción no se ejecuta, solo la del try y el else
    print("La ejecución continua correctamente")
    
# try except else(opcional) finally(opcional)
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce un error
    print("Se ha producido un error")
else: 
    # si se produce una excepción no se ejecuta, solo la del try y el else
    print("La ejecución continua correctamente")
finally:
    # se ejecuta siempre salte error o no
     print("La ejecución continua")

# print(number_one+number_two) si la ejecución esta afuera y tienen un error va a romperse


# Manejo de errores por tipo

try:
    print(number_one+number_two)
    print("No se ha producido un error")
except TypeError: # se ejecuta solo si se produce un TypeError (en este caso)
    print("Se ha producido un error")
    
# Captura de la información de la excepción   
try:
    print(number_one+number_two)
    print("No se ha producido un error")
except ValueError as error: # as error (error la cual es una variable donde captura el error)
    print(error)
except Exception as e: # Exception global que captura si hay un error de cualquier tipo
    print(e)