#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 01 informatica@sefa 2017/2018


In questo test è ancora troppo presto per fare verifica degli
argomenti numerici. Tutti gli argomenti passati alle funzioni da
testare saranno validi.


Es.8 - migliorare le funzioni degli esercizi 1,2,3,4,5,6,7

ES.9 - ghms2(secondi)

   simile a  quella di =lab01=,  ma che produca stringhe  più sensate.
   Ad esempio.
   
   |  input | output                           |
   |--------+----------------------------------|
   |      0 | =0 secondi.=                     |
   |   2348 | =39 minuti e 8 secondi.=         |
   |   3840 | =1 ora e 4 minuti.=              |
   | 122456 | =1 giorno, 10 ore e 56 secondi.= |

   - attenzione ai plurali e singolari.
   - attenzione alla punteggiatura e all'uso di 'e'
   - controllare la correttezza degli input
   - fate un bel respiro e aiutatevi con il file di test


ES.10 - ordinati(lista)

   Prende in input una sequenza di elementi e 

   - solleva =ValueError= se nella lista ci sono sia numeri che stringhe
   - restituisce =True= se sono ordinati dal più basso al più alto
   - restituisce =False= se non sono ordinati


"""

import lab02 as lab
import unittest

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

    def test_prezzo_positivo(self):
        self.assertRaises(ValueError,lab.scontato,-10,20)
            
    def test_sconto_range(self):
        self.assertEqual(lab.scontato(100,0),100)
        self.assertEqual(lab.scontato(100,100),0)
        self.assertRaises(ValueError,lab.scontato,100,-1)
        self.assertRaises(ValueError,lab.scontato,100,130)

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

    def test_area_ppr_unit(self):
        area = lab.area_parallelepipedo_rettangolo(1,1,1)
        self.assertAlmostEqual(6,area)

    def test_area_ppr_zero(self):
        area = lab.area_parallelepipedo_rettangolo(1,0,1)
        self.assertAlmostEqual(2,area)

    def test_area_ppr_zero_zero(self):
        area = lab.area_parallelepipedo_rettangolo(1,0,0)
        self.assertAlmostEqual(0,area)

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
    
    def test_area_cilindro_argomenti(self):
        self.assertRaises(ValueError,lab.area_cilindro,10,-1)

    def test_area_cilindro_raggio(self):
        self.assertRaises(ValueError,lab.area_cilindro,-10,0)

    def test_area_cilindro_argomenti(self):
        self.assertRaises(ValueError,lab.area_cilindro,-1,-1)

    def test_volume_cilindro_argomenti(self):
        self.assertRaises(ValueError,lab.volume_cilindro,10,-1)

    def test_volume_cilindro_raggio(self):
        self.assertRaises(ValueError,lab.volume_cilindro,-10,0)

    def test_volume_cilindro_argomenti(self):
        self.assertRaises(ValueError,lab.volume_cilindro,-1,-1)

    def test_volume_ppr_altezza(self):
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,-1,1,1)

    def test_volume_ppr_larghezza(self):
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,1,-1,1)

    def test_volume_ppr_profondità(self):
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,1,1,-1)

    def test_volume_ppr_argomenti(self):
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,-1,-1,1)
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,-1,1,-1)
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,1,-1,-1)
        self.assertRaises(ValueError,lab.volume_parallelepipedo_rettangolo,-1,-1,-1)

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

    def test_totale_sec_positive(self):
        self.assertRaises(ValueError,lab.totale_secondi,0,0,0,-3)

    def test_totale_min_positive(self):
        self.assertRaises(ValueError,lab.totale_secondi,0,0,-3,0)

    def test_totale_ora_positive(self):
        self.assertRaises(ValueError,lab.totale_secondi,0,-3,0,0)

    def test_totale_giorni_positive(self):
        self.assertRaises(ValueError,lab.totale_secondi,-3,0,0,0)

    def test_ghms_positive(self):
        self.assertRaises(ValueError,lab.ghms,-3)

    def test_ghms_data(self):
        self._verify_ghms_(2,5,1,3,2*86400+5*3600+1*60+3)

    def test_totali_data(self):
        self._verify_totali_(2,5,1,3,2*86400+5*3600+1*60+3)


class TestLab02GHMS2(unittest.TestCase):

    def _verify_ghms(self,secondi,text):
        self.assertEqual(text,lab.ghms2(secondi))

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

    def test_ghms2_positive(self):
        self.assertRaises(ValueError,lab.ghms,-3)


class TestLab02Ordered(unittest.TestCase):

    def test_base_cases(self):
        self.assertTrue(lab.ordinati([1]))
        self.assertTrue(lab.ordinati([]))

    def test_small(self):
        self.assertTrue(lab.ordinati([1,2]))
        self.assertFalse(lab.ordinati([2,1]))

    def test_mixed(self):
        self.assertRaises(ValueError,lab.ordinati,[1,'2'])
        self.assertRaises(ValueError,lab.ordinati,["1.0",2])
        self.assertTrue(lab.ordinati([1.0,2]))
        self.assertFalse(lab.ordinati([2.3,1]))

    def test_examples_cases1(self):
        self.assertFalse( lab.ordinati([4,5,1,3,1]) )

    def test_examples_cases2(self):
        self.assertFalse( lab.ordinati([1,4,4,1,3,1]) )

    def test_examples_cases3(self):
        self.assertFalse( lab.ordinati([1,2,3,4,5,4]) )

    def test_examples_cases4(self):
        self.assertTrue( lab.ordinati([1,1,1,1,1,1]) )

    def test_repetition(self):
        self.assertTrue( lab.ordinati([1,2,3,4,4,4,5,6,7]) )

    def test_int_float(self):
        self.assertTrue( lab.ordinati([1.0,2.3,3.1,4.5,6,7.4]) )
          
if __name__ == '__main__':
    unittest.main()
    
