#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 06 informatica@sefa 2018/2019

"""
import importlib
import unittest
import sys

ex_name      ='lab06'
ex_functions =['benformata','proiezione'] 

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




class TestLab06Benformata(unittest.TestCase):

    def _verify(self,data,expected):
        result   = benformata(data)
        messaggio = "\nTEST FAIL> La funzione benformata({})\n dovrebbe produrre: '{}',\n invece produce:    '{}'".format(data,expected,result)
        self.assertEqual(expected,result,msg=messaggio)

    def _verify_raise(self,data,error,reason):
        msg="\nTEST FAIL> benformata({}) dovrebbe sollevare un {} perché {}."
        msg = msg.format(data,error,reason)
        with self.assertRaises(error,msg=msg):
            benformata(data)

    def test_stringa(self):
        self._verify("è una tabella?",False)

    def test_vuoto(self):
        self._verify({},True)

    def test_senza_righe(self):
        self._verify({1:[],2:[],3:[]},True)

    def test_una_colonna(self):
        self._verify({1:['a','b','c']},True)

    def test_colonne_diverse1(self):
        self._verify({1:[1,2],2:[1,2,3],3:[1,2,3]},False)

    def test_colonne_diverse2(self):
        self._verify({1:[1,2,3],2:[1,2],3:[1,2,3]},False)

    def test_colonne_diverse3(self):
        self._verify({1:[1,2,3],2:[1,2,3],3:[1,2]},False)

    def test_colonne_tipodiverso1(self):
        self._verify({1:12,2:[1,2],3:[1,2,3]},False)

    def test_colonne_tipodiverso2(self):
        self._verify({1:[1,2,3],2:12,3:[1,2,3]},False)

    def test_colonne_tipodiverso3(self):
        self._verify({1:[1,2,3],2:[1,2,3],3:12},False)

    def test_colonne_tupla1(self):
        self._verify({1:(1,2,3),2:[1,2,3]},False)
    def test_colonne_tupla2(self):
        self._verify({1:[1,2,3],2:(1,2,3)},False)


class TestLab06Proiezioni(unittest.TestCase):

    def _verify(self,tab,cols,expected):
        result   = proiezione(tab,cols)
        messaggio = "\nTEST FAIL> La proiezione della tabella \n{}\n" + \
                    "sulle colonne {} dovrebbe produrre: '{}',\n invece produce:    '{}'"
        messaggio = messaggio.format(tab,cols,expected,result)
        self.assertEqual(expected,result,msg=messaggio)

    def _verify_raise(self,tab,cols,error,reason):
        msg="\nTEST FAIL> proiezione({},{}) dovrebbe sollevare un {} perché {}."
        msg = msg.format(tab,cols,error,reason)
        with self.assertRaises(error,msg=msg):
            proiezione(tab,cols)

    def test_malformata1(self):
        self._verify_raise({1:[1,2],2:[1,2,3],3:[1,2,3]},[1,2],
                           TypeError,
                           "La tabella non è benformata")
        
    def test_malformata2(self):
        self._verify_raise({1:(1,2,3),2:[1,2,3]},[1,2],
                           TypeError,
                           "La tabella non è benformata")

    def test_malformata3(self):
        self._verify_raise({1:[1,2,3],2:12,3:[1,2,3]},[1,2],
                           TypeError,
                           "La tabella non è benformata")


    def test_colonne_assenti(self):
        self._verify_raise({'a':[1,2,3],'b':[1,2,3],'c':[1,2,3]},'de',
                           ValueError,
                           "Le colonne richieste non fanno parte della tabella.")
        
    def test_colonne_alcune_assenti(self):
        self._verify_raise({'a':[1,2,3],'b':[1,2,3],'c':[1,2,3]},'acd',
                           ValueError,
                           "Alcune delle colonne richieste non fanno parte della tabella.")

    def test_projection1(self):
        egdict = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9], 'd':[10,11,12]}
        res = {'a':[1,2,3],'c':[7,8,9]}
        self._verify(egdict,'ac',res)

    def test_projection2(self):
        egdict = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9], 'd':[10,11,12]}
        res = {'b':[4,5,6]}
        self._verify(egdict,'b',res)
        
    def test_projection3(self):
        egdict = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9], 'd':[10,11,12]}
        res = {'a':[1,2,3],'d':[10,11,12]}
        self._verify(egdict,'ad',res)

if __name__ == '__main__':
    unittest.main()
    
