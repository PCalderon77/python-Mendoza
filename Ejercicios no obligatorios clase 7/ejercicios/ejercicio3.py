# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
# vive en <dirección> y su número de teléfono es <teléfono>.


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad:"))
domicilio = input("Ingrese su domicilio: ")
telefono = int(input("Ingrese su telefono: "))

datos_usuario = dict(nombre=nombre, apellido= apellido,edad=edad domicilio= domicilio, telefono=telefono)

#print(datos_usuario)
#En forma de lista lo podemos mostrar de la siguiente manera
#print(f"Bienvenido al sistema {nombre}\nDATOS PERSONALES:\nNombre: {nombre}\nApellido: {apellido}\n Edad:{edad}\nDomicilio: {domicilio}\nTelefono: {telefono}")

print(f"Bienvenido al sistema {nombre} {apellido} tiene {edad} vive en {direccion}  y su numero de telefono es {telefono}")