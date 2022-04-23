# Ejemplo 1
""" lista = [1, 2, 3, 4, 5]
for valor in lista:
	print("Soy un item de la lista y valgo", valor) """


# Ejemplo 2
""" lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in lista:
	print("Soy un valor de la lista y valgo ", num)
	num *= 5
	print("Soy un valor de la lista y ahora valgo ", num) """


# Ejemplo 3 (modificando la lista)
""" indice = 0
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
	numeros[indice] *= 5 # Si aca pongo numeros[numero] *= 5 seria lo mismo y comento indice = 0 y indice += 1
	indice += 1
print(numeros) """


# for con enumerate
""" lista = [66, -3 , 35, 96]
#  Posicion, elemento
for indice, numero in enumerate(lista):
    print(f"INDICE: {indice}")
    print(f"NUMERO: {numero}")
    print(f"-----> {lista[indice]}\n") # Aca imprime lo que hay en el indice en esa vuelta del bucle
# No hace falta crear indice externo por que el enumerate nos devuelve uno cada vez 
# que pasa por un numero de la lista, nos ahorra también incrementar indice en 1 por iteración. Esto
# comparandolo con el Ejemplo 3 (modificando la lista). """


# Otro ejemplo con enumerate
""" frutas = ["Manzana", "Pera", "Naranja", "Banana"]
for elemento in enumerate(frutas): # Podemos pasarle un argumento (frutas, 1) y ese numero es desde donde empieza a contar
	print(elemento) #Fijense que me devuelve una tupla, con el indice y el elemento que se encuentra en ese indice

for indice, elemento in enumerate(frutas): # Cuando hacemos esto estamos desempaquetando la tupla
	print(f"La posicion {indice} corresponde a la fruta {elemento}") """

# Recorriendo un string con for
""" texto = "Hola Mundo, estoy usando for en Python"
for letra in texto:
	print(letra, end="")
	
texto2 = ""
for letra in texto:
	texto2 = letra * 2
print(texto2) """

