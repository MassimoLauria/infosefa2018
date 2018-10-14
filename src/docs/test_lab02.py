#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 02 informatica@sefa 2018/2019
"""

import importlib
import unittest
import sys

ex_name      ='lab02'
ex_functions =['scontato','volume_cilindro','superficie_cilindro',
               'ghms','totale_secondi'] 

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



class TestLab02Sconto(unittest.TestCase):

    def test_sconti(self):
        val_calcolato = scontato(456,35)
        val_corretto  = 4.56*65
        self.assertAlmostEqual(val_calcolato,val_corretto,
                               msg="\nTEST FAIL> 456 euro con 35% di sconto è {}, e non {}.".format(val_corretto,val_calcolato))

    def test_sconti_zero(self):
        val_calcolato = scontato(0,50)
        self.assertAlmostEqual(val_calcolato,0,
                               msg="\nTEST FAIL> Una cosa di prezzo 0, anche scontata, deve costare 0.")

    def test_sconti_cento(self):
        val_calcolato = scontato(2724,100)
        self.assertAlmostEqual(val_calcolato,0,
                               msg="\nTEST FAIL> Una cosa scontata al 100% deve costare 0.")

    def test_prezzo_positivo(self):
        msg="\nTEST FAIL> scontato(-10,20) dovrebbe sollevare un ValueError perché il prezzo è negativo."
        with self.assertRaises(ValueError,msg=msg):
            scontato(-10,20)
            
    def test_sconto_range_low(self):
        msg="\nTEST FAIL> scontato(100,-1) dovrebbe sollevare un ValueError perché lo sconto è negativo."
        with self.assertRaises(ValueError,msg=msg):
            scontato(100,-1)

    def test_sconto_range_hi(self):
        msg="\nTEST FAIL> scontato(100,130) dovrebbe sollevare un ValueError perché lo sconto è > 100."
        with self.assertRaises(ValueError,msg=msg):
            scontato(100,130)


from math import pi as pigreco
        
class TestLab02Geometria(unittest.TestCase):

    def test_superficie_cilindro_zero_altezza(self):
        area = superficie_cilindro(10,0)
        msg="\nTEST FAIL> superficie_cilindro(10,0) è {}, non {}".format(200*pigreco,area)
        self.assertAlmostEqual(200*pigreco,area,msg=msg)

    def test_vol_cilindro_zero(self):
        vol = volume_cilindro(10,0)
        msg ="\nTEST FAIL> volume_cilindro(10,0) è {}, non {}".format(0,vol)
        self.assertAlmostEqual(0,vol,msg=msg)

    def test_vol_cilindro_zero2(self):
        vol = volume_cilindro(0,10)
        msg ="\nTEST FAIL> volume_cilindro(0,10) è {}, non {}".format(0,vol)
        self.assertAlmostEqual(0,vol,msg=msg)

    def test_superficie_cilindro_zero_raggio(self):
        area = superficie_cilindro(0,0)
        msg="\nTEST FAIL> superficie_cilindro(0,0) è {}, non {}".format(0,area)
        self.assertAlmostEqual(0,area,msg=msg)

    def test_superficie_pi(self):
        area = superficie_cilindro(1,1)
        msg="\nTEST FAIL> superficie_cilindro(1,1) è {}, non {}".format(4*pigreco,area)
        self.assertAlmostEqual(4*pigreco,area,msg=msg)

    def test_vol_cilindro_pi(self):
        vol = volume_cilindro(1,1)
        msg ="\nTEST FAIL> volume_cilindro(1,1) è {}, non {}".format(pigreco,vol)
        self.assertAlmostEqual(pigreco,vol,msg=msg)

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


    def test_superficie_cilindro_altezza(self):
        msg="\nTEST FAIL> superficie_cilindro(10,-1) dovrebbe sollevare un ValueError perché altezza < 0."
        with self.assertRaises(ValueError,msg=msg):
            superficie_cilindro(10,-1)

    def test_superficie_cilindro_raggio(self):
        msg="\nTEST FAIL> superficie_cilindro(-10,0) dovrebbe sollevare un ValueError perché raggio < 0."
        with self.assertRaises(ValueError,msg=msg):
            superficie_cilindro(-10,0)

    def test_superficie_cilindro_argomenti(self):
        msg="\nTEST FAIL> superficie_cilindro(-1,-1) dovrebbe sollevare un ValueError perché altezza e raggio < 0."
        with self.assertRaises(ValueError,msg=msg):
            superficie_cilindro(-1,-1)

    def test_volume_cilindro_altezza(self):
        msg="\nTEST FAIL> volume_cilindro(10,-1) dovrebbe sollevare un ValueError perché altezza < 0."
        with self.assertRaises(ValueError,msg=msg):
            volume_cilindro(10,-1)
        
    def test_volume_cilindro_raggio(self):
        msg="\nTEST FAIL> volume_cilindro(-10,0) dovrebbe sollevare un ValueError perché raggio < 0."
        with self.assertRaises(ValueError,msg=msg):
            volume_cilindro(-10,0)

    def test_volume_cilindro_argomenti(self):
        msg="\nTEST FAIL> volume_cilindro(-1,-1) dovrebbe sollevare un ValueError perché altezza e raggio < 0."
        with self.assertRaises(ValueError,msg=msg):
            volume_cilindro(-1,-1)

            
class TestLab02Time(unittest.TestCase):

    def _verify_totali_(self,gg,hh,mm,ss,total):
        res = totale_secondi(gg,hh,mm,ss)
        messaggio = "\nTEST FAIL> totale_secondi({},{},{},{}) dovrebbe dare {}, non {}".format(gg,hh,mm,ss,total,res)
        self.assertEqual(res,total,msg=messaggio)

    def _verify_ghms_(self,gg,hh,mm,ss,total):
        text = ghms(total)
        ref  = 'Giorni: ' +str(gg)+' - Ore: '+str(hh)+' - Minuti: '+\
               str(mm)+' - Secondi: '+str(ss)
        messaggio = "\nTEST FAIL> La funzione ghms({})\n dovrebbe produrre: '{}',\n invece produce:    '{}'".format(total,ref,text)
        self.assertEqual(text,ref,msg=messaggio)
        
    
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

    def test_totale_sec_positive(self):
        msg="\nTEST FAIL> totale_secondi(0,0,0,-3) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            totale_secondi(0,0,0,-3)

    def test_totale_min_positive(self):
        msg="\nTEST FAIL> totale_secondi(0,0,-3,0) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            totale_secondi(0,0,-3,0)

    def test_totale_ora_positive(self):
        msg="\nTEST FAIL> totale_secondi(0,-3,0,0) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            totale_secondi(0,-3,0,0)

    def test_totale_giorni_positive(self):
        msg="\nTEST FAIL> totale_secondi(-3,0,0,0) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            totale_secondi(-3,0,0,0)

    def test_ghms_positive(self):
        msg="\nTEST FAIL> ghms(-3) dovrebbe sollevare un ValueError perché ha un parametro < 0."
        with self.assertRaises(ValueError,msg=msg):
            ghms(-3)
    
        

if __name__ == '__main__':
    unittest.main()
    
