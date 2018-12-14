#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab XX informatica@sefa 2018/2019

"""
import importlib
import unittest
import sys

ex_name      ='lab03'
ex_functions =['ghms2','decrescente'] 

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




class TestLab03GHMS2(unittest.TestCase):

    def _verify_ghms(self,secondi,text):
        result   = ghms2(secondi)
        messaggio = "\nTEST FAIL> La funzione ghms2({})\n dovrebbe produrre: '{}',\n invece produce:    '{}'".format(secondi,text,result)
        self.assertEqual(text,ghms2(secondi),msg=messaggio)

    def test_examples_cases1(self):
        self._verify_ghms(0,"0 secondi.")

    def test_examples_cases2(self):
        self._verify_ghms(2348,"39 minuti e 8 secondi.")

    def test_examples_cases3(self):
        self._verify_ghms(3840,"1 ora e 4 minuti.")

    def test_examples_cases4(self):
        self._verify_ghms(122456,"1 giorno, 10 ore e 56 secondi.")

    def test_examples_cases5(self):
        self._verify_ghms(60*60*48,"2 giorni.")

    def test_examples_cases6(self):
        self._verify_ghms(60,"1 minuto.")

    def test_examples_cases7(self):
        self._verify_ghms(1,"1 secondo.")

    def test_ghms2_positive(self):
        msg="\nTEST FAIL> ghms2(-3) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            ghms2(-3)


class TestLab03Ordered(unittest.TestCase):
     
    def test_base_zero(self):
        msg="\nTEST FAIL> La lista [1] di un solo elemento è decrescente. Ma hai restituito False."
        self.assertTrue(decrescente([1]),msg=msg)

    def test_base_one(self):
        msg="\nTEST FAIL> La lista [] di zero elementi è decrescente. Ma hai restituito False."
        self.assertTrue(decrescente([]),msg=msg)

    def test_base_zerot(self):
        msg="\nTEST FAIL> La tupla (1,) di un solo elemento è decrescente. Ma hai restituito False."
        self.assertTrue(decrescente((1,)),msg=msg)

    def test_base_onet(self):
        msg="\nTEST FAIL> La tupla () di zero elementi è decrescente. Ma hai restituito False."
        self.assertTrue(decrescente(()),msg=msg)
        

    def test_small1(self):
        testcase=[2,1]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)
    
    def test_small2(self):
        testcase=[1,2]
        expected=False 
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)


    def test_even(self):
        testcase=[1,1,1,1,1]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)


    def test_mixed1(self):
        testcase=[2.0,1]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)

    def test_mixed2(self):
        testcase=[1,2.3]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)

    def test_example1(self):
        testcase=[1,3,1,5,4]
        expected=False
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)

    def test_example2(self):
        testcase=[1,3,1,4,4,1]
        expected=False
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)
    

    def test_example3(self):
        testcase=[5,4,3,2,1,2]
        expected=False
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)


    def test_example4(self):
        testcase=[1,1,1,1,1,1]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)


    def test_example5(self):
        testcase=[7.4, 6, 4.5, 3.1, 2.3, 1.0]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)


    def test_example6(self):
        testcase=[7,6,5,4,4,4,3,2,1]
        expected=True
        
        if expected:
            msg="\nTEST FAIL> La sequenza {} è decrescente, e invece il tuo codice ha restituito False."
        else:
            msg="\nTEST FAIL> La sequenza {} non è decrescente, e invece il tuo codice ha restituito True."
        msg=msg.format(testcase)

        if expected:
            self.assertTrue(decrescente(testcase),msg=msg)
        else:
            self.assertFalse(decrescente(testcase),msg=msg)



    def test_mixed1(self):
        msg="\nTEST FAIL> La lista [1,'ciao'] contiene elementi non confrontabili. Si dovrebbe sollevare un TypeError."
        with self.assertRaises(TypeError,msg=msg):
            decrescente( [1,'ciao'] )

    def test_mixed2(self):
        msg="\nTEST FAIL> La lista ['ciao', 1.2] contiene elementi non confrontabili. Si dovrebbe sollevare un TypeError."
        with self.assertRaises(TypeError,msg=msg):
            decrescente( ( 'ciao', 1.2 ) )
            

    def test_mixed3(self):
        msg="\nTEST FAIL> La lista ['bau','ciao', 1.2] contiene elementi non confrontabili. Si dovrebbe sollevare un TypeError."
        with self.assertRaises(TypeError,msg=msg):
            decrescente( ( 'bau','ciao', 1.2 ) )
        

if __name__ == '__main__':
    unittest.main()
    
