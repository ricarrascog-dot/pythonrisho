# --- PROGRAMA DE TIENDA RETAIL ---

opcion = 0

while opcion != 2:
    print("\n--- MENU TIENDA RETAIL ---")
    print("1. Registrar compra")
    print("2. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: debe ingresar un número entero.")
        opcion = 0
        continue # Reinicia el ciclo para mostrar el menú de nuevo

    if opcion == 1:
        print("\n--- Registro de compra ---")
        
        # Validación del monto
        monto = 0
        while monto <= 0:
            try:
                monto = int(input("Ingrese un monto de compra: $"))
                if monto <= 0:
                    print("El número debe ser mayor a cero.")
            except ValueError:
                print("Error: Debe ser un número entero.")

        # Validación del tipo de cliente
        tipo_cliente = input("Ingrese tipo de cliente (Premium / Socio / Normal): ")
        tipo_cliente = tipo_cliente.lower().strip()

        # Cálculo de porcentaje
        if tipo_cliente == "premium":
            porcentaje = 0.20
        elif tipo_cliente == "socio":
            porcentaje = 0.10  # Asumimos que Socio tiene 10%
        elif tipo_cliente == "normal":
            porcentaje = 0.05  # Ejemplo: 5% para normal
        else:
            porcentaje = 0
            print("Tipo de cliente no reconocido, no se aplicará descuento.")

        # Operaciones matemáticas
        descuento = monto * porcentaje
        total = monto - descuento

        # Resultados
        print("\n--- RESUMEN DE BOLETA ---")
        print(f"Monto original: ${monto}")
        print(f"Descuento aplicado ({int(porcentaje*100)}%): ${int(descuento)}")
        print(f"Total a pagar: ${int(total)}")
        print("-------------------------\n")

    elif opcion == 2:
        print("Gracias por usar el sistema. ¡Adiós!")
    else:
        print("Opción inválida, intente de nuevo.")