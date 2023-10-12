import requests
import json

#creo una funcion para llamar a la api para que nos devuelva los nombres de los personajes
def obtenerPersonajes():
    #le paso una url
    url = "https://api.gameofthronesquotes.xyz/v1/random/5"
    #llamada a la api
    respuesta=requests.get(url)
    #si la api me devuelve algo entro en el if
    if respuesta.status_code == 200:
        #creamos una lista para devolver solo nombres
        listaNombre=[]
        #convierto respuesta a un JSON
        datoPersonajes=respuesta.json()
        #recorro los datos
        for dato in datoPersonajes:
            #almaceno solo el nombre 
            nombrePersonaje=dato["character"]["slug"]
            #con el metodo .append añado a la lista
            listaNombre.append(nombrePersonaje)
        #devuelvo la lista con los nombres
        return listaNombre

#declaramos una variable de tipo lista para almacenar lo que devuelve el funcion
nuevaLista=obtenerPersonajes()
print("Nombres:")
for nombre in nuevaLista:
    print(nombre)
