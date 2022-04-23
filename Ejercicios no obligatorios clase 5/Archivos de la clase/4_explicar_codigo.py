chance = 1
while chance <= 3:
    txt = input("Escribe SI: ")
    if txt == "SI":
        print("Ok, lo conseguiste en el intento", chance)
        break
    chance += 1
else:
  	print("Has agotado tus tres intentos")
