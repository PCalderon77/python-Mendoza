#Crear un archivo en Visual Studio Code que se llame calcular_nota.py y realizar lo siguiente:

#Crear un programa para calcular la nota final del estudiante en base a 2 exámenes. 
#(La nota final debera ser el promedio de esos dos exámenes)

#Cada una de las notas de los exámenes deberan ser guardadas en variables (por ejemplo nota_1 y nota_2) 
# y se deberan solicitar por medio de inputs (recordar lo de transformacion de tipo de datos, ¿Que tipo de dato devuelve input? 
# ¿A que tipo de dato lo tengo que transformar?).

#Pueden subir una captura del codigo o el archivo calcular_nota.py

print("Bienvenido al programa que calculara la nota final del alumno")
nota_1 = float(input("Ingrese la nota del primer examen: "))
nota_2 = float(input("Ingrese la nota del segundo examen: "))
validacion_1= False
validacion_2 = False
if (nota_1 >0 and nota_1<10) : validacion_1 =True
while validacion_1 == False :
 
 nota_1 = float(input("Ingrese la nota del primer examen que sea valida: "))
 if (nota_1 >0 and nota_1<10) : validacion_1 =True

if (nota_2 > 0 and nota_2<10) : validacion_2 =True
while validacion_2 == False :
 
 nota_2 = float(input("Ingrese la nota del segundo examen que sea valida: "))
 if (nota_2 > 0 and nota_2<10) : validacion_2 =True

nota_final = (nota_1 + nota_2)/2

print("La nota final del alumno es: "+ str(nota_final))

    






