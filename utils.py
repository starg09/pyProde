#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pickle


def quitar_comentarios(linea):
	"""Recibe como parámetro una línea y elimina todo aquello que este
	a continuación del primer #.
	linea tiene que ser un string.
	"""
	return linea.split('#')[0].strip()


def calcular_puntaje(resultado, pronostico):
	"""Calcula el puntaje obtenido en función del resultado pronosticado
	Suma dos puntos acertar quien gana (local, empate o visitante) y uno 
	por cada uno de los siguientes aciertos:
		* Si acierta la cantidad de goles del local
		* Si acierta la cantidad de goles del visitante
		* Si acierta la diferencia (goles del local menos goles del visitante)

	resultado y pronostico tienen que ser dos diccionarios que tengan las claves
	local y visitante.
	"""
	puntos = 0
	diferencia_real = resultado['local'] - resultado['visitante']
	diferencia_pronosticada = pronostico['local'] - pronostico['visitante']
	if diferencia_pronosticada == diferencia_real:
		puntos += 5 if pronostico['local'] == resultado['local'] else 3
	else:
		if pronostico['local'] == resultado['local']:
			puntos += 1
		if pronostico['visitante'] == resultado['visitante']:
			puntos += 1
		if diferencia_real < 0 and diferencia_pronosticada < 0:
			puntos += 2
		elif diferencia_real > 0 and diferencia_pronosticada > 0:
			puntos += 2

	return puntos


def ordenar_puntajes(lista_puntajes):
	"""Ordena los puntajes de los usuarios primero por orden decreciente del
	puntaje y, en caso de igualdad, por orden creciente del usuario.

	lista_puntajes tiene que ser una lista de diccionarios que tenga al menos
	las claves puntaje y usuario.
	Retorna la misma lista que recibió como parámetro, pero ordenada.
	"""
	lista_ordenada = sorted(lista_puntajes, key=lambda x: (-x['puntaje'], x['usuario']))
	return lista_ordenada


def leer_natural(mensaje):
	"""Muestra un mensaje tantas veces como sea necesario hasta que el
	usuario ingree un número natural (entero mayor a 0).
	"""
	continuar = True
	while continuar:
		continuar = False
		try:
			n = int(raw_input(mensaje))
		except ValueError:
			continuar = True
		else:
			if n < 0:
				continuar = True

	return n


def guardar_en_archivo(pkl_file, contenido):
	"""Guarda lo que le pasen como segundo parámetro en el archivo pkl_file.
	pkl_file tiene que estar abieto en modo binario y para escritura (wb)
	"""
	pickler = pickle.Pickler(pkl_file)
	pickler.dump(contenido)


def leer_desde_archivo(pkl_file):
	"""Lee del archivo pkl_file un registro o elemento del archivo.
	pkl_file tiene que estar abieto en modo binario y para lectura (rb)
	"""
	try:
		data = pickle.load(pkl_file)
		fin_de_archivo = False
	except EOFError:
		data = None
		fin_de_archivo = True
	return data, fin_de_archivo


def limpiar_pantalla():
	"""Limpia la pantalla.
	"""
	os.system('cls' if os.name=='nt' else 'clear')
