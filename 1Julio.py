age = -1

r1 = 18
r2 = 60
r3 = 110

if (age <= 0):
    print("Edad invalida")
elif (age > 0 and age < r1):
    print ("Solo puede entrar a las atracciones de menores de edad")
elif (age >= r1 and age <= r2):
    print ("Puede utilizar todas las atracciones del parque")
elif (age >= r2 and <= r3):
    print("Solo puede utilizar algunas atracciones")
else:
    print("Edad invalida")