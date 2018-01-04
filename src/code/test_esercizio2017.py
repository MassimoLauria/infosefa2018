#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test preliminari per l'homework di Informatica@SEFA 2017/2018

Questo file contiene i test preliminari per il compito di
programmazione del corso di Informatica@SEFA dell'anno 2017/2018
disponibile all'indirizzo

   http://massimolauria.net/courses/infosefa2017/docs/esercizio2017.pdf

Questi test verificano che le soluzioni del compito siano state
impostate correttamente, ma il fatto di passare questi test non
garantisce in alcun modo che le soluzioni siano
effettivamente corrette.

"""

import unittest
import sys
import shutil
import os
import os.path
from math import sin,cos,trunc,ceil,floor
from random import random
from matplotlib.pyplot import clf
from subprocess import call


# Verifica che i file di dati siano presenti
dataset=['alice.txt',
         'chinook_db.sqlite',
         'registro_automobilistico_db.sqlite']


for fn in dataset:
    file_missing=False
    try:
        f=open(fn,'r')
    except FileNotFoundError:
        file_missing = True
        print("Manca il file {}".format(fn))
if file_missing:
    print("Non posso eseguire i test: mancano alcuni file di dati.")
    sys.exit(-1)

# Verifica che il file dell'esercizio sia presente.
try:
    import esercizio2017
except ImportError:
    print("Non posso eseguire i test: file esercizio2017.py assente")
    sys.exit(-1)


# Parte 1 presente
try:
    from esercizio2017 import spacchetta
except ImportError:
    print("Non posso eseguire i test: parte 1 incompleta")
    sys.exit(-1)

# Parte 2 presente
try:
    from esercizio2017 import ismatrix,size,zeromatrix,transpose,matrixsum,scale,mult
except ImportError:
    print("Non posso eseguire i test: parte 2 incompleta")
    sys.exit(-1)

# Parte 3 presente
try:
    from esercizio2017 import conteggiofile,conteggiotesto
except ImportError:
    print("Non posso eseguire i test: parte 3 incompleta")
    sys.exit(-1)

# Parte 4 presente
try:
    from esercizio2017 import produciplot
except ImportError:
    print("Non posso eseguire i test: parte 4 incompleta")
    sys.exit(-1)

# Parte 5 presente
try:
    from esercizio2017 import query1,query2,query3
except ImportError:
    print("Non posso eseguire i test: parte 5 incompleta")
    sys.exit(-1)


# Test Parte 1
class TestParte1(unittest.TestCase):

    def test_empty(self):
        self.assertRaises(ValueError,spacchetta,[])
        
    def test_different_size(self):
        self.assertRaises(ValueError,spacchetta,[(1,'a'),(2,'b','invalid')])

    def test_ex1(self):
        result=spacchetta([(1,'a'),(4,'b'),('x','ff')])
        self.assertEqual(result,[[1, 4, 'x'], ['a', 'b', 'ff']])
        
    def test_ex2(self):
        result=spacchetta([(1,'a','casa'),('foglia',4,'b')])
        self.assertEqual(result,[[1, 'foglia'], ['a', 4], ['casa', 'b']])
        
# Test Parte 2
class TestParte2(unittest.TestCase):
    
    def test_zerocols(self):
        M=[[],[],[]]
        self.assertFalse(ismatrix(M))

    def test_nofloat(self):
        M=[ [1.0,-1.0], [1,-1.2], [0.0,3.2], [-1.5,1.5] ]
        self.assertFalse(ismatrix(M))

    def test_strangesize(self):
        M=[ [1.0,-1.0], [1.0,-1.2,1.5] ]
        self.assertFalse(ismatrix(M))

    def test_transpose_good(self):
        M=zeromatrix(10,4)
        T=transpose(M)
        self.assertEqual(size(T),(4,10))

    def test_size_bad(self):
        M=[ [1.0,-1.0], [1,-1.2], [0.0,3.2], [-1.5,1.5] ]
        self.assertRaises(ValueError,size,M)

    def test_create_good(self):
        M=zeromatrix(10,4)
        self.assertTrue(ismatrix(M))

    def test_create_size(self):
        M=zeromatrix(10,4)
        self.assertEqual(size(M),(10,4))

    def test_scale_good(self):
        M=[[1.0,-1.0]]
        self.assertEqual(scale(2.0,M),[[2.0,-2.0]])

    def test_somma_esempio(self):
        A=[[1.0,-1.0],[1.0, 4.5],[0.5,-1.0]]
        B=[[2.5, 1.0],[2.0,-1.0],[1.0,-1.0]]
        C=[[3.5, 0.0],[3.0, 3.5],[1.5,-2.0]]
        self.assertEqual(matrixsum(A,B),C)

    def test_mult_esempio(self):
        A=[[1.0, -1.0]]
        B=[[2.5],[1.0]]
        C=[[1.5]]
        self.assertEqual(mult(A,B),C)
        
# Test Parte 3
class TestParte3(unittest.TestCase):

    def test_ex1(self):
        res=conteggiotesto("Quanta legna taglia un taglia-legna, se vuol tagliare legna",5)
        self.assertEqual(res,1)

    def test_ex2(self):
        res=conteggiotesto("Quanta legna taglia un taglia-legna, se vuol tagliare legna",6)
        self.assertEqual(res,2)

    def test_attaccate(self):
        res=conteggiotesto("casa cavacasa cA,SA",4)
        self.assertEqual(res,1)

    def test_nofile(self):
        self.assertRaises(FileNotFoundError,conteggiofile,"nonesiste.txt",3)
        
    def test_alice5(self):
        res=conteggiofile('alice.txt',5,encoding='utf-8-sig')
        self.assertEqual(res,480)


# Test Parte 4
class TestParte4(unittest.TestCase):

    def assertFilePresent(self,nome):
        if not os.path.isfile(nome):
            raise AssertionError("Il file {} non è presente.".format(nome))
        
    def test_noise(self):
        def noise(x):
            return random()/5
        produciplot(cos,noise,'plot_esercizio2017.pdf')
        self.assertFilePresent('plot_esercizio2017.pdf')
       
# Test Parte 5
class TestParte5(unittest.TestCase):

    def test_query1empty(self):
        self.assertEqual(query1(0),[])

    def test_query1ex1(self):
        self.assertEqual(query1(3),[('Ford',), ('Honda',)])

    def test_query2format(self):
        res=query2()
        self.assertEqual(len(res[0]),3)

    def test_query3ex1(self):
        self.assertEqual(query3(11,20),[('Led Zeppelin', 14), ('Deep Purple', 11)])

    def test_query3ex2(self):
        self.assertEqual(query3(6,10),[('Metallica', 10), ('U2', 10), ('Ozzy Osbourne', 6)])
        
if __name__ == '__main__':
    unittest.main()


    
