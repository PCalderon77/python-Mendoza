#Localiza el error en el siguiente bloque de código. 
# Crea una función con la excepción para evitar que el programa se bloquee y 
# además explica en un mensaje al usuario la causa y/o solución:
#resultado = 10/0



def division(num1:float ,num2:float)->float:

    while True:
        try:
            num1=float(input("ingresa el numero que quieres dividir:"))
            num2=float(input("ingresa el divisor:"))
            return round(num1/num2, 2)
        except ZeroDivisionError:
            print("No se puede dividir por cero, ingrese un divisor diferente de 0")
        except ValueError:
            print("No se introdujeron numeros, intente de nuevo")
            


print(division(num1, num2))




