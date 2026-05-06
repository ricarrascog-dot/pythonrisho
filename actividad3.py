def calculo(precio, descuento):
    precio_final = precio - (precio * (descuento / 100))
    return precio_final 
datos = [10000, 10]
print("El monto final a pagar es: ", calculo(*datos))