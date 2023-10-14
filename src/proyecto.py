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
        #creamos una lista para devolver los slug
        listaSlug=[]
        #creamos una lista para devolver solo nombres
        listaNombre=[]
        #convierto respuesta a un JSON
        datoPersonajes=respuesta.json()
        #recorro los datos
        for dato in datoPersonajes:
            #alamceno el slug del personaje
            slugPersonaje=dato["character"]["slug"]
            #almaceno solo el nombre del personaje
            nombrePersonaje=dato["character"]["name"]
            #con el metodo .append añado a las listas
            listaSlug.append(slugPersonaje)
            listaNombre.append(nombrePersonaje)
        #devuelvo la lista con los slugs y otra lista con los nombres nombres
        return listaSlug,listaNombre


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


#declaramos una funcion para tener un switch en python, el cual sera un dicionario
def switchOpcion(numeroUsuario):
    switch_dict = {
        1:nombre1,
        2:nombre2,
        3:nombre3
    }
    return switch_dict.get(numeroUsuario,'error')

#declaramos una funcion para adivinar el personaje
def adivinarPersonaje(baseDeDatos):
    #de toda la lista de objetos me da un aleatorio
    objetoAleatorio=random.choice(listaCompleta)
    #filtramos por frase y nombre del personaje
    frase=objetoAleatorio["sentence"]
    personaje=objetoAleatorio["character"]["name"]
    #print(frase)
    #print(personaje)
    print("-------------------------------------------------------------------")
    print("Quien dijo la siguiente frase:")
    print(frase)
    print(f"Opciones: 1) {nombre1}, 2) {nombre2}, 3) {nombre3}")
    print("-------------------------------------------------------------------")
    respuestaUsuario=int(input("Seleciona la opcion correcta (1,2,3): "))
    respuestaUsuarioCadena=switchOpcion(respuestaUsuario)
    
    #comprobamos la respuesta del usuario
    if respuestaUsuarioCadena == personaje:
        resultado ="Acertaste"
    else:
        resultado="Incorrecto"
    #enseñamos resultado
    print (resultado)
    #devolvemos el resultado
    return resultado

def switchPuntuacion(numeroAciertos):
    puntuacion_dict = {
        0:"mal",
        1:"regular",
        2:"bien",
        3:"Exelente"
    }
    return puntuacion_dict.get(numeroAciertos, "Puntuación no encontrada")

#declaramos variables de tipo lista para almacenar lo que devuelve el funcion(slugs y nombres de personajes)
nuevaListaSlug,nuevaListaNombre=obtenerPersonajes()
#almacenar los slugs y nombres en variables
slug1,slug2,slug3=nuevaListaSlug
nombre1,nombre2,nombre3=nuevaListaNombre

#almacenar listas de objestos de cada personaje
lista1=funcionDatos(slug1)
lista2=funcionDatos(slug2)
lista3=funcionDatos(slug3)
#unir las lista para tener un base de datos
listaCompleta=lista1+lista2+lista3
contador=0
for i in range(3):
    respuesta=adivinarPersonaje(listaCompleta)
    if respuesta == "Acertaste":
        contador+=1
resultadoDePuntuacion = switchPuntuacion(contador)
print(resultadoDePuntuacion)
