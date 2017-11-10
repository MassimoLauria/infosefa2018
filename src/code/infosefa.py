#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Codice utile per le esercitazioni di Informatica@SEFA 2017/2018

Il modulo contiene alcune funzioni utili per le esercitazioni.
Verrà regolarmente esteso quindi controllate che non vi siano
aggiornamenti disponibili prima di usarlo.

Copyright (C) 2017  Massimo Lauria <massimo.lauria@uniroma1.it>
"""

   
import random

def numeriacaso(N,minimo,massimo,ordinati=False):
    """Produce una lista di numeri generati a caso.

    Produce una lista di N elementi, ognuno dei quali preso a caso
    (con uguale probabilità) tra tutti i numeri interi compresi tra
    'minimo' e 'massimo', estremi inclusi.

    Se N<0 o minimo>massimo la funzione solleva un ValueError.

    Se 'ordinati' è vero la lista restituita è ordinata.
    """
    if N<0:
        ValueError("Quantità negativa di numeri da generare.")
    if minimo>massimo:
        ValueError("L'intervallo dei valori non ha senso: minimo>massimo.")
    seq = [random.randint(minimo,massimo) for _ in range(N)]
    if ordinati:
        seq.sort()
    return seq

def bubblesort(seq):
    """Ordina la sequenza utilizzando bubblesort
    """
    end=len(seq)-1
    while end>0:
        last_swap = -1
        for i in range(0,end):
            if seq[i] > seq[i+1]:
                last_swap = i
                seq[i], seq[i+1] = seq[i+1],seq[i]
        end=last_swap


def argmin(seq,start,end):
    minimo = seq[start]
    indice = start
    for i in range(start+1,end+1):
        if seq[i] < minimo:
            minimo = seq[i]
            indice = i
    return minimo,indice

def insertionsort(seq):
    """Ordina la sequenza utilizzando insertionsort
    """    
    for i in range(0,len(seq)-1):
        
        val,pos = argmin(seq,i,len(seq)-1)
        
        for j in range(pos-1,i-1,-1):
            seq[j+1] = seq[j] 

        seq[i] = val


