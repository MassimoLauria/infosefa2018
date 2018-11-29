#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 07 informatica@sefa 2018/2019


Es. 12

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

Es. 13

   : plot_dati(test,nomefile)

   analizzare la stringa di testo come fatto nell'esercizio
   precedente, ma invece di produrre le coppie di valori in output,
   interpretate il primi valori di ogni riga come i valori delle
   x e quelli della seconda riga come i valori della funzione f(x)
   e fate il grafico della funzione, salvando l'immagine nel file
   'nomefile.


Es.14

   : frequenze(testo,lista_parole)
 
   La funzione deve prendere in input una stringa e deve restituire
   una lista della stessa lunghezza di 'lista_parole', nella posizione
   i-esima della lista restituita ci deve essere il numero di
   occorrenze della parola i-esima in lista_parole.

   - 'Casa' , 'caSa', 'casa' sono la stessa parola

"""

import importlib
import unittest
import sys
import os

ex_name      ='lab07'
ex_functions =['parse_dati','plot_dati','frequenze'] 

# Importa le soluzioni degli esercizi
lab=None
try:
    lab=importlib.__import__(ex_name)
except Exception:
    msg="""ERROR: Problema col file {0}.py. Forse
    -- forse non è presente in questa cartella
    -- oppure contiene errori che non lo rendono eseguibile
    
    Prova ad eseguire '$ python3 {0}.py'""".format(ex_name)
    print(msg,file=sys.stderr)
    sys.exit(-1)

f_objects={}
for f_name in ex_functions:
    try:
        f_object = lab.__dict__[f_name]
        f_objects[f_name] = f_object
    except KeyError:
        msg="ESERCIZIO MANCANTE: Funzione {1} non presente in file {0}.py".format(ex_name,f_name)
        print(msg,file=sys.stderr)

# Caricale nel namespace
globals().update(f_objects)

class TestLab07ParseDati(unittest.TestCase):

    def _verify(self,data,expected):
        result   = parse_dati(data)
        messaggio = "\nTEST FAIL> parse_dati su input {}\n" + \
                    "dovrebbe produrre: '{}',\n invece produce:    '{}'"
        messaggio = messaggio.format(repr(data),expected,result)
        self.assertEqual(expected,result,msg=messaggio)

    def _verify_raise(self,data,error,reason):
        messaggio = "\nTEST FAIL> parse_dati su input {}\n" + \
                    "dovrebbe sollevare '{}' perché '{}'"
        messaggio = messaggio.format(repr(data),error,reason)
        with self.assertRaises(error,msg=messaggio):
            parse_dati(data)

    
    def test_vuota(self):
        data=''''''
        self._verify(data,[])

    def test_invalid(self):
        data='''
        1 : 4
        1 : 4 : 3
        '''
        self._verify_raise(data,ValueError,"la seconda riga ha tre campi invece di due.")

    def test_one(self):
        data='''
        1.0 : 3.0
        '''
        self._verify(data,[(1.0,3.0)])
        
    def test_two(self):
        data='''
        1.0 : 3.0

        1.5 : 4.0
        '''
        self._verify(data,[(1.0,3.0),(1.5,4.0)])

    def test_three(self):
        data='''
        1.0 : 3.0
        1.5 : 4.0
        2.0 : 2.1
        '''
        self._verify(data,[(1.0,3.0),(1.5,4.0),(2.0,2.1)])

    def test_random(self):
        import random
        randomdata = [ ]
        for _ in range(100):
            x=round(random.random(),3)
            y=round(random.random(),3)
            randomdata.append( (x,y) )
        testo='\n'.join(['{} : {}'.format(x,y) for x,y in randomdata])
        self._verify(testo,randomdata)

class TestLab07PlotDati(unittest.TestCase):

    def _verify_raise(self,data,error,reason):
        messaggio = "\nTEST FAIL> plot_dati su input {}\n" + \
                    "dovrebbe sollevare '{}' perché '{}'"
        messaggio = messaggio.format(repr(data),error,reason)
        with self.assertRaises(error,msg=messaggio):
            plot_dati(data)

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

class TestLab07Frequenze(unittest.TestCase):

    def _verify(self,data,parole,expected):
        result   = frequenze(data,parole)
        messaggio = "\nTEST FAIL> Le frequenze delle parole: {1} in {0}\n" + \
                    "sono '{2}',\n e invece il programma produce '{3}'"
        messaggio = messaggio.format(data,parole,expected,result)
        self.assertEqual(expected,result,msg=messaggio)


    def test_legna(self):
        testo="Quanta legna taglia un taglia-legna, se vuol tagliare legna."
        chiavi=['legna','taglia','castoro','quanta']
        self._verify(testo,chiavi,[3,2,0,1])

    def test_maiuscole(self):
        testo="casa Casa cAsA cASA"
        chiavi=['Casa','lavoro']
        self._verify(testo,chiavi,[4,0])

    def test_attaccate(self):
        testo="casa casacasa cASA"
        chiavi=['Casa']
        self._verify(testo,chiavi,[2])

    def test_punteggiatura(self):
        testo="casa, casa; casa ca:sa"
        chiavi=['Casa']
        self._verify(testo,chiavi,[3])

        
if __name__ == '__main__':
    unittest.main()
    
