x = 300
v1 = 100
v2 = 300

if x > 0 and x <= v1:
    print("pago con efectivo")
elif x > v1 and x <= v2:
    print("pago con tarjeta debito")
elif x > v2:
    print ("pago con tarjeta credito")
else:
    print("valor de compra invalido")

