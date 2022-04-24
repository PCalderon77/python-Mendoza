# Programa las siguientes instrucciones de forma ordenada sobre la variable animales:
# Inicialmente el diccionario es: 
animales = {"elefante": ""}

# 1- Añade al diccionario las claves perro, tigre y mono con sus respectivos valores “Bobby”,  “Peepe” y “homero”
# 2- Modificá las claves elefante y delfin con los valores “Trompis”y “Manolo” respectivamente

# 1-
animales.update({"perro": "Bobby", "tigre": "Peepe", "mono": "homero"})
print(animales)

# 2-
animales.update({"elefante": "Trompis", "delfin": "Manolo"})
print(animales)



# 1-
# Tambien con la clave
# animales["perro"] = "Bobby"
# animales["tigre"] = "Peepe"
# animales["mono"] = "Homero"
# print(animales)
#2-
#animales["elefante"] = "Trompis"
#animales["delfin"] = "Manolo"
#print(animales)