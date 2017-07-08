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

	def test_directo(self)
		self.assertEqual(ArrayFichas().eje(),10)
		
if __name__ == '__main__':
	unittest.main()
