# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable (Formula --> imc=peso/talla**2) y luego imprima por pantalla el texto segun el resultado del imc:
# imc por debajo de 18.5 debera imprimir "Bajo peso"
# imc entre 18.5 – 24.9 debera imprimir "Normal"
# imc entre 25.0 – 29.9 debera imprimir "Sobrepeso"
# imc entre 30.0 o más debera imprimir "Obesidad"


peso=float(input("ingrese su peso en kg: "))
estatura=float(input("Ingrese su altura en metros: "))

imc=0

def indice_de_masa_corporal(peso:float,estatura:float)->float:
    
    return (peso/pow(estatura,2))


print(indice_de_masa_corporal(peso,estatura))

if indice_de_masa_corporal(peso,estatura)< 18.5:
    print("Bajo peso")
elif indice_de_masa_corporal(peso,estatura)>= 18.5 and indice_de_masa_corporal(peso,estatura)<=24.9:
    print("Normal")
elif indice_de_masa_corporal(peso,estatura)>= 25 and indice_de_masa_corporal(peso,estatura)<=29.9:
    print("sobrepeso")
else:
    print("Obesidad")


