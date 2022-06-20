#Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla 
# un diagrama de líneas con la evolución de las ventas.
import matplotlib.pyplot as plt


anio_inicial = int(input('Introduce el año inicial: '))

anio_final = int(input('Introduce el año final: '))


lista_ventas = []
lista_anios=[]

for i in range(anio_inicial, anio_final+1):
    ventas = int(input("Ingrese el numero de ventas del año "+str(i)+" : "))
    lista_anios.append(i)
    lista_ventas.append(ventas)
    
print("Ventas: ",lista_ventas)
print("años: ",lista_anios)




fig, ax = plt.subplots()

ax.plot(lista_anios, lista_ventas)

plt.title("Numero de ventas por año")
plt.xlabel("Años")
plt.ylabel("Numero de ventas")

plt.show()










