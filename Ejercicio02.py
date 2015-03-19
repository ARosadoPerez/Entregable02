# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Sistemas Distribuidos
# Seminario 2 con fecha 17/03/2015

# Autores:
#   José Carlos Solís Lojo
#   Alejandro Rosado Pérez

# Explicación del Programa:
# Este programa se encarga de obtener una lista con todas las palabras contenidas en un fichero
# de texto. Una vez hecho esto, buscará las palabras cuya última letra coincida con la primera letra
# de otra palabra de la lista. Posteriormente, imprimirá por pantalla la lista de palabras que mayor número
# de palabras haya encontrado.

# Comprueba si una palabra ha sido añadida anteriormente a la lista
def estaRepetida(lista, cad):
    for palabra in lista:
        if palabra == cad:
            return True
    return False
# **************************************************

#Busca la siguiente palabra que empiece por la ultima letra de la palabra indicada por parametro
def buscarSiguiente(lista_completa, lista_actual, palabra):
    for cadena in lista_completa:
        if palabra[len(palabra)-1] == cadena[0] and estaRepetida(lista_actual, cadena) == False:
            return cadena
    return ""
# **************************************************

# Programa principal, obtiene la lista de palabras y busca la mejor combinacion de palabras
def emparejarPalabras(ruta):
    lista = []
    with open(ruta) as myfile:
        for line in myfile: # Por cada línea del fichero
            for palabra in line.split(' '): # Por cada palabra de la línea
                palabra = palabra.replace("\n","") # Sustituimos los saltos de línea
                lista += [palabra]

    lista_final = [] # Será la lista que haya obtenido más resultados
    
    for palabra in lista:
        lista_aux = [] # Borramos el contenido de la lista auxiliar
        lista_aux += [palabra]
        siguiente = buscarSiguiente(lista, lista_aux, palabra)
        while siguiente != "": # Mientras encontremos una palabra que sea factible
            lista_aux += [siguiente] # La añadimos
            palabra = siguiente # Actualizamos la palabra
            siguiente = buscarSiguiente(lista, lista_aux, palabra) # Buscamos la siguiente
    
        if len(lista_aux) > len(lista_final): # Si hemos obtenido más palabras en esta iteración
            lista_final = list(lista_aux)
    
    print lista_final
# **************************************************
    
fichero = raw_input("Introduzca el nombre del fichero (ej. 'pokemon.txt'): ")
print "Mayor lista encontrada: "
emparejarPalabras(fichero)

# <codecell>


