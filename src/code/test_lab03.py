#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test per gli esercizi del Lab 03 informatica@sefa 2017/2018


Es. 11

   max_mod(lista,base)

   Che data  una lista o una  sequenza restituisca il massimo  tra gli
   elementi nelle  posizioni $0$, =base=, =2*base=, ecc... 

   Sollevate l'eccezione ValueError se base <=0 o se la lista è vuota.

Es. 12

   : formatta_riga(tabella,indice_riga,vista)

   - la tabella è data nel formato descritto in precedenza
   - =indice_riga= quale riga deve essere stampata (0 è la prima riga)
   - =vista= è una sequenza di triple dove per ogni tripla
     + nome di una colonna da stampare
     + l'ampiezza della colonna 
     + ='l'= o ='r'= per indicare allineamento a sx o dx

   Possono esserci ripetizioni tra le colonne e alcune colonne possono
   essere omesse

   Possono esserci ripetizioni tra le colonne e alcune colonne possono
   essere omesse

   Esempio:  "| A1003  | ghms2                |    20 | 20   |"

   - separatori tra le colonne
   - uno spazio tra separatore e il testo della colonna

Es.13 

   Formattate un'intera tabella

   - una riga contenente i nomi delle colonne
   - una riga separatrice (con dei =+= agli incroci)
   - allineamento a sinistra per i campi alfanumerici
   - a destra per quelli *esclusivamente* numerici
   - calcolate voi lo spazio necessario

  "| codice | esercizio             | percentuale voto |
   |--------+-----------------------+------------------|
   | A1001  | calcolo dello sconto  |               10 |
   | A1002  | formattazione strighe |               20 |
   | A1003  | ghms2                 |               20 |
   | A1004  | operazioni su tabelle |               15 |
   | A1005  | interprete assembler  |               35 |"

