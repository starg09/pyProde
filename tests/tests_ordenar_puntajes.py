#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from utils import ordenar_puntajes


class TestOrdenarPuntajes(unittest.TestCase):

	def test_ordenar_puntajes_con_una_lista_vacia(self):
		# Setup
		lista_puntaje = []
		resultado_esperado = []

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_ordenar_puntajes_con_una_lista_ordenada_por_puntajes_no_modifica_nada(self):
		# Setup
		lista_puntaje = [
			{'nombre': 'usuario1', 'puntaje': 5}, 
			{'nombre': 'usuario2', 'puntaje': 3}, 
			{'nombre': 'usuario3', 'puntaje': 1}, 
		]
		resultado_esperado = [
			{'nombre': 'usuario1', 'puntaje': 5}, 
			{'nombre': 'usuario2', 'puntaje': 3}, 
			{'nombre': 'usuario3', 'puntaje': 1}, 
		]

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_ordenar_puntajes_con_una_lista_ordenada_por_usuarios_no_modifica_nada(self):
		# Setup
		lista_puntaje = [
			{'nombre': 'usuario1', 'puntaje': 5}, 
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario3', 'puntaje': 5}, 
		]
		resultado_esperado = [
			{'nombre': 'usuario1', 'puntaje': 5}, 
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario3', 'puntaje': 5}, 
		]

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_ordenar_puntajes_con_una_lista_ordenada_por_puntajes_y_usuarios_no_modifica_nada(self):
		# Setup
		lista_puntaje = [
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario1', 'puntaje': 3}, 
			{'nombre': 'usuario3', 'puntaje': 3}, 
		]
		resultado_esperado = [
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario1', 'puntaje': 3}, 
			{'nombre': 'usuario3', 'puntaje': 3}, 
		]

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)


	def test_ordenar_puntajes_con_una_lista_desordenada_por_usuarios_retorna_lista_ordenada(self):
		# Setup
		lista_puntaje = [
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario3', 'puntaje': 5}, 
			{'nombre': 'usuario1', 'puntaje': 5}, 
		]
		resultado_esperado = [
			{'nombre': 'usuario1', 'puntaje': 5}, 
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario3', 'puntaje': 5}, 
		]

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_ordenar_puntajes_con_una_lista_desordenada_por_puntajes_y_usuarios_retorna_lista_ordenada(self):
		# Setup
		lista_puntaje = [
			{'nombre': 'usuario1', 'puntaje': 3}, 
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario3', 'puntaje': 3}, 
		]
		resultado_esperado = [
			{'nombre': 'usuario2', 'puntaje': 5}, 
			{'nombre': 'usuario1', 'puntaje': 3}, 
			{'nombre': 'usuario3', 'puntaje': 3}, 
		]

		# Exercise
		resultado = ordenar_puntajes(lista_puntaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)


