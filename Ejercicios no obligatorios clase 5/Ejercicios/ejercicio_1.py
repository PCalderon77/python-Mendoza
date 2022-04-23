# Escribir un programa que enumere los países de la siguiente lista:-------3
paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
contador=0
for i in paises:
    contador+=1
    print(contador,"-",i)












# Solucion 1
""" for indice, elemento  in enumerate(paises):
    print(f"En el indice {indice} se encuentra el país {elemento}") """

# Solucion 2
""" for pais in paises:
    print(pais) """
