n1 = 1290223
n2 = 12190920

if(n1 <= 0 and n2 <= 0):
    print("Ingrese un numero mayor que cero")
elif (n1%2 == 0 and n2%2 != 0):
    print (n1, "es un numero par y", n2, "es impar")
elif (n1%2 == 0 and n2%2 == 0):
    print(n1, "es par y",n2,"tambien es par")
elif (n1%2 != 0 and n2%2 != 0):
    print(n1, "es impar y",n2,"tambien es impar")
else:
    print(n1, "es impar y", n2, "es par")
