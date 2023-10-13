import requests
import json
import random

#creo una funcion para llamar a la api para que nos devuelva los nombres de los personajes
def obtenerPersonajes():
    #le paso una url
    url = "https://api.gameofthronesquotes.xyz/v1/random/3"
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

#funcion para traer frases de los personajes pasado por parametro
def funcionDatos(nombrePersonaje):
    #declaramos una url nueva con el nombre personaje
    urlNueva = f"https://api.gameofthronesquotes.xyz/v1/author/{nombrePersonaje}/3"
    #llamada a la Api
    respuesta=requests.get(urlNueva)
    #si la api me devuelve algo entro en el if
    if respuesta.status_code == 200:
        #convierto respuesta a un JSON
        datoPersonajes=respuesta.json()
        #devuelvo una lista de objetos(con las frases de los personajes)
        return datoPersonajes

#declaramos una variable de tipo lista para almacenar lo que devuelve el funcion(nombres de personajes)
nuevaLista=obtenerPersonajes()
#almacenar los nombres en variables
nombre1,nombre2,nombre3=nuevaLista
#almacenar listas de objestos de cada personaje
lista1=funcionDatos(nombre1)
lista2=funcionDatos(nombre2)
lista3=funcionDatos(nombre3)
#unir las lista para tener un base de datos
listaCompleta=lista1+lista2+lista3

#de toda la lista de objetos me da un aleatorio
objetoAleatorio=random.choice(listaCompleta)
#filtramos por frase y nombre del personaje
frase=objetoAleatorio["sentence"]
personaje=objetoAleatorio["character"]["name"]

print(frase)
print(personaje)