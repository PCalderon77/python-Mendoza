# Operador ternario
a = 10
b = 5
c = a/b if b!=0 else -1
print(c)

# Es lo mismo que hacer esto!!
if b != 0:
    print(a/b)
else:
    print -1