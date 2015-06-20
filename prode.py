#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils import quitar_comentarios


def parsear_linea_prode(linea):
	"""Crea, a partir de un string que le pasan como parámetro un diccionario
	que representa el pronóstico de un partido de la Copa América.

	La línea tiene que tener el formato:
		numero_partido,goles_local,goles_visitante\n
	Opcionalmente, la línea podrá tener un comentario que comenzará con # y 
	continuará hasta el fin de la línea. Por ejemplo:
		numero_partido,goles_local,goles_visitante  # Comentario que sera ignorado\n
	Dicho comentario deberá ignorarse al momento de parsearla.
	Si la línea no tiene dicho formato, retornará un registro vacío.
	"""
	# TODO: Hacer
	#pass
	str_lista = linea.split("#")[0].rstrip('\n')
	lista = str_lista.split(",")
	if len(lista) == 3:
		return {
			"numero_partido": int(lista[0]),
			"goles_local": int(lista[1]),
			"goles_visitante": int(lista[2])
		}
	else:
		return {}


def importar_prode(archivo):
	"""
	Recibe un archivo csv como parámetro, lo recorre parseando sus líneas y retorna
	una lista de diccionarios donde cada uno de ellos representará el pronóstico del
	usuario para un partido en particular.

	archivo tiene que ser un archivo de texto abierto en modo lectura (rt). Dentro
	de este procedimiento no se abre ni cierra el archivo.
	"""
	# TODO: Hacer
	#pass
	lista = []
	for linea in archivo:
		parseado = parsear_linea_prode(linea)
		if (parseado) and (len(lista)<=26):
			lista.append(parseado)
	return lista



def actualizar_prode(prode, fixture, nuevo_prode):
	"""Actualiza los pronósticos que el usuario haya realizado con la información que 
	se encuentra en el nuevo prode, pero ignorando los resultados de los partidos que
	ya se disputaron y están cargados en el fixture. Los resultados de los partidos 
	que ya se jugaron, así como los de los que faltan jugarse, pueden estar o no.

	Se asume que el prode está ordenado por número de partido, comenzando con el 1 en 
	la posición 0 de la lista y todos los nuevos pronósticos se encuentran en el 
	pronóstico preexistente (nuevo_prode es un subconjunto de los partidos que figuran
	en prode)
	"""
	# TODO: Hacer
	#pass
	for nuevo_item in nuevo_prode:
		nuevo_id = nuevo_item["numero_partido"]
		yajugado = False
		for fechafix in fixture:
			if (fechafix["numero_partido"] == nuevo_id) and (fechafix["jugado"] == True):
				yajugado = True
		if not(yajugado):
			prode[nuevo_id-1] = nuevo_item
	return prode

