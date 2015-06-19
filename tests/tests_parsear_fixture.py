#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from fixture import parsear_linea_fixture


class TestParsearLineasFixture(unittest.TestCase):

	def test_parsear_linea_fixture_retorna_un_diccionario_vacio_cuando_le_pasan_una_linea_vacia(self):
		# Setup
		linea = ''
		resultado_esperado = {}

		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_parsea_partido_de_grupo_correctamente(self):
		# Setup
		linea = '1,11,6,18,30,Grupo,Chile,Ecuador'
		resultado_esperado = {
			'numero_partido': 1,
			'dia': 11,
			'mes': 6,
			'hora': 18,
			'minutos': 30,
			'instancia': 'Grupo',
			'local': 'Chile',
			'visitante': 'Ecuador'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_parsea_semifinal_correctamente(self):
		# Setup
		linea = '23,29,6,18,30,Semifinal,G19,G20'
		resultado_esperado = {
			'numero_partido': 23,
			'dia': 29,
			'mes': 6,
			'hora': 18,
			'minutos': 30,
			'instancia': 'Semifinal',
			'local': 'G19',
			'visitante': 'G20'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_parsea_tercer_correctamente(self):
		# Setup
		linea = '25,3,7,18,30,Tercer y Cuarto puesto,P23,P24'
		resultado_esperado = {
			'numero_partido': 25,
			'dia': 3,
			'mes': 7,
			'hora': 18,
			'minutos': 30,
			'instancia': 'Tercer y Cuarto puesto',
			'local': 'P23',
			'visitante': 'P24'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_parsea_con_acento_correctamente(self):
		# Setup
		linea = '13,19,6,16,0,Grupo,México,Ecuador'
		resultado_esperado = {
			'numero_partido': 13,
			'dia': 19,
			'mes': 6,
			'hora': 16,
			'minutos': 0,
			'instancia': 'Grupo',
			'local': 'México',
			'visitante': 'Ecuador'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_parsea_final_correctamente(self):
		# Setup
		linea = '26,4,7,15,0,Final,G23,G24'
		resultado_esperado = {
			'numero_partido': 26,
			'dia': 4,
			'mes': 7,
			'hora': 15,
			'minutos': 0,
			'instancia': 'Final',
			'local': 'G23',
			'visitante': 'G24'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_parsear_linea_fixture_ignora_el_enter_al_final_de_la_linea(self):
		# Setup
		linea = '1,11,6,18,30,Grupo,Chile,Ecuador\n'
		resultado_esperado = {
			'numero_partido': 1,
			'dia': 11,
			'mes': 6,
			'hora': 18,
			'minutos': 30,
			'instancia': 'Grupo',
			'local': 'Chile',
			'visitante': 'Ecuador'
		}


		# Exercise
		resultado = parsear_linea_fixture(linea)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

