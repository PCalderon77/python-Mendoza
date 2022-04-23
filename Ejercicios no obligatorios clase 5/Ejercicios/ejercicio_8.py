# Escribir un programa que almacene el string "python" en una variable (esta sera nuestra contraseña), 
# y luego pregunte al usuario por esa contraseña y 
# hasta que no la introduzca correctamente seguira preguntando indefinidamente.

contraseña="python"

contraseña_ingreso=input("Ingrese una contraseña: ")

while contraseña_ingreso.lower() != contraseña:
    contraseña_ingreso=input("!Contraseña incorrecta! \n ingresala nuevamente: ")

print("Ingreso correctamente !Bienvenido al sistema¡")






















