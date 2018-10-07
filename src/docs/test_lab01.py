#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 01 informatica@sefa 2018/2019

In questo test è ancora troppo presto per fare verifica degli
argomenti numerici. Tutti gli argomenti passati alle funzioni da
testare saranno validi.


Es.1 - scontato(prezzo,sconto) -> float

       dato un prezzo ed uno sconto da 0 a 100, produce il prezzo
       scontato. Ad esempio se il prezzo è 500 e lo sconto è 20 (che
       vuol dire 20 percento), allora il prezzo finale restituito
       è 400.

ES.2 - superficie_cilindro(raggio,altezza) -> float
     
       Essenzialmente una reimplementazione  dell'esempio visto in classe.
       Dati l'altezza  del cilindro ed  il raggio della base,  la funzione
       deve calcolare  la superficie  del cilindro.  E si  deve utilizzare
       l'approssimazione `math.pi'.

ES.3 - volume_cilindro(raggio,altezza) -> float

       Dati l'altezza  del cilindro ed  il raggio della base,  la funzione
       deve  calcolare  il  volume  del cilindro.  E  si  deve  utilizzare
       l'approssimazione `math.pi'.

"""

### Preamble ###
import sys

try:
    from lab01 import scontato,superficie_cilindro,volume_cilindro
except:
    print("Il file 'lab01.py' non è presente o non contiene le soluzioni di tutti gli esercizi.")
    sys.exit(-1)

    
    
import unittest
import random
from math import pi as pigreco

class TestLab01Sconto(unittest.TestCase):

    def test_sconti(self):
        for s in range(0,100,10):
            val_calcolato = scontato(456,s)
            val_corretto  = 4.56*(100-s)
            self.assertAlmostEqual(val_calcolato,val_corretto,
                                   msg="\nTEST FAIL> 456 euro con {}% di sconto è {}, e non {}.".format(s,val_corretto,val_calcolato))

    def test_sconti_zero(self):
        for s in range(0,100,10):
            val_calcolato = scontato(0,s)
            self.assertAlmostEqual(val_calcolato,0,
                                   msg="\nTEST FAIL> Una cosa di prezzo 0, anche scontata, deve costare 0.")


class TestLab01Geometria(unittest.TestCase):

    def test_superficie_cilindro_zero_altezza(self):
        area = superficie_cilindro(10,0)
        self.assertAlmostEqual(200*pigreco,area,
                               msg="\nTEST FAIL> Un cilindro di altezza 0 e raggio 10, ha superficie {}.".format(200*pigreco))

    def test_vol_cilindro_zero(self):
        area = volume_cilindro(10,0)
        self.assertAlmostEqual(0,area,
                               msg="\nTEST FAIL> Un cilindro di raggio 0 ha volume 0.")

        area = volume_cilindro(0,10)
        self.assertAlmostEqual(0,area,
                               msg="\nTEST FAIL> Un cilindro di altezza 0 ha volume 0.")

    def test_superficie_cilindro_zero_raggio(self):
        area = superficie_cilindro(0,0)
        self.assertAlmostEqual(0,area,
                               msg="\nTEST FAIL> Un cilindro di raggio 0 ha superficie 0.")

    def test_area_pi(self):
        area = superficie_cilindro(1,1)
        self.assertAlmostEqual(4*pigreco,area,
                               msg="\nTEST FAIL> Un cilindro di altezza e raggio 1, ha superficie {}.".format(4*pigreco))

    def test_vol_cilindro_pi(self):
        area = volume_cilindro(1,1)
        self.assertAlmostEqual(pigreco,area,
                               msg="\nTEST FAIL> Un cilindro di altezza e raggio 1, ha volume {}.".format(pigreco))

    def test_scaling_vol_cilindro(self):
        raggio = 2.0
        altezza = 5.7
        area = volume_cilindro(raggio,altezza)
        for scale in range(0,10):
            narea = volume_cilindro(scale*raggio,altezza)
            self.assertAlmostEqual(scale**2*area,narea,
                                   msg="\nTEST FAIL> Il volume del cilindro cresce quadraticamente col raggio.")
            
            narea = volume_cilindro(raggio,scale*altezza)
            self.assertAlmostEqual(scale*area,narea,
                                   msg="\nTEST FAIL> Il volume del cilindro cresce linearmente col raggio.")
        
            narea = volume_cilindro(scale*raggio,scale*altezza)
            self.assertAlmostEqual( (scale**3)*area, narea,
                                   msg="\nTEST FAIL> Il volume del cilindro cresce cubicamente scalando tutti i parametri.")
    

if __name__ == '__main__':
    unittest.main()
    
