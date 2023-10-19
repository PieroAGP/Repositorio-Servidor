import requests
import json
import random

#creo una funcion para llamar a la api para que nos devuelva los nombres de los personajes
def obtenerPersonajes():
    #le paso una url
    url = "https://api.gameofthronesquotes.xyz/v1/random/5"
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


#declaramos una funcion para tener un switch en python, el cual sera un dicionario con valores a la respuesta del usuario
def switchOpcion(numeroUsuario):
    switch_dict = {
        1:nombre1,
        2:nombre2,
        3:nombre3,
        4:nombre4,
        5:nombre5
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
    print()
    print("Quien dijo la siguiente frase:")
    print("         ",frase)
    print(f"Opciones: ")
    print(f"          1) {nombre1}, 2) {nombre2}, 3) {nombre3}, 4) {nombre4}, 5){nombre5}")
    print()
    respuestaUsuario=int(input("Seleciona la opcion correcta (1,2,3,4,5): "))
    respuestaUsuarioCadena=switchOpcion(respuestaUsuario)
    
    #comprobamos la respuesta del usuario
    if respuestaUsuarioCadena == personaje:
        resultado ="Acertaste"
    else:
        resultado="Incorrecto"
    #enseñamos resultado
    print()
    print (resultado)
    print()
    print("-------------------------------------------------------------------")
    #devolvemos el resultado
    return resultado

#declaramos una funcion para tener un switch en python, el cual sera un dicionario con valores a la puntuación del usuario
def switchPuntuacion(numeroAciertos):
    puntuacion_dict = {
        0:"0 aciertos",
        1:"1 acierto",
        2:"2 aciertos",
        3:"3 aciertos",
        4:"4 aciertos",
        5:"5 aciertos"
    }
    return puntuacion_dict.get(numeroAciertos, "Puntuación no encontrada")

#creamos una funcion para iniciar una partida
def partidaNueva():
    contador=0
    for i in range(5):
        respuesta=adivinarPersonaje(listaCompleta)
        if respuesta == "Acertaste":
            contador+=1
    resultadoDePuntuacion = switchPuntuacion(contador)
    print()
    if contador<3:
        print("No te preocupes, ¡sigue intentándolo! La próxima vez será mejor.")
    else:
        print("¡Felicidades por tu victoria!")
    print(resultadoDePuntuacion)
    print()

#creamos una funcion para pintar el menu
def menu():
    print("Menú:")
    print("a. ¿Como jugar?")
    print("b. Iniciar una partida")
    print("c. Salir")

#----------------------------------------------------------------------------------------------------------------------------
#declaramos variables de tipo lista para almacenar lo que devuelve el funcion(slugs y nombres de personajes)
nuevaListaSlug,nuevaListaNombre=obtenerPersonajes()
#almacenar los slugs y nombres en variables
slug1,slug2,slug3,slug4,slug5=nuevaListaSlug
nombre1,nombre2,nombre3,nombre4,nombre5=nuevaListaNombre

#almacenar listas de objestos de cada personaje
lista1=funcionDatos(slug1)
lista2=funcionDatos(slug2)
lista3=funcionDatos(slug3)
#unir las lista para tener un base de datos
listaCompleta=lista1+lista2+lista3


#muestro menu y sus opciones
while True:
    menu()
    opcionMenu=input("Selecione una opción: ")
    if opcionMenu=="a":
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("Para poder jugar, necesitas seleccionar la opción 'Iniciar una partida'. \nLuego, el juego comenzará, el cual consiste en adivinar personajes \nde Game of Thrones según la frase que te toque aleatoriamente. \nPara cada frase, se te mostrarán las opciones.")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print()
    elif opcionMenu=="b":
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        partidaNueva()
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print()
    elif opcionMenu=="c":
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        salir=input("Seguro que quieres salir (s/n): ")
        if salir!="n":
            print("--------------------------------------------------------------------------------------------------------------------------------------")
            break
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print()
    else:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("No existe opción, seleciona una opción a,b,c")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print()
