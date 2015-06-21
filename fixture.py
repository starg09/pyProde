#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parsear_linea_fixture(linea):
	"""Crea, a partir de un string que le pasan como parámetro un diccionario
	que representa un partido de la Copa América.

	La línea tiene que tener el formato:
		numero_partido,dia,mes,hora,minutos,instancia,local,visitante\n
	Si la línea no tiene dicho formato, retornará un registro vacío.
	"""
	try:
		nro, dia, mes, hora, mins, inst, loc, vis = linea.strip().split(',')
	except (TypeError, ValueError) :
		return {}

	partido = {
		'numero_partido': int(nro),
		'dia': int(dia),
		'mes': int(mes),
		'hora': int(hora),
		'minutos': int(mins),
		'instancia': inst,
		'local': loc,
		'visitante': vis,
	}

	return partido



def importar_fixture(archivo):
	"""
	Recibe un archivo csv como parámetro, lo recorre parseando sus líenas y retorna
	una lista de diccionarios donde cáda uno de ellos represtará un partido.

	archivo tiene que ser un archivo de texto abierto en modo lectura (rt). Dentro
	de este procedimiento no se abre ni cierra el archivo.
	Retorna una lista de registros que tendrán los mismos campos que tiene la función
	parsear_linea_fixture y le agregará:
		* jugado: indica si el partido se jugó o no y por defecto vale False
		* goles_local: en el caso de haberse jugado el partido indica la cantidad de 
			goles convertidos por el equipo local. Por defecto vale 0.
		* goles_visitante: en el caso de haberse jugado el partido indica la cantidad 
			de goles convertidos por el equipo visitante. Por defecto vale 0.
	"""
	# TODO: Hacer
	#pass
	lista = []
	for linea in archivo:
		parseado = parsear_linea_fixture(linea)
		if parseado:
			parseado["jugado"] = False
			parseado["goles_local"] = 0
			parseado["goles_visitante"] = 0
			lista.append(parseado)
	return lista
