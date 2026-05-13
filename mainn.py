import utils as u

personas = []
while True: 
    u.mostrar_menu()
   

    try: 
        opcion = int(input("Ingrese una opción: "))
    except:
        print("La opcion debe numérica")
        opcion = 0  
     
    if opcion == 1:
        usuario =u.ingresar_persona() 
        personas.append(usuario)
        print("Opción 1 seleccionada")
    elif opcion == 2:
        u.listar_personas(personas)
        print("Esta es la opcion 2")
    elif opcion == 3: 
        print("Gracias por usar el sistema")
        break 
    else:
        print("Opción no válida, por favor intente de nuevo")          