# En una lista encontraremos diferentes operaciones relacionales, CALCULAR MENTALMENTE (🤨🤨🤨) el resultado 
# de cada expresión y almacenarlo en una nueva lista que contendrá únicamente valores lógicos True y False.
# Luego comprobar con print() si lo pensaste bien!

expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]
#false, true, true, true, true


expresiones2 = [
not False,
not 3 == 5,
33/3 == 11 and 5 > 2,
True or False,
True*5 == 2.5*2 or 123 >= 23,
12 > 7 and True < False
]
#true,true, true, true,true, false

print(expresiones)
print(expresiones2)

