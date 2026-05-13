def mostrar_menu():    
    print("*****Menu*****") 
    print("1) Agregar persona")
    print("2) Listar personas")
    print("3) Salir")  
def opcion_menu():
    flag_opcion = True
    opcion = 0
    while flag_opcion:
        try: 
            opcion = int(input("Ingrese una opción: "))
            flag_opcion = False
        except:
            print("La opcion debe numérica")
    return opcion    
def ingresar_persona():
    nombre = validacion_texto("Ingrese el nombre de la persona: ")
    correo = validacion_texto("Ingrese el correo de la persona: ")

    usuario = {"nombre": nombre, "correo": correo}
    return usuario

def validacion_texto(texto_a_mostrar):
    flag_texto = True
    texto = ""
    while flag_texto == True:
        texto = input(texto_a_mostrar)
        if texto != "":
            flag_texto = False
        else:
            print("El texto no puede estar vacio")
    return texto  

def listar_personas(lista):
    for persona in lista:
        print(persona)      