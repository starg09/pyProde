#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from prode import parsear_linea_prode


class TestParsearLineasFixture(unittest.TestCase):

	def test_parsear_linea_prode_retorna_un_diccionario_vacio_cuando_le_pasan_una_linea_vacia(self):
		# Setup
		linea = ''
		resultado_esperado = {}

		# Exercise
		resultado = parsear_linea_prode(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)
	
	def test_parsear_linea_prode_parsea_bien_la_primer_linea(self):
		# Setup
		linea = '1,0,0'
		resultado_esperado = {
			'numero_partido': 1,
			'goles_local': 0,
			'goles_visitante': 0
		}

		# Exercise
		resultado = parsear_linea_prode(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)
	
	def test_parsear_linea_prode_ignora_el_comentario_despues_del_numeral(self):
		# Setup
		linea = '1,0,0   # Chile vs Ecuador'
		resultado_esperado = {
			'numero_partido': 1,
			'goles_local': 0,
			'goles_visitante': 0
		}

		# Exercise
		resultado = parsear_linea_prode(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)
	
	def test_parsear_linea_prode_ignora_el_enter_al_final_de_la_linea(self):
		# Setup
		linea = '1,0,0   # Chile vs Ecuador\n'
		resultado_esperado = {
			'numero_partido': 1,
			'goles_local': 0,
			'goles_visitante': 0
		}

		# Exercise
		resultado = parsear_linea_prode(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

