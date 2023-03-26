### Functions ###
# basicamente intetamos agrupar lógica y para facilitar la solución de problemas
def my_function (): # def nombre de la función y ()
    print("Esto es una función")
    
my_function()

def my_sum_two_values (first_value, second_value): # se puede mandar 2 paramentros dentro de los ()
    print(first_value + second_value) # si se pone otro tipo de operación como - , * o / se rompe el string ya que no se acepta
    
my_sum_two_values(3,4)
my_sum_two_values(344,4222)
my_sum_two_values("3","2") # como es un string concatena las cadenas de texto
my_sum_two_values(3.4,4.3)

def my_sum_two_values_with_return (first_value, second_value): # se puede mandar 2 paramentros dentro de los ()
    my_sum = first_value + second_value
    return my_sum # con return devuelve algo obviamente no imprime nada

my_result = my_sum_two_values_with_return(12,3) # se puede asignar una función a una variable
print(my_result)

print( my_sum_two_values_with_return(10,3))

def print_name (name , surname):
    print(f"{name} {surname}") 
    
print_name(surname="Cosentino",name="Camila") # se puede predeterminar los valores de los paramentros por si se ingresan desordenados 


def print_name_with_default (name , surname, alias = "Sin alias"): # se puede declarar un valor por defecto y si alias no tiene valor se enviar el predeterminado
    print(f"{name} {surname} {alias}") 
    
print_name_with_default("Camila", "Cosentino", "Cami")
print_name_with_default("Camila", "Cosentino")

def print_upper_texts(*text): # con el * antes del paramentro te deja incluir más de un argumento a la hora de llamar la función
    print(type(text)) # se interpreta como una tuple()
    for i in text: # con in for intera los argumentos en cada vuelta (se le puede enviar una lista pero de forma infinita ya que vos pones la cantidad de parametros que quieras)
        print(i.upper())
    
print_upper_texts("Hola","Python", "CC0905")