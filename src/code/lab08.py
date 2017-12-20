#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soluzioni per gli esercizi del laboratorio 8
"""

from matplotlib.pyplot import plot,savefig 

def frequenze(testo,lista_parole):
    """Restituisce la lista delle frequenze delle parole cercate,
    rispetto al testo dato in input
    """
    # trova i caratter non alfabetici
    noalpha=''
    for c in testo:
        if not c.isalpha() and c not in noalpha:
            noalpha += c
    # separa tutte le parole nel testo
    for c in noalpha:
        testo = testo.replace(c,' ')
    data=testo.lower().split()
    # restituisci le frequenze
    return [data.count(word.lower()) for word in lista_parole]
    
    
def parse_dati(testo):
    output=[]
    for line in testo.splitlines():

        if len(line.strip())==0:
            continue
            
        l = line.split(":")
        if len(l) != 2:
            raise ValueError("Riga non vuota e mal formattata")

        x,y = float(l[0]),float(l[1])
        output.append( (x,y) )
    return output

def plot_dati(testo,filename):
    x=[]
    y=[]
    for line in testo.splitlines():

        if len(line.strip())==0:
            continue
            
        l = line.split(":")
        if len(l) != 2:
            raise ValueError("Riga non vuota e mal formattata")

        x.append( float(l[0]))
        y.append( float(l[1]))
        
    plot(x,y)
    savefig(filename)
