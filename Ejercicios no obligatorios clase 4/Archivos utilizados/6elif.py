# Ejemplo ELIF
""" comando = "SALUDO"

if (comando == "ENTRAR"):
    print("Bienvenido al sistema.")
elif (comando == "SALUDO"):
    print("Hola! ¿Cómo estás?")
elif (comando == "SALIR"):
    print("Saliendo del sistema.")
else:
    print("No se reconoce el comando.") """



#Ejemplo IF --> Va a entrar en todos los IF y yo no quiero eso
""" nota =  9
if nota >= 9:
	print("Sobresaliente.")
if nota >= 7:
	print("Muy bien")
if nota >= 6:
	print("Bien")
if nota >= 4:
	print("Regular")
else:
	print("Insuficiente") """
#Como arreglarlo!!
""" nota =  6
if nota >= 9:
	print("Sobresaliente.")
elif nota >= 7:
	print("Muy bien")
elif nota >= 6:
	print("Bien")
elif nota >= 4:
	print("Regular")
else:
	print("Insuficiente") """
#Otra forma sin usar elif, solo if, pero con mas codigo. Es preferible usar los elif
""" nota =  9
if nota >= 9:
	print("Sobresaliente.")
if nota >= 7 and nota < 9:
	print("Muy bien")
if nota >= 6 and nota < 7:
	print("Bien")
if nota >= 4 and nota < 6:
	print("Regular")
else:
	print("Insuficiente") """