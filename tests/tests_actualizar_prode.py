#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from prode import actualizar_prode


class TestParsearLineasFixture(unittest.TestCase):

	def test_actualizar_prode_con_todas_listas_vacias_da_una_lista_vacia(self):
		# Setup
		prode = []
		fixture = []
		nuevo_prode = []
		resultado_esperado = []

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
	
	def test_actualizar_prode_sin_nuevo_prode_no_se_modifica_el_prode_viejo(self):
		# Setup
		prode = [{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1}]
		fixture = [{'numero_partido': 1, 'jugado': False}]
		nuevo_prode = []
		resultado_esperado = [{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1}]

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
	
	def test_actualizar_prode_nuevo_prode_modifica_prode_anterior_si_no_se_jugo_el_partido(self):
		# Setup
		prode = [{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1}]
		fixture = [{'numero_partido': 1, 'jugado': False}]
		nuevo_prode = [{'numero_partido': 1, 'goles_local': 2, 'goles_visitante': 2}]
		resultado_esperado = [{'numero_partido': 1, 'goles_local': 2, 'goles_visitante': 2}]

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
	
	def test_actualizar_prode_nuevo_prode_no_modifica_prode_anterior_si_se_jugo_el_partido(self):
		# Setup
		prode = [{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1}]
		fixture = [{'numero_partido': 1, 'jugado': True}]
		nuevo_prode = [{'numero_partido': 1, 'goles_local': 2, 'goles_visitante': 2}]
		resultado_esperado = [{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1}]

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
	
	def test_actualizar_prode_considera_si_se_jugo_por_cada_partido(self):
		# Setup
		prode = [
			{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1},
			{'numero_partido': 2, 'goles_local': 3, 'goles_visitante': 1},
			{'numero_partido': 3, 'goles_local': 3, 'goles_visitante': 1},
		]
		fixture = [
			{'numero_partido': 1, 'jugado': True},
			{'numero_partido': 2, 'jugado': False},
			{'numero_partido': 3, 'jugado': True},
		]
		nuevo_prode = [
			{'numero_partido': 1, 'goles_local': 2, 'goles_visitante': 2},
			{'numero_partido': 2, 'goles_local': 2, 'goles_visitante': 2},
			{'numero_partido': 3, 'goles_local': 2, 'goles_visitante': 2},
		]
		resultado_esperado = [
			{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1},  # No se modifico
			{'numero_partido': 2, 'goles_local': 2, 'goles_visitante': 2},  # Si se modifico
			{'numero_partido': 3, 'goles_local': 3, 'goles_visitante': 1},  # No se modifico
		]

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
	
	def test_actualizar_prode_no_requiere_prode_completo(self):
		# Setup
		prode = [
			{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1},
			{'numero_partido': 2, 'goles_local': 3, 'goles_visitante': 1},
			{'numero_partido': 3, 'goles_local': 3, 'goles_visitante': 1},
		]
		fixture = [
			{'numero_partido': 1, 'jugado': True},
			{'numero_partido': 2, 'jugado': False},
			{'numero_partido': 3, 'jugado': True},
		]
		nuevo_prode = [
			{'numero_partido': 2, 'goles_local': 2, 'goles_visitante': 2},
		]
		resultado_esperado = [
			{'numero_partido': 1, 'goles_local': 3, 'goles_visitante': 1},  # No se modifico
			{'numero_partido': 2, 'goles_local': 2, 'goles_visitante': 2},  # Si se modifico
			{'numero_partido': 3, 'goles_local': 3, 'goles_visitante': 1},  # No se modifico
		]

		# Exercise
		prode_actualizado = actualizar_prode(prode, fixture, nuevo_prode)

		# Verify
		self.assertEquals(prode_actualizado, resultado_esperado)
