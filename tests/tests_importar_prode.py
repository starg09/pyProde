#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from StringIO import StringIO
from prode import importar_prode


class TestImportarProde(unittest.TestCase):

	def test_importar_prode_con_archivo_vacio_retorna_fixture_vacio(self):
		# Setup
		archivo = StringIO()
		resultado_esperado = []

		# Exercise
		resultado = importar_prode(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_importar_prode_a_un_archivo_con_un_partido_lo_parsea_bien(self):
		# Setup
		archivo = StringIO('1,2,3   # Chile vs Ecuador')
		resultado_esperado = [{
			'numero_partido': 1,
			'goles_local': 2,
			'goles_visitante': 3
		}]

		# Exercise
		resultado = importar_prode(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_importar_prode_a_un_archivo_completo_lo_parsea_bien(self):
		# Setup
		contenido_del_archivo = '''1,2,0   # Chile vs Ecuador
2,1,1   # México vs Bolivia
3,3,0   # Uruguay vs Jamaica
4,2,1   # Argentina vs Paraguay
5,2,0   # Colombia vs Venezuela
6,4,1   # Brasil vs Perú
7,0,1   # Ecuador vs Bolivia
8,2,1   # Chile vs México
9,2,0   # Paraguay vs Jamaica
10,2,2  # Argentina vs Uruguay
11,2,1  # Brasil vs Colombia
12,0,1  # Perú vs Venezuela
13,1,0  # México vs Ecuador
14,2,0  # Chile vs Bolivia
15,1,0  # Uruguay vs Paraguay
16,3,0  # Argentina vs Jamaica
17,2,0  # Colombia vs Perú
18,3,0  # Brasil vs Venezuela
19,1,0  # 1A vs 1M3
20,0,1  # 2A vs 2C
21,1,0  # 1B vs 2M3
22,0,1  # 1C vs 2B
23,1,0  # G19 vs G20
24,0,1  # G21 vs G22
25,1,0  # P23 vs P24
26,0,1  # G23 vs G24
'''
		archivo = StringIO(contenido_del_archivo)
		self.maxDiff = None
		resultado_esperado = [
			{'numero_partido': 1, 'goles_local': 2, 'goles_visitante': 0},
			{'numero_partido': 2, 'goles_local': 1, 'goles_visitante': 1},
			{'numero_partido': 3, 'goles_local': 3, 'goles_visitante': 0},
			{'numero_partido': 4, 'goles_local': 2, 'goles_visitante': 1},
			{'numero_partido': 5, 'goles_local': 2, 'goles_visitante': 0},
			{'numero_partido': 6, 'goles_local': 4, 'goles_visitante': 1},
			{'numero_partido': 7, 'goles_local': 0, 'goles_visitante': 1},
			{'numero_partido': 8, 'goles_local': 2, 'goles_visitante': 1},
			{'numero_partido': 9, 'goles_local': 2, 'goles_visitante': 0},
			{'numero_partido': 10, 'goles_local': 2, 'goles_visitante': 2},
			{'numero_partido': 11, 'goles_local': 2, 'goles_visitante': 1},
			{'numero_partido': 12, 'goles_local': 0, 'goles_visitante': 1},
			{'numero_partido': 13, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 14, 'goles_local': 2, 'goles_visitante': 0},
			{'numero_partido': 15, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 16, 'goles_local': 3, 'goles_visitante': 0},
			{'numero_partido': 17, 'goles_local': 2, 'goles_visitante': 0},
			{'numero_partido': 18, 'goles_local': 3, 'goles_visitante': 0},
			{'numero_partido': 19, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 20, 'goles_local': 0, 'goles_visitante': 1},
			{'numero_partido': 21, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 22, 'goles_local': 0, 'goles_visitante': 1},
			{'numero_partido': 23, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 24, 'goles_local': 0, 'goles_visitante': 1},
			{'numero_partido': 25, 'goles_local': 1, 'goles_visitante': 0},
			{'numero_partido': 26, 'goles_local': 0, 'goles_visitante': 1}
		]


		# Exercise
		resultado = importar_prode(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)
