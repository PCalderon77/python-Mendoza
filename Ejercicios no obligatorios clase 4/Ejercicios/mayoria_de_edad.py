# Escribir un programa que le pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# Nota:	Para preguntarle al usuario, recuerda usar input

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

if edad>=18:
    print("Usted ",nombre," es mayor de edad y tiene ",edad," años")
else:
    print("Usted ",nombre," es menor de edad y tiene ",edad," años")