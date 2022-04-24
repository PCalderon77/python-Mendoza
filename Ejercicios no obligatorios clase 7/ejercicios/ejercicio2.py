# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

divisas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}

divisa_usuario=input("Ingrese la divisa para ver el correspondiente simbolo: (Euro ,Dolar ,Yen) \n-Divisa:")

guardar_seleccion = divisas.get(divisa_usuario, "No tenemos registrado el simbolo de esa divisa")
print(guardar_seleccion)

# Solucion 2
# usuario_divisa = input("""Ingrese la divisa para ver el correspondiente simbolo:
# - Euro
# - Dolar
# - Yen
# """)

#print(divisas[divisa_usuario])


# Solucion 3
# Probar con capitalize, con strip
#moneda = input("Introduce una divisa: ")
#if moneda.title() in divisas:
#    print(divisas[moneda.title()])
#else:
#    print("La divisa no está.")