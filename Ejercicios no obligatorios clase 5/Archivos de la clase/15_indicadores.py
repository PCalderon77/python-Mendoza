# Introducir 5 número e indicar si se ha introducido algún número par.
""" indicador  =  False
for var in range(1,6):
	num = int(input("Dime un número:"))
	if num % 2 == 0:
		indicador  = True
if indicador:
	print("Has introducido algún número par")
else:
	print("No has introducido algún número par") """


# Ejemplo de bandera o flag
""" bandera = True
while bandera:
    ingreso_usuario = input("Ingresa tu contraseña: ")
    if ingreso_usuario == "aguantepython":
        print("Has ingresado a tu cuenta!")
        bandera = False # Si no pongo la bandera en False, siempre sera True y quedare en un bucle infinito
    else:
        print("Ingresa una contraseña correcta.")

print("¡Bienvenido al Sistema!") """