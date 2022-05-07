#Realizar una función llamada par_o_impar:
#Recibirá un número por parámetro.
#Imprimirá Par si el número es par
#Imprimirá Impar si el número es impar
#Si se ingresa algo que no sea número debe indicar que se ingrese un número.


def par_o_impar():

    while True:
        try:
         numero=int(input("ingrese un numero para determinar si es par o impar:"))
         if numero%2==0:
             print("El numero ",numero," ingresado es par")
             break
         else:
             print("El numero ",numero," es impar")
             break
        except ValueError:
         print("El valor ingresado no es un numero, ingrese numero:")

par_o_impar()
    