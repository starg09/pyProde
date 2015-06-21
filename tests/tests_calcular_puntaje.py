#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from utils import calcular_puntaje


class TestCalcularPuntajesGanaLocal(unittest.TestCase):

	def test_calcular_puntaje_pronostico_exacto_saca_5_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 1
			Goles visitante: 1
			Diferencia de goles: 1
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		puntaje_esperado = 5

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_goles_local_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 1
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 3,
			'goles_visitante': 0
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_goles_visitantes_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 1
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 4,
			'goles_visitante': 2
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_diferencia_goles_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 1
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 1
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_solo_lev_saca_2_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 4,
			'goles_visitante': 0
		}
		puntaje_esperado = 2

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_solo_goles_locales_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 1
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 3,
			'goles_visitante': 3
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_solo_goles_visitantes_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 1
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 1,
			'goles_visitante': 2
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_todo_mal_saca_0_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		puntaje_esperado = 0

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)


class TestCalcularPuntajesEmpate(unittest.TestCase):

	def test_calcular_puntaje_pronostico_exacto_saca_5_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 1
			Goles visitante: 1
			Diferencia de goles: 1

			Si acierta los goles del local y la diferencia, si o si 
			tiene que acertar lo goles del visitante.
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		puntaje_esperado = 5

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_diferencia_goles_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 1

			Si acierta el empate, si o si acierta la diferencia, que es 0.
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 1,
			'goles_visitante': 1
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_solo_goles_locales_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 1
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 0
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_solo_goles_visitantes_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 1
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 1,
			'goles_visitante': 2
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_todo_mal_saca_0_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 2
		}
		pronostico = {
			'goles_local': 1,
			'goles_visitante': 3
		}
		puntaje_esperado = 0

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)


class TestCalcularPuntajesGanaVisitante(unittest.TestCase):

	def test_calcular_puntaje_pronostico_exacto_saca_5_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 1
			Goles visitante: 1
			Diferencia de goles: 1
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		puntaje_esperado = 5

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_goles_visitante_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 1
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 0,
			'goles_visitante': 3
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_goles_local_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 1
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 4
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_diferencia_goles_saca_3_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 1
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 1,
			'goles_visitante': 2
		}
		puntaje_esperado = 3

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_solo_lev_saca_2_pts(self):
		""" Local, empate o visitante: 2
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 0,
			'goles_visitante': 4
		}
		puntaje_esperado = 2

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_solo_goles_visitantes_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 1
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 3,
			'goles_visitante': 3
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_solo_goles_local_saca_1_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 1 
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 2,
			'goles_visitante': 1
		}
		puntaje_esperado = 1

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

	def test_calcular_puntaje_partido_todo_mal_saca_0_pts(self):
		""" Local, empate o visitante: 0
			Goles local: 0
			Goles visitante: 0
			Diferencia de goles: 0
		"""
		# Setup
		resultado = {
			'goles_local': 2,
			'goles_visitante': 3
		}
		pronostico = {
			'goles_local': 3,
			'goles_visitante': 2
		}
		puntaje_esperado = 0

		# Exercise
		resultado = calcular_puntaje(resultado, pronostico)

		# Verify
		self.assertEquals(resultado, puntaje_esperado)

