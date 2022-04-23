#Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
#cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

total= 0
num= int(input("Ingrese un numero: "))

while num !=0 :
    total +=num
    num= int(input("Ingrese otro numero: "))

print("La suma de todos los numeros ingresados es: "+str(total))