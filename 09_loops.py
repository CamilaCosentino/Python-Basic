### Loops ###
# Mecanismo para iterar (pasar por un código muchas veces)

# While
my_condition = 0

while my_condition < 10: # s va a repetir a traves de una condición
    print(my_condition)
    my_condition += 2 
# if my_condition ==10: # pero obviamente se puede poner el if
   # print("La condición es igual a 10")
else: # es opcional
    # en Python while permite poder un else sin if (este else pertenece al while) pero no lo acepta ni el if ni el elif ya que while funciona como "if infinito"
    print("La mi condición es mayor o igual que 10")
    
    
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiende la ejecución")
        break # con break se detiende la ejecución
    print(my_condition)
    
# For 
# nos sirve para itear un listado de elementos
my_list = list() 
my_list = [11,33,22,23,42,12]
for element in my_list: # va a ejecutarse dependiendo la cantidad de elementos del listado o cualquier estructura donde se puede almacenar elementos
    print(element)
    
my_tuple = (23, 1.63, "Alexis Gabriel" , "Gomez")
my_set = {"Camila", "Cosentino", 22}
my_dicts = {
    "Nombre": "Camila",
    "Apellido": "Cosentino",
    "Edad": 22,
    "Lenguages": {"Python", "Node.js", "JavaScript"},
    1: 1.63
}

for element in my_tuple:
    print(element)
    
for element in my_set:
        print(element)
        
for element in my_dicts: # impreme las claves
        print(element)

        
for element in my_dicts.values(): # impreme las valores
        print(element)
    
    
        
for element in my_dicts: # impreme las claves
        print(element) 
        if element == "Edad": # detiene en cuando llega a la clave "Edad"
          
            break # se puede utilizar un break para deterner la operación si la condición es TRUE
           # continue # continua pero no corta la funcion sino vuelve al comienzo y ejecuta el resto. No se conseja usarlo ya que rompe el tema que Python de ser un lenguaje moderno
else: # se puede poner el ELSE como con el while
    print("El bucle for ha terminado")
# el elif no se puede utilizar con un for