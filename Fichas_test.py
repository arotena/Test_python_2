#import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
#sys.path.append('../Test_python')
from Fichas import Fichas
from Array_Fichas import ArrayFichas
import unittest

class CarcassoneTest(unittest.TestCase):
	def test_first_ficha(self):
		f = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],True)
		expected="""A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
A1 A1 A1
"""
		self.assertEqual(expected,f.imprimir())

	def test_long_array(self):

		self.assertEqual(len(ArrayFichas().saco),71)

	def test_eliminar_ficha_saco(self):
		ficha = ArrayFichas().sacar_ficha(26)
		expected = len(ArrayFichas().saco)-1
		ArrayFichas().eliminar_ficha(ficha)
		self.assertEqual(len(ArrayFichas().saco),expected)

if __name__ == '__main__':
	unittest.main()
