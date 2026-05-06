diccionario = {"Nombre": "Cesar Huispe","fonos": [9877882,963503690,8777792],"activo": True} 
#
print ("Nombre", diccionario["Nombre"])
print ("Segundo Telefono",diccionario["fonos"][1]) 
#Inserción 
diccionario["email"]="cesar.huispe@example.com"
diccionario["fonos"].append(123456789) 
#Actualizacion
diccionario["activo"]=False
diccionario["fonos"][0]=999999999
#Eliminación 
del diccionario["activo"]
diccionario["fonos"].pop(2)

print(diccionario)