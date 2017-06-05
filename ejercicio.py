#!/usr/bin/python
# -*- coding: utf-8 -*-

def multi(n,p):
	return n*p
def division(n,p):
	return n/p
def factorial(n):
    	return 1 if n < 1 else n * factorial(n-1)
def suma (c,p):
	return c + p
def resta(c,j):
	return c - j
def igual():
	return '='

	#jhedhgdchj
class Test_EJER(unittest.TestCase):
	def test_factorial_1(self):
        self.assertEqual(factorial(1),1)#de1
	def test_factorial_2(self):
	self.assertEqual(factorial(2),2)#de2
	def test_suma(self):
	self.assertEqual(suma(2,2),4)
