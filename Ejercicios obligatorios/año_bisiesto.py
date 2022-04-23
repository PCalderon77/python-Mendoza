#Realizar una función llamada año_bisiesto:
#Recibirá un año por parámetro
#Imprimirá “El año año es bisiesto” si el año es bisiesto
#Imprimirá “El año año no es bisiesto” si el año no es bisiesto
#Si se ingresa algo que no sea número debe indicar que se ingrese un número.


#Información a tener en cuenta al realizar el ejercicio:

#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, 
# aunque los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 
# 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.
from xmlrpc.client import boolean


print("Bienvenido al programa que le indicara si el año es bisiesto o no")
año=int(input("Ingrese el año: "))
#Funcion para indicar si el año es bisiesto
def año_bisiesto(año: int)->boolean:
    if (año%4)==0 and (año%100) !=0 :
        return True
    elif(año%400)==0 and (año%100) ==0 :
        return True
    else:
        return False
        

if año_bisiesto(año) == True:
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado no es bisiesto")
