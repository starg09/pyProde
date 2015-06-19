#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from utils import quitar_comentarios


class TestQuitarComentarios(unittest.TestCase):

	def test_quitar_comentarios_solo_hace_strip_de_un_string_sin_numeral(self):
		# Setup
		mensaje = '1,0,0'
		resultado_esperado = '1,0,0'

		# Exercise
		resultado = quitar_comentarios(mensaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_quitar_comentarios_quita_lo_que_esta_a_partir_del_numeral(self):
		# Setup
		mensaje = '1,0,0# Chile vs Ecuador'
		resultado_esperado = '1,0,0'

		# Exercise
		resultado = quitar_comentarios(mensaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_quitar_comentarios_quita_espacios_previos_al_numeral(self):
		# Setup
		mensaje = '1,0,0   # Chile vs Ecuador'
		resultado_esperado = '1,0,0'

		# Exercise
		resultado = quitar_comentarios(mensaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)

	def test_quitar_comentarios_elimina_todo_desde_el_primer_numeral(self):
		# Setup
		mensaje = '1,0,0# Chile # Ecuador'
		resultado_esperado = '1,0,0'

		# Exercise
		resultado = quitar_comentarios(mensaje)

		# Verify
		self.assertEquals(resultado, resultado_esperado)


if __name__ == "__main__":
    unittest.main()