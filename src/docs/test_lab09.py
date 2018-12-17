#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 10 informatica@sefa 2017/2018

"""

import importlib
import unittest
import sys
import os

ex_name      ='lab09'
ex_functions =['simple_query','plot_query'] 

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


from pprint import pformat

class TestLab09SQL(unittest.TestCase):

    def test_plot(self):
        test_fname='lab09test.png'
        try:
            os.remove(test_fname)
        except FileNotFoundError:
            pass
        plot_query(test_fname)
        self.assertTrue( os.path.isfile(test_fname) )
#        os.remove(test_fname)
    
    def assertQueryEqual(self,tables,columns,expected):

        result=simple_query(tables,columns)
        result=sorted(result)
        expected=sorted(expected)
      
        messaggio = '''
TEST FAIL> La query costruita è

select {1} from {0}

           e produce
{3}

           quando invece dovrebbe produrre:

{2}
'''
        messaggio = messaggio.format(tables,columns,pformat(expected),pformat(result))
        self.assertSequenceEqual(expected,result,msg=messaggio)

    def test_combustibili(self):
        self.assertQueryEqual('Combustibili','Descrizione_Combustibile',
                              [('Benzina',),('Gasolio',),('Metano',),('GPL',)])
        
    def test_modelli(self):
        self.assertQueryEqual('Modelli','Nome_Modello', [('Brava',),
                                                         ('Civic',),
                                                         ('Clio',),
                                                         ('Corolla',),
                                                         ('Coupè',),
                                                         ('Ducato',),
                                                         ('Golf',),
                                                         ('Laguna',),
                                                         ('Megane',),
                                                         ('Mondeo',),
                                                         ('Panda',),
                                                         ('Seicento',),
                                                         ('V-10',),
                                                         ('Vespa',)])

    def test_numproprietari(self):
        result=simple_query('Proprietari','Nome,Cognome')
        self.assertEqual(len(result),7)
    
if __name__ == '__main__':
    unittest.main()
                              
