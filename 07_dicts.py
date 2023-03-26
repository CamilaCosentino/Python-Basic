### Dictionaries ###
# Tipo de estructura donde se puede almacenar datos de clave:valor
my_dicts = dict()
# de la misma forma que los sets pero la sintásis dentro de ellas es diferencia.
my_other_dicts = {}

print(type(my_dicts))
print(type(my_other_dicts))


# Sintásis parecida al JSON y también con la cuál se diferencia al set.
my_dicts = {"Nombre": "Camila",
            "Apellido": "Cosentino", "Edad": 22, 1: "Python"}
my_other_dicts = {
    "Nombre": "Camila",
    "Apellido": "Cosentino",
    "Edad": 22,
    "Lenguages": {"Python", "Node.js", "JavaScript"},
    1: 1.63
}


print(my_dicts)
print(my_other_dicts)
print(len(my_dicts))
# El largo se basa en la cantidad de claves que contiene.
print(len(my_other_dicts))


# Imprime el valor de esa clave, facilidad de entrar a los dicts
print(my_other_dicts["Nombre"])

my_other_dicts["Nombre"] = "Alexis"

print(my_other_dicts["Nombre"])  # Se puede modificar el valor de una clave.

print(my_other_dicts[1])

# es la forma de agregar un nuevo campo a un dict
my_other_dicts["Calle"] = "Nogoyá"

print(my_other_dicts)

# si accedemos a un elemento se elimina, sino se borra la variable
del my_other_dicts["Calle"]

print(my_other_dicts)


print("Cosentino" in my_other_dicts)  # Retorna false ya que busca por la clave
print("Apellido" in my_other_dicts)  # Retorna true ya q existe esa clave.
# Metodos
print(my_other_dicts.items())  # Devueve el listado de los items
print(my_other_dicts.keys())  # Devuelve solamente las claves
print(my_other_dicts.values())  # Devuelve solamente los valores
# Crea un dict sin valores, como argumento se le incluye las claves. No es necesario crear un dict en base al my_other_dict
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
# Después de crearlo puedes asignarle los valores. Es más recomendable crear un dict de 0.
my_new_dict["Nombre"] = "Alexis"
my_new_dict[1] = "Python"
my_new_dict["Piso"] = 3954

print(my_new_dict)

my_list = ["Nombre", 1, "Piso"]
# 3 formas de mostrar con la funcion formkeys()
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys((my_list))
print((my_new_dict))
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

# --------------------------#
# Con una linea de código crea un nuevo dict con uno ya creado
my_new_dict = dict.fromkeys(my_other_dicts)
print(my_new_dict)
# El value de recibe el valor(cualquier tipo de dato) a todas las claves del dict.
my_new_dict = dict.fromkeys(my_other_dicts, "Camila")
print(my_new_dict)

my_values = my_other_dicts.values()
print(type(my_values))  # el tipo de dato es dict-values no es un dict..
# si queremos un dato como tal, se tiene q convertir a una lista y ahi retona todos los valores del dict(en este caso Camila
print(list(my_new_dict.values()))
# Cuando lo convertimos a otro tipo de dato, como list, tuple, set. te elementos que lo componen son las claves del dict

print(list(my_other_dicts))
print(tuple(my_other_dicts))
print(set(my_other_dicts))
