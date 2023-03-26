### Conditionals ###

my_condition =  False
if my_condition: # Es lo mismo que if my_condition == True
    print("Se ejecuta la condición del IF")
    


my_condition = 5 * 5
if my_condition == 10: 
    print("Se ejecuta la condición del 2do IF")


if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")


if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 ")
    
# Con las tabulaciones puede que cambie si está dentro del condicional o fuera
    
print("Es menor o igual que 10 o mayor o igual que 20 ")

print("La ejecución continua")
if my_condition > 10 and my_condition < 20:  
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
       print("es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto que 25 ")

my_string = "" # un string vacio devuelve false
if not my_string: # pero si nosotros negamos la condicion valida si está vacia o no
    print("Mi cadena de texto es vacia")

if my_string == "Holaaaa":
    print("Esttas cadenas de texto coinciden")
    