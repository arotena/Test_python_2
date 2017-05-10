#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd","r");
lineas = fd.readlines()
fd.close()

for linea in lineas:
    if not linea:
        break
    corte = linea.split(':')
    login = corte[0] 
    shell = corte[-1]
    print login, shell[:-1]

def factorial(n):
    return 1 if n < 1 else n * factorial(n-1)
def suma (c,p):
	return c + p
def resta(c,j):
	return c - j

	#jhedhgdchj
class Test_EJER(unittest.TestCase):
	def test_sa(self):
        self.assertEqual(factorial(1),1)#aaaaaa
