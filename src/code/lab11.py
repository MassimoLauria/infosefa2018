#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from matplotlib.pyplot import plot,savefig,xlabel,ylabel

DB='../dataset/registro_automobilistico_db.sqlite'

def simple_query(tables,columns):

    query = 'select {1} from {0}'.format(tables,columns)
    result = []
    
    with sqlite3.connect(DB) as connessione:
        for row in connessione.execute(query):
            result.append( row )

    return result


def plot_query(filename):
    
    query = """
    select Cilindrata,Velocità from Veicoli 
           where Cilindrata is not NULL and Velocità is not NULL
    """
    x = []
    y = []
    with sqlite3.connect(DB) as connessione:
        for row in connessione.execute(query):
            x.append( int(row[0]) )
            y.append( int(row[1]) )

    xlabel('Cilindrata')
    ylabel('Velocità')
    plot(x,y,'ro')
    savefig(filename)
