#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Fake implementation

import math


def scontato(prezzo,sconto):
    return prezzo*(100-sconto)/100

def area_cilindro(raggio,altezza):
    area = 2*math.pi*raggio*altezza + 2 * math.pi * raggio**2 
    return area
     
def area_parallelepipedo_rettangolo(altezza,larghezza,profondità):
    faccia1 = altezza * larghezza 
    faccia2 = altezza * profondità 
    faccia3 = larghezza * profondità
    return 2*(faccia1 + faccia2 + faccia3)
     
def volume_cilindro(raggio,altezza):
    return altezza * raggio**2 * math.pi

def volume_parallelepipedo_rettangolo(altezza,larghezza,profondità):
    return altezza*larghezza*profondità

def totale_secondi(gg,hh,mm,ss):
    sec_in_min = 60
    sec_in_ora = sec_in_min * 60
    sec_in_giorno = sec_in_ora * 24
    return gg*sec_in_giorno + hh*sec_in_ora + mm*sec_in_min + ss


def ghms(secondi):
    sec_in_min = 60
    sec_in_ora = sec_in_min * 60
    sec_in_giorno = sec_in_ora * 24

    giorni = secondi // sec_in_giorno
    secondi %= sec_in_giorno

    ore = secondi // sec_in_ora
    secondi %= sec_in_ora

    minuti = secondi // sec_in_min
    secondi %= sec_in_min

    return 'Giorni: ' + str(giorni) +' - Ore: ' + str(ore) \
        +' - Minuti: ' + str(minuti) +' - Secondi: '+str(secondi)

