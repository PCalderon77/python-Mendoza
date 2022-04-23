# Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.


horas=float(input("Ingresa la cantidad de horas trabajadas: "))
costo=float(input("Ingresa el costo por hora: "))

resultado= horas * costo

print("Te pagan al dia:",resultado)