"""

from lab03 import max_mod,formatta_riga,formatta_tabella
import unittest


data1=[1,7,3,5,7,-4,20,1]
data2=('a','A','Aa','ab','g','21')



tabella1 = {
    "nome" : ["Gianni","Bruna",'Alessandra','Marta','Giacomo'],
    "matricola" : ['AX7382','BC1991','AC8931','XX9289','A1152'],
    "v" : [23,21,27,19,24]
}

tabella2 = {
    "codice" : ['A1001','A1002','A1003','A1004','A1005'],
    "esercizio" : ['calcolo dello sconto',
                   'formattazione strighe',
                   'ghms2',
                   'operazioni su tabelle',
                   "interprete assembler"],
    "percentuale voto" : [10,20,20,15,35]
}

tabella_senza_campi = {}

tabella_vuota ={
    "codice" : (),
    "esercizio" : (),
    "percentuale_voto" : ()
}

tabella_invalida = {
    "colonna1" : [100,1000,10000,100000],
    "colonna2" : ['7h(/@pCa:prG','x$|BpvG+30,a']
}

class TestLab03MaxMod(unittest.TestCase):

    def test_vuota(self):
        self.assertRaises(ValueError,max_mod,[],3)

    def test_base_invalid(self):
        self.assertRaises(ValueError,max_mod,(1,2,3),0)

    def test_due_errori(self):
        self.assertRaises(ValueError,max_mod,[],0)        

    def match_max(self,lista,base):
        self.assertEqual(max_mod(lista,base),max([x for i,x in enumerate(lista) if i%base==0]))
        
    def same_max(self,lista):
        self.assertEqual(max_mod(lista,1),max(lista))

    def test1s(self):
        self.same_max(data1)
    def test2s(self):
        self.same_max(data2)
        
    def test1m(self):
        self.match_max(data1,2)

    def test2m(self):
        self.match_max(data2,3)

class TestLab03StampaRiga(unittest.TestCase):

    def test_no_campi(self):
        self.assertRaises(ValueError,formatta_riga,tabella_senza_campi,0,[])
    
    def test_nomi_sbagliati(self):
        self.assertRaises(ValueError,formatta_riga,tabella1,0,[("nome",20,'l'),("cognome",30,'r')])
        self.assertRaises(ValueError,formatta_riga,tabella2,0,[("nome",20,'l'),("cognome",30,'r')])

    def test_spazi_sbagliati(self):
        self.assertRaises(ValueError,formatta_riga,tabella1,0,[("nome",2,'l')])
        self.assertRaises(ValueError,formatta_riga,tabella2,0,[("nome",2,'l')])

    def test_align_sbagliato(self):
        self.assertRaises(ValueError,formatta_riga,tabella1,0,[("nome",20,'a')])
        self.assertRaises(ValueError,formatta_riga,tabella2,0,[("nome",20,'34')])

    def test_indice1(self):
        self.assertRaises(ValueError,
                          formatta_riga,tabella2,7,
                          [('codice',10,'l'),('esercizio',30,'l'),('percentuale voto',5,'r')])
        
    def test_indice2(self):
        self.assertRaises(ValueError,
                          formatta_riga,tabella2,7,
                          [('codice',10,'l'),('esercizio',30,'l'),('percentuale voto',5,'r')])

    def test_invalida(self):
        self.assertRaises(ValueError,formatta_riga,tabella_invalida,1,[('colonna1',20,'r')])

    def test_riga1(self):
        self.assertEqual(formatta_riga(tabella1,3,[('v',10,'r'),('nome',20,'r'),('v',10,'l')]),
                         "|         19 |                Marta | 19         |")

    def test_riga2(self):
        self.assertEqual(formatta_riga(tabella1,2,[('v',10,'r'),('nome',20,'r'),('v',10,'l')]),
                         "|         27 |           Alessandra | 27         |")
    def test_riga3(self):
        self.assertEqual(formatta_riga(tabella1,2,[('nome',20,'l')]),
                         "| Alessandra           |")
    def test_riga4(self):
        self.assertEqual(formatta_riga(tabella2,1,[('codice',10,'l'),('esercizio',30,'l'),('percentuale voto',5,'r')]),
                         "| A1002      | formattazione strighe          |    20 |")
        
class TestLab03StampaTabella(unittest.TestCase):
    pass

    def test_no_campi(self):
        self.assertRaises(ValueError,formatta_tabella,tabella_senza_campi,[])
    
    def test_nomi_sbagliati(self):
        self.assertRaises(ValueError,formatta_tabella,tabella1,["nome","cognome"])
        self.assertRaises(ValueError,formatta_tabella,tabella2,["nome","cognome"])

    def test_invalida(self):
        self.assertRaises(ValueError,formatta_riga,tabella_invalida,1,['colonna1'])

    def test_completa1(self):
        self.assertEqual(formatta_tabella(tabella1,['nome','matricola','v']),
                         """
| nome       | matricola |  v |
|------------+-----------+----|
| Gianni     | AX7382    | 23 |
| Bruna      | BC1991    | 21 |
| Alessandra | AC8931    | 27 |
| Marta      | XX9289    | 19 |
| Giacomo    | A1152     | 24 |
""".strip())

    def test_ripetizioni(self):
        self.assertEqual(formatta_tabella(tabella1,['nome','nome','v']),
                         """
| nome       | nome       |  v |
|------------+------------+----|
| Gianni     | Gianni     | 23 |
| Bruna      | Bruna      | 21 |
| Alessandra | Alessandra | 27 |
| Marta      | Marta      | 19 |
| Giacomo    | Giacomo    | 24 |
""".strip())

    def test_completa2(self):
        self.assertEqual(formatta_tabella(tabella2,['codice','esercizio','percentuale voto']),
                         """
| codice | esercizio             | percentuale voto |
|--------+-----------------------+------------------|
| A1001  | calcolo dello sconto  |               10 |
| A1002  | formattazione strighe |               20 |
| A1003  | ghms2                 |               20 |
| A1004  | operazioni su tabelle |               15 |
| A1005  | interprete assembler  |               35 |""".strip())

        
if __name__ == '__main__':
    unittest.main()
    
