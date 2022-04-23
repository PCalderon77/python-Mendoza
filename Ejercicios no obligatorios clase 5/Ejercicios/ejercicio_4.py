# Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

# 🖐 Ayuda: Podes utilizar la funciones sum() y range() para hacerlo más fácil. 
# El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

suma=0

for i in range(0,101,1):
    if i%2!=0:
        suma+=i

print(suma)


# Solucion 1
""" suma = 0
for i in range(1, 101, 2):
    suma += i
print(suma) """

# Solucion 2
""" print(sum(range(1, 101, 2))) """