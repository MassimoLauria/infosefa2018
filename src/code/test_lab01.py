#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 01 informatica@sefa 2017/2018


In questo test è ancora troppo presto per fare verifica degli
argomenti numerici. Tutti gli argomenti passati alle funzioni da
testare saranno validi.


Es.1 - scontato(prezzo,sconto) -> float

       dato un prezzo ed uno sconto da 0 a 100, produce il prezzo
       scontato. Ad esempio se il prezzo è 500 e lo sconto è 20 (che
       vuol dire 20 percento), allora il prezzo finale restituito
       è 400.

ES.2 - area_cilindro(raggio,altezza) -> float
     
       essenzialmente una reimplementazione dell'esempio in classe.
       Per vedere se si riesce a scrivere una funzione e a lanciare il
       programma di test. Si deve utilizzare l'approssimazione
       `math.pi'

ES.3 - area_parallelepipedo_rettangolo(altezza,larghezza,profondità) -> float
     
       una piccola variazione dell'esercizio precedente

ES.4 - volume_cilindro(raggio,altezza) -> float

ES.5 - volume_parallelepipedo_rettangolo(altezza,larghezza,profondità) -> float
     
       calcoliamo i volumi questa volta

Es.6 - ghms(secondi) -> str

       scrivere una funzione che prende in input un numero di secondi
       (intero) e restituisce una stringa con l'equivalente in giorni,
       ore, minuti e secondi. Ad esempio se secondi=5000 allora la
       funzione deve restituire una stringa
       
       'Giorni: 0 - Ore: 1 - Minuti: 23 - Secondi: 40'

       Attenti alla formattazione della stringa. No a capo, spazi giusti ecc...

Es.7 - totale_secondi(gg,hh,mm,ss) -> int

       La funzione ha in input un certo numero di giorni, ore, minuti
       e secondi, e deve restituire il totale dei secondi che
       costituiscono l'intero lasso di tempo.

       Ad esempio totale_secondi(2,14,27,12) deve restituire 224832

"""

import lab01 as lab
import unittest
import random

from math import pi as pigreco

class TestLab01Sconto(unittest.TestCase):

    def test_sconti(self):
        for s in range(0,100,10):
            val = lab.scontato(456,s)
            self.assertAlmostEqual(val,4.56*(100-s))

    def test_sconti_zero(self):
        for s in range(0,100,10):
            val = lab.scontato(0,s)
            self.assertAlmostEqual(val,0)


class TestLab01Geometria(unittest.TestCase):

    def test_area_cilindro_zero_altezza(self):
        area = lab.area_cilindro(10,0)
        self.assertAlmostEqual(200*pigreco,area)

    def test_vol_cilindro_zero(self):
        area = lab.volume_cilindro(10,0)
        self.assertAlmostEqual(0,area)

        area = lab.volume_cilindro(0,10)
        self.assertAlmostEqual(0,area)

    def test_area_cilindro_zero_raggio(self):
        area = lab.area_cilindro(0,0)
        self.assertAlmostEqual(0,area)

    def test_area_pi(self):
        area = lab.area_cilindro(1,1)
        self.assertAlmostEqual(4*pigreco,area)

    def test_vol_cilindro_pi(self):
        area = lab.volume_cilindro(1,1)
        self.assertAlmostEqual(pigreco,area)

    def test_vol_ppr_unit(self):
        area = lab.volume_parallelepipedo_rettangolo(1,1,1)
        self.assertAlmostEqual(1,area)

    def test_scaling_vol_cilindro(self):
        raggio = 2.0
        altezza = 5.7
        area = lab.volume_cilindro(raggio,altezza)
        for scale in range(0,10):
            narea = lab.volume_cilindro(scale*raggio,altezza)
            self.assertAlmostEqual(scale**2*area,narea)
            
            narea = lab.volume_cilindro(raggio,scale*altezza)
            self.assertAlmostEqual(scale*area,narea)
        
            narea = lab.volume_cilindro(scale*raggio,scale*altezza)
            self.assertAlmostEqual( (scale**3)*area, narea)

    def test_scaling_vol_ppr(self):
        h = 2.0
        l = 1.0
        p = 3.5
        area = lab.volume_parallelepipedo_rettangolo(h,l,p)
        for scale in range(0,10):
            narea = lab.volume_parallelepipedo_rettangolo(scale*h,l,p)
            self.assertAlmostEqual(scale*area,narea)
            
            narea = lab.volume_parallelepipedo_rettangolo(h,scale*l,p)
            self.assertAlmostEqual(scale*area,narea)
        
            narea = lab.volume_parallelepipedo_rettangolo(h,l,p*scale)
            self.assertAlmostEqual(scale*area,narea)
    



class TestLab01Time(unittest.TestCase):

    def _verify_totali_(self,gg,hh,mm,ss,total):
        res = lab.totale_secondi(gg,hh,mm,ss)
        self.assertEqual(res,total)

    def _verify_ghms_(self,gg,hh,mm,ss,total):
        text = lab.ghms(total)
        ref  = 'Giorni: ' +str(gg)+' - Ore: '+str(hh)+' - Minuti: '+\
               str(mm)+' - Secondi: '+str(ss)
        self.assertEqual(text,ref)
        
    
    def test_totali_zero(self):
        self._verify_totali_(0,0,0,0,0)
 
    def test_totali_1day(self):
        self._verify_totali_(1,0,0,0,60*60*24)
        
    def test_totali_1hour(self):
        self._verify_totali_(0,1,0,0,60*60)

    def test_totali_1min(self):
        self._verify_totali_(0,0,1,0,60)

    def test_totali_1sec(self):
        self._verify_totali_(0,0,0,1,1)


    def test_ghms_zero(self):
        self._verify_ghms_(0,0,0,0,0)

    def test_ghms_1day(self):
        self._verify_ghms_(1,0,0,0,60*60*24)
        
    def test_ghms_1hour(self):
        self._verify_ghms_(0,1,0,0,60*60)

    def test_ghms_1min(self):
        self._verify_ghms_(0,0,1,0,60)

    def test_ghms_1sec(self):
        self._verify_ghms_(0,0,0,1,1)


    def test_ghms_data(self):
        self._verify_ghms_(2,5,1,3,2*86400+5*3600+1*60+3)

    def test_totali_data(self):
        self._verify_totali_(2,5,1,3,2*86400+5*3600+1*60+3)


if __name__ == '__main__':
    unittest.main()
    
