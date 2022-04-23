# Escribir un programa que muestre el eco de todo lo que el usuario 
# introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    frase = input("Ingresa tu palabra o frase (Ingrese 'Salir' para salir del sistema): ")
    if frase.lower() == "salir":
        break
    print(frase) 


# Solucion posible
""" while True:
    frase = input("Ingresa tu palabra o frase (Ingrese 'Salir' para salir del sistema): ")
    if frase == "Salir":
        break
    print(frase) """
