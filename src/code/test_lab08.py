#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 08 informatica@sefa 2017/2018


Es. 14

   : parse_dati(testo)

   la funzione ha in input una stringa di testo, che è costituita da
   diverse righe. Ogni riga contiene 2 valori numerici float, separati
   da ':'

   x0 : y0
   x1 : y1
   x2 : y2
   ...

   La funzione deve produrre una lista di triple [(x0,y0),... ] che
   rappresenta le coppie contenute nel file.

   - ignorate le righe vuote
   - sollevate l'eccezione ValueError se esiste una riga mal formattata   

Es. 15

   : plot_dati(test,nomefile)

   analizzare la stringa di testo come fatto nell'esercizio
   precedente, ma invece di produrre le coppie di valori in output,
   interpretate il primi valori di ogni riga come i valori delle
   x e quelli della seconda riga come i valori della funzione f(x)
   e fate il grafico della funzione, salvando l'immagine nel file
   'nomefile.


Es.16 

   : frequenze(testo,lista_parole)
 
   La funzione deve prendere in input una stringa e deve restituire
   una lista della stessa lunghezza di 'lista_parole', nella posizione
   i-esima della lista restituita ci deve essere il numero di
   occorrenze della parola i-esima in lista_parole.

   - 'Casa' , 'caSa', 'casa' sono la stessa parola

"""

from lab08 import parse_dati,plot_dati,frequenze
import unittest
import os

class TestLab08ParseDati(unittest.TestCase):

    def test_vuota(self):
        data=''''''
        self.assertEqual(parse_dati(data),[])

    def test_invalid(self):
        data='''
        1 : 4
        1 : 4 : 3
        '''
        self.assertRaises(ValueError,parse_dati,data)

    def test_one(self):
        data='''
        1.0 : 3.0
        '''
        self.assertEqual(parse_dati(data),[(1.0,3.0)])
        
    def test_two(self):
        data='''
        1.0 : 3.0
        1.5 : 4.0
        '''
        self.assertEqual(parse_dati(data),[(1.0,3.0),(1.5,4.0)])

    def test_three(self):
        data='''
        1.0 : 3.0
        1.5 : 4.0
        2.0 : 2.1
        '''
        self.assertEqual(parse_dati(data),[(1.0,3.0),(1.5,4.0),(2.0,2.1)])

    def test_random(self):
        import random
        randomdata = [ ]
        for _ in range(100):
            x=round(random.random(),3)
            y=round(random.random(),3)
            randomdata.append( (x,y) )
        testo='\n'.join(['{} : {}'.format(x,y) for x,y in randomdata])
        self.assertEqual(parse_dati(testo),randomdata)

class TestLab08PlotDati(unittest.TestCase):

    def _plot_test(self,data):
        plot_dati(data,'temp.png')
        os.remove('temp.png')
    
    def test_vuota(self):
        data=''''''
        self._plot_test(data)
        
    def test_invalid(self):
        data='''
        1 : 4
        1 : 4 : 3
        '''
        self.assertRaises(ValueError,parse_dati,data)

    def test_one(self):
        data='''
        1.0 : 3.0
        '''
        self._plot_test(data)
        
    def test_two(self):
        data='''
        1.0 : 3.0
        1.5 : 4.0
        '''
        self._plot_test(data)

    def test_three(self):
        data='''
        1.0 : 3.0
        1.5 : 4.0
        2.0 : 2.1
        '''
        self._plot_test(data)

    def test_random(self):
        import random
        randomdata = [ ]
        for _ in range(100):
            x=round(random.random(),3)
            y=round(random.random(),3)
            randomdata.append( (x,y) )
        testo='\n'.join(['{} : {}'.format(x,y) for x,y in randomdata])
        self._plot_test(testo)

class TestLab08Frequenze(unittest.TestCase):


    def test_legna(self):
        res=frequenze("Quanta legna taglia un taglia-legna, se vuol tagliare legna",
                      ['legna','taglia','castoro'])
        self.assertEqual(res,[3,2,0])

    def test_maiuscole(self):
        res=frequenze("casa Casa cAsA cASA",
                      ['Casa','lavoro'])
        self.assertEqual(res,[4,0])

    def test_attaccate(self):
        res=frequenze("casa casacasa cASA",
                      ['Casa'])
        self.assertEqual(res,[2])

    def test_punteggiatura(self):
        res=frequenze("casa, casa; casa ca:sa",
                      ['Casa'])
        self.assertEqual(res,[3])

        
if __name__ == '__main__':
    unittest.main()
    
