#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, 
#debe repetirse el proceso hasta que lo introduzca correctamente.

num= int(input("Ingrese un numero impar: "))


while num%2== 0:
    num=int(input("El numero ingresado no es correcto, ingrese un numero impar: "))

print("Correcto el numero ingresado es impar y es el numero ingresado es: "+ str(num))
