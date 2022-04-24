# Realizar las instrucciones
# A partir de una lista realizar las siguientes tareas:
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# 1-Borrar los elementos duplicados
# 2-Ordenar la lista de menor a mayor
# 3-Ordenar la lista de mayor a menor
# 4-Realizar una suma de todos los números de la lista. 🤫 sum()
# 5-Añadir como primer elemento de la lista la suma realizada insert(0, suma)
# 6-Comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

#1-
print(lista)
conjunto = set(lista)
print(f"Borramos los elementos duplicados {set(conjunto)}")

# 2-
lista.sort()
print(f"Lista ordenada de menor a mayor: {lista}")

# 3-
lista.sort(reverse=True)
print(f"Lista ordenada de mayor a menor: {lista}")

# 4-
print("La suma de todos los elementos de la lista es: ",sum(lista))
print("La suma de todos los elementos del conjunto es: "sum(conjunto))

# 5-
lista.insert(0, sum(lista))
print(lista)

# 6-
print(lista[0] == sum(lista[1:])) 