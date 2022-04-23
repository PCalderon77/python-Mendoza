# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# Por ejemplo, el usuario ingresa "Hola como andas" (mediante input) y despues ingresa la letra "a" (mediante input) --> 
# el resultado debera ser 3, porque hay 3 letras "a" en esa frase.



palabra=input("Ingrese una frase: ")
letra=input('Ingrese una letra: ')

contador=0

for i in palabra:
    if i == letra:
        contador+=1

print("La letra ",letra," se encuentra ",contador, "veces en la palabra: ", palabra)