medicamentos = 60000
despacho = 8000

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").upper()

descuento_medicamentos = 0

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.18
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.12

elif edad >= 31 and edad <= 60:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.12
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.08


valor_medicamentos = medicamentos - (medicamentos * descuento_medicamentos)

descuento_despacho = 0

if tramo == "A" or tramo == "B":
    descuento_despacho = descuento_despacho + 0.10

    if edad >= 55:
        descuento_despacho = descuento_despacho + 0.05
valor_despacho = despacho - (despacho * descuento_despacho)

print("El valor de medicamentos es:", int(valor_medicamentos))
print("El valor del despacho es:", int(valor_despacho))