#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from StringIO import StringIO
from fixture import importar_fixture


class TestImportarFixture(unittest.TestCase):

	def test_archivo_vacio_retorna_fixture_vacio(self):
		# Setup
		archivo = StringIO()
		resultado_esperado = []

		# Exercise
		resultado = importar_fixture(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_archivo_con_un_partido_lo_parsea_bien(self):
		# Setup
		archivo = StringIO('1,11,6,18,30,Grupo,Chile,Ecuador')
		resultado_esperado = [{
			'numero_partido': 1,
			'dia': 11,
			'mes': 6,
			'hora': 18,
			'minutos': 30,
			'instancia': 'Grupo',
			'local': 'Chile',
			'visitante': 'Ecuador',
			'jugado': False,
			'goles_local': 0,
			'goles_visitante': 0
		}]

		# Exercise
		resultado = importar_fixture(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_archivo_completo_lo_parsea_bien(self):
		# Setup
		contenido_del_archivo = '''1,11,6,18,30,Grupo,Chile,Ecuador
2,12,6,18,30,Grupo,México,Bolivia
3,13,6,14,0,Grupo,Uruguay,Jamaica
4,13,6,16,30,Grupo,Argentina,Paraguay
5,14,6,14,0,Grupo,Colombia,Venezuela
6,14,6,16,30,Grupo,Brasil,Perú
7,15,6,16,0,Grupo,Ecuador,Bolivia
8,15,6,18,30,Grupo,Chile,México
9,16,6,16,0,Grupo,Paraguay,Jamaica
10,16,6,18,30,Grupo,Argentina,Uruguay
11,17,6,18,30,Grupo,Brasil,Colombia
12,18,6,18,30,Grupo,Perú,Venezuela
13,19,6,16,0,Grupo,México,Ecuador
14,19,6,18,30,Grupo,Chile,Bolivia
15,20,6,14,0,Grupo,Uruguay,Paraguay
16,20,6,16,30,Grupo,Argentina,Jamaica
17,21,6,14,0,Grupo,Colombia,Perú
18,21,6,16,30,Grupo,Brasil,Venezuela
19,24,6,18,30,Cuartos de final,1A,1M3
20,25,6,18,30,Cuartos de final,2A,2C
21,26,6,18,30,Cuartos de final,1B,2M3
22,27,6,16,30,Cuartos de final,1C,2B
23,29,6,18,30,Semifinal,G19,G20
24,30,6,18,30,Semifinal,G21,G22
25,3,7,18,30,Tercer y Cuarto puesto,P23,P24
26,4,7,15,0,Final,G23,G24
'''
		archivo = StringIO(contenido_del_archivo)
		self.maxDiff = None
		resultado_esperado = [
			{
				'numero_partido': 1,
				'dia': 11,
				'mes': 6,
				'hora': 18,
				'minutos': 30,
				'instancia': 'Grupo',
				'local': 'Chile',
				'visitante': 'Ecuador',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 12,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'M\xc3\xa9xico',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 2,
				'visitante': 'Bolivia',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 13,
				'hora': 14,
				'instancia': 'Grupo',
				'local': 'Uruguay',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 3,
				'visitante': 'Jamaica',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 13,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Argentina',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 4,
				'visitante': 'Paraguay',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 14,
				'hora': 14,
				'instancia': 'Grupo',
				'local': 'Colombia',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 5,
				'visitante': 'Venezuela',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 14,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Brasil',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 6,
				'visitante': 'Per\xc3\xba',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 15,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Ecuador',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 7,
				'visitante': 'Bolivia',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 15,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'Chile',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 8,
				'visitante': 'M\xc3\xa9xico',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 16,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Paraguay',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 9,
				'visitante': 'Jamaica',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 16,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'Argentina',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 10,
				'visitante': 'Uruguay',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 17,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'Brasil',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 11,
				'visitante': 'Colombia',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 18,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'Per\xc3\xba',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 12,
				'visitante': 'Venezuela',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 19,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'M\xc3\xa9xico',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 13,
				'visitante': 'Ecuador',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 19,
				'hora': 18,
				'instancia': 'Grupo',
				'local': 'Chile',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 14,
				'visitante': 'Bolivia',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 20,
				'hora': 14,
				'instancia': 'Grupo',
				'local': 'Uruguay',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 15,
				'visitante': 'Paraguay',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 20,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Argentina',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 16,
				'visitante': 'Jamaica',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 21,
				'hora': 14,
				'instancia': 'Grupo',
				'local': 'Colombia',
				'mes': 6,
				'minutos': 0,
				'numero_partido': 17,
				'visitante': 'Per\xc3\xba',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 21,
				'hora': 16,
				'instancia': 'Grupo',
				'local': 'Brasil',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 18,
				'visitante': 'Venezuela',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 24,
				'hora': 18,
				'instancia': 'Cuartos de final',
				'local': '1A',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 19,
				'visitante': '1M3',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 25,
				'hora': 18,
				'instancia': 'Cuartos de final',
				'local': '2A',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 20,
				'visitante': '2C',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 26,
				'hora': 18,
				'instancia': 'Cuartos de final',
				'local': '1B',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 21,
				'visitante': '2M3',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 27,
				'hora': 16,
				'instancia': 'Cuartos de final',
				'local': '1C',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 22,
				'visitante': '2B',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 29,
				'hora': 18,
				'instancia': 'Semifinal',
				'local': 'G19',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 23,
				'visitante': 'G20',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 30,
				'hora': 18,
				'instancia': 'Semifinal',
				'local': 'G21',
				'mes': 6,
				'minutos': 30,
				'numero_partido': 24,
				'visitante': 'G22',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 3,
				'hora': 18,
				'instancia': 'Tercer y Cuarto puesto',
				'local': 'P23',
				'mes': 7,
				'minutos': 30,
				'numero_partido': 25,
				'visitante': 'P24',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			},
			{
				'dia': 4,
				'hora': 15,
				'instancia': 'Final',
				'local': 'G23',
				'mes': 7,
				'minutos': 0,
				'numero_partido': 26,
				'visitante': 'G24',
				'jugado': False,
				'goles_local': 0,
				'goles_visitante': 0
			}
		]

		# Exercise
		resultado = importar_fixture(archivo)

		# Verify
		self.assertEquals(resultado, resultado_esperado)
