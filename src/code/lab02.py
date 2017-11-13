#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math


def scontato(prezzo,sconto):
    if sconto<0 or sconto>100:
        raise ValueError("sconto deve essere tra 0 e 100")
    if prezzo<0:
        raise ValueError("prezzo deve essere non negativo")
    return prezzo*(100-sconto)/100

def area_cilindro(raggio,altezza):
    if raggio<0 or altezza<0:
        raise ValueError("raggio e altezza devono essere non negativi")
    area = 2*math.pi*raggio*altezza + 2 * math.pi * raggio**2 
    return area
     
def area_parallelepipedo_rettangolo(altezza,larghezza,profondità):
    if altezza<0 or larghezza<0 or profondità<0:
        raise ValueError("le dimensioni devono essere non negative")
    faccia1 = altezza * larghezza 
    faccia2 = altezza * profondità 
    faccia3 = larghezza * profondità
    return 2*(faccia1 + faccia2 + faccia3)
     
def volume_cilindro(raggio,altezza):
    if raggio<0 or altezza<0:
        raise ValueError("raggio e altezza devono essere non negativi")
    return altezza * raggio**2 * math.pi

def volume_parallelepipedo_rettangolo(altezza,larghezza,profondità):
    if altezza<0 or larghezza<0 or profondità<0:
        raise ValueError("le dimensioni devono essere non negative")
    return altezza*larghezza*profondità

def totale_secondi(gg,hh,mm,ss):
    if gg<0 or hh<0 or mm<0 or ss<0:
        raise ValueError("mi aspetto input non negativi")
    sec_in_min = 60
    sec_in_ora = sec_in_min * 60
    sec_in_giorno = sec_in_ora * 24
    return gg*sec_in_giorno + hh*sec_in_ora + mm*sec_in_min + ss


def ghms(secondi):
    if secondi<0:
        raise ValueError("mi aspetto un input non negativo")
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


def ghms2(secondi):
    if secondi<0:
        raise ValueError("mi aspetto un input non negativo")
    if secondi == 0:
        return "0 secondi."

    sec_in_min = 60
    sec_in_ora = sec_in_min * 60
    sec_in_giorno = sec_in_ora * 24

    giorni = secondi // sec_in_giorno
    secondi %= sec_in_giorno

    ore = secondi // sec_in_ora
    secondi %= sec_in_ora

    minuti = secondi // sec_in_min
    secondi %= sec_in_min

    finale=[]
    
    if giorni == 1:
        finale.append( "1 giorno" )
    elif giorni > 1:
        finale.append( str(giorni) + " giorni")

    if ore == 1:
        finale.append( "1 ora" )
    elif ore > 1:
        finale.append( str(ore) + " ore")

    if minuti == 1:
        finale.append( "1 minuto" )
    elif minuti > 1:
        finale.append( str(minuti) + " minuti")

    if secondi == 1:
        finale.append( "1 secondo" )
    elif secondi > 1:
        finale.append( str(secondi) + " secondi")

    if len(finale)==1:
        return finale[0] + '.'
    else:
        return ", ".join(finale[:-1]) + " e " + finale[-1] + "."

def ordinati(lista):
    if len(lista)<2:
        return True
    first = lista[0]
    for second in lista[1:]:
        if (type(first)==str) ^ (type(second)==str):
            raise ValueError("Lista di tipo non omogeneo")
        elif first > second:
            return False
        else:
            first = second
    return True
