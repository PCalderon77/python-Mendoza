# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# | Fruta  | Precio|
# |Banana  | 250   |
# |Manzana | 150   |
# |Pera    | 130   |
# |Naranja | 100   |

frutas = {'Banana':250, 'Manzana':150, 'Pera':130, 'Naranja':100}

usuario_fruta = input("Ingrese la fruta que desea llevar: ").title() # o .capitalize()
usuario_kilos = int(input("Ingrese los kilos que desea llevar: "))

if usuario_fruta in frutas:
    total = frutas[usuario_fruta] * usuario_kilos
    
print(f"Usted va a llevar {usuario_kilos} Kg de {usuario_fruta} y debe abonar {total}ARS") 