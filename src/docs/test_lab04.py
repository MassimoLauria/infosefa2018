#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 04 informatica@sefa 2018/2019

"""
import importlib
import unittest
import sys

ex_name      ='lab04'
ex_functions =['segmenticrescenti','sommeparziali'] 

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




class TestLab04Segmenti(unittest.TestCase):

    def _verify(self,seq,expected):
        result   = segmenticrescenti(seq)
        messaggio = "\nTEST FAIL> La funzione segmenticrescenti({})\n dovrebbe produrre: '{}',\n invece produce:    '{}'".format(seq,expected,result)
        self.assertEqual(expected,result,msg=messaggio)

    def _verify_raise(self,seq,error,reason):
        msg="\nTEST FAIL> segmenticrescenti({}) dovrebbe sollevare un {} perché {}."
        msg = msg.format(seq,error,reason)
        with self.assertRaises(error,msg=msg):
            segmenticrescenti(seq)

    def test_segmenti_inconfrontabili(self):
        self._verify_raise([13,"stringa1","stringa2"],
                           TypeError,
                           "ha elementi non confrontabili")

    def test_segmenti_zero(self):
        self._verify([],[])

    def test_segmenti_one(self):
        self._verify([1],[[1]])

    def test_segmenti_zerot(self):
        self._verify((),[])

    def test_segmenti_one(self):
        self._verify((1,),[[1]])

    def test_segmenti_crescente(self):
        self._verify([1,2,3,4,5],[[1,2,3,4,5]])

    def test_segmenti_decrescente(self):
        self._verify([5,4,3,2,1],[[5],[4],[3],[2],[1]])
        
    def test_segmenti_due(self):
        self._verify([1,2,3,-1,2,3],[[1,2,3],[-1,2,3]])

    def test_segmenti_singleton_iniziale(self):
        self._verify([4,-3,-2,2,7], [[4],[-3,-2,2,7]] )

    def test_segmenti_singleton_finale(self):
        self._verify([-3,-2,2,7,4], [[-3,-2,2,7],[4]] )

    def test_segmenti_uguali(self):
        self._verify([1,1,1,1,1], [[1,1,1,1,1]] )

    def test_segmenti_uguali(self):
        self._verify([2,2,1,1,1], [[2,2],[1,1,1]] )
        
    def test_segmenti_esempio(self):
        self._verify([1,-1,2,4,3,7,8,8,5] ,
                     [ [1], [-1,2,4], [3,7,8,8], [5] ] )

    def test_segmenti_stringa(self):
        self._verify(['casa','studio','garage','mansarda','villaggio'] ,
                     [ ['casa','studio'], ['garage','mansarda','villaggio'] ] )

    def test_segmenti_stringa2(self):
        self._verify('analfabetismo' ,
                     [ ['a','n'], ['a','l'],['f'],['a','b','e','t'],['i','s'],['m','o'] ] )
        
class TestLab04SommeParziali(unittest.TestCase):
     
    def _verify(self,seq,expected):
        result   = sommeparziali(seq)
        messaggio = "\nTEST FAIL> La funzione sommeparziali({})\n dovrebbe produrre: '{}',\n invece produce:    '{}'".format(seq,expected,result)
        self.assertEqual(expected,result,msg=messaggio)

    def _verify_raise(self,seq,error,reason):
        msg="\nTEST FAIL> sommeparziali({}) dovrebbe sollevare un {} perché {}."
        msg = msg.format(seq,error,reason)
        with self.assertRaises(error,msg=msg):
            sommeparziali(seq)
            

    def test_parziali_zero(self):
        self._verify([],[])

    def test_parziali_one(self):
        self._verify([13],[13])

    def test_parziali_zerot(self):
        self._verify((),[])

    def test_parziali_one(self):
        self._verify((12,),[12])

    def test_parziali_string(self):
        self._verify(('aa','bb','cc'),['aa','aabb','aabbcc'])

        
    def test_somme_insommabili1(self):
        self._verify_raise([13,"stringa1","stringa2"],
                           TypeError,
                           "ha elementi non sommabili")

    def test_somme_insommabili2(self):
        self._verify_raise(('ciao',1.2),
                           TypeError,
                           "ha elementi non sommabili")

    def test_small1(self):
        self._verify( [-2,2]  , [-2,0])
    
    def test_small2(self):
        self._verify( [1,2]  , [1,3])

    def test_ones(self):
        self._verify( [1,1,1,1,1,1,1,1]  , [1,2,3,4,5,6,7,8])

    def test_sequence(self):
        self._verify( [1,2,3,4,5,6,7,8]  , [1,3,6,10,15,21,28,36])

    def test_mixed(self):
        self._verify( [1,2.3], [1,3.3])

            
        
        
if __name__ == '__main__':
    unittest.main()
    
