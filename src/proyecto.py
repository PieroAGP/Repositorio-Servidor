import requests
import json

#le paso una url
url = "https://api.gameofthronesquotes.xyz/v1/random/5"
#llamada a la api
respuesta=requests.get(url)
#si la api me devuelve algo entro en el if
if respuesta.status_code == 200:
    #convierto en un jason
    datoPersonajes=respuesta.json()
    #recorro los datos
    for dato in datoPersonajes:
        #almaceno solo el nombre 
        nombrePersonaje=dato["character"]["slug"]
        #muesto por consola el resultado
        print(nombrePersonaje)