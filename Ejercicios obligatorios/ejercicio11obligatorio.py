#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
#Construye los siguientes métodos para la clase:
#Un constructor, para sus atributos. Mencionar ¿Que tipo de atributos son?
#mostrar(): Muestra los datos de la persona. 
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.



class Persona:
    
    #Constructor
    def __init__(self, nombre, edad, dni):
        
        #Atributos de la instancia
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    #Metodo para mostrar los datos de la persona
    def mostrar(self):
        print(f"El nombre de la persona es {self.nombre}")
        print(f"Su DNI es {self.dni}")
        print(f"Su edad es {self.edad}")

    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"Es mayor de edad? = { True}")
        else:
            print(f"Es mayor de edad? = { False}")

edad_ingreso = 0
dni_ingreso=None
nombre_ingreso= ""
#Pido los datos por teclado los datos y los valido

nombre_ingreso = input("Ingrese el nombre de la persona: ")  
   
while edad_ingreso == 0:
    try:
        edad_ingreso = int(input("Ingrese la edad de la persona: "))   
    except ValueError:
        print("La edad ingresada no es un numero")

while dni_ingreso == None:
    try:
      dni_ingreso = int(input("Ingrese el DNI de la persona: "))
    except ValueError:
        print("No se introdujeron numeros, intente de nuevo")



#Instancio una persona     
persona1 = Persona(nombre_ingreso, edad_ingreso, dni_ingreso)
#Llamo los metodos
persona1.mostrar()
persona1.es_mayor_de_edad()


