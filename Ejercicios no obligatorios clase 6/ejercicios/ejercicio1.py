# Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
# 1- Añade los usuarios: Ana, Ramón, Marta, Eric, David
# 2- Elimina los usuarios: Mario, Miguel, Esteban
grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

lista = ["Ana", "Ramon", "Marta", "Eric", "David"]
for i in lista:
  grupo.add(i)
print(grupo)


grupo.discard("Mario")
grupo.discard("Miguel")
grupo.discard("Esteban") 
print(grupo)


# 1-
# Con update()
#pero se le puede pasar una lista grupo.update(["Ana", "Ramon", "Marta", "Eric", "David"])
# print(grupo)

# Con add()
# grupo.add("Ana")
# grupo.add("Ramon")
# grupo.add("Marta")
# grupo.add("Eric")
# grupo.add("David")
# print(grupo)

# 2-
# Con remove()
# grupo.remove("Mario")
# grupo.remove("Miguel")
# grupo.remove("Esteban") # Al no estar Esteban lanza un error

# ¿Con la funcion pop() se puede realizar?
# pop elimina un elemento aleatorio, entonces no se cual estoy borrando.