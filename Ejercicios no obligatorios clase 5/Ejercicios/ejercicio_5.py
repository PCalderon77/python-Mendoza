# Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# 🖐 Ayuda: Recuerden, la conversión de listas es mi_lista=list(range(inicio,fin,salto))

lista=[]

for i in range(0,11,1):
    lista.append(i)

print("La lista creada es: \nLista:",lista)


mi_lista=list(range(-10,1,1))
print("La lista creada es: \nLista:",mi_lista)

mi_lista=list(range(0,21,2))
print("La lista creada es: \nLista:",mi_lista)

mi_lista=list(range(-19,1,2))
print("La lista creada es: \nLista:",mi_lista)

mi_lista=list(range(0, 51, 5))
print("La lista creada es: \nLista:",mi_lista)













