# Utilizando operadores lógicos, determina si una cadena de texto introducida 
# por el usuario tiene una longitud mayor o igual que 8 (es suficiene con mostrar True o False).
# Pista: Recuerden la funcion para medir la longitud de una cadena. 😊

print("Ingresa una palabra")
palabra=input("Palabra: ")

valor=False
if len(palabra)== 8:
    valor=True
    print("La palabra ingresada tiene una longitud de 8 caracteres.")
else:
    print("La palabra ingresada es: ",palabra)




