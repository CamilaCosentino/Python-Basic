### Classes ###
# igual que una function la clases funcionan para dozar de principio a fin un objeto
# todo lo que este dentro de esta clase todo tiene que estar vinculado con la lógica (buena práctica)
# indentificar el código más fácil
class MyEmptyPerson: # las clases se usan con CamelCase sin espacios ni _
    pass # es un marcador de posición que evita que el programa emita un mensaje de error, es para cuando vamos creando la clase y no salte 

print(MyEmptyPerson()) # se puede llamar una clase con o sin parentesis

class Person:
    def __init__(self, name, surname): # contructor (seflf es requerido)
        self.name = name
        self.surname = surname # crea una prop dentro de persona con self. y se puede acceder dede afuera
    
my_person = Person("Camila","Cosentino")
print(f"{my_person.name} {my_person.surname}")

class PersonOneProp:
    def __init__(self, name, surname, alias ="Sin alias"): # contructor (seflf es requerido) se puede pasar paramentro por defecto
        self.__name = name # __prop es para crear una propiedad privada
        self.__surname = surname
        self.fullname = f"{name} {surname} ({alias})" # Se puede crear una clase con una sola prop y formatiando el texto
    def get_name(self):
        return self.__name # no se puede modificar
    def walk(self): # se puede pasar self por defecto para acceder los elementos guardados dentro de él
         print(f"{self.fullname} Está caminando")  
    
my_person2 = PersonOneProp("Camila","Cosentino")
print(my_person2.fullname) 
print(my_person2.get_name())
my_person2.walk()
my_other_person = PersonOneProp("Alexis", "Gomez", "GZ4003")
print(my_other_person.fullname)
my_other_person.walk()
my_other_person.fullname = "Lourdes Ferrara (makeupbyLour)"
print(my_other_person.fullname)