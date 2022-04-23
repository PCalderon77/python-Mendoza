#Pedirle al usuario que ingrese dos numeros, y cada uno de esos numeros guardarlos en variables,
#luego comparar esos dos numeros para ver si son iguales (==) imprimendolos por pantalla (dara True o False)🤓

print("Ingrese dos numeros e indicara verdadero si son iguales o falso si son distintos")

num1=int(input("num1: "))
num2=int(input("num2: "))

valor=False

if num1 == num2:
    valor=True

print("Los numeros ingresados son: ",num1," y ", num2," su valor es: ", valor)