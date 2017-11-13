#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def max_mod(lista,base):
    if base <=0:
        raise ValueError("invalid base argument")
    if len(lista)==0:
        raise ValueError("empty sequence")
    return max(x for i,x in enumerate(lista) if i%base==0)



def n_righe_tabella(tabella):
    rows=None
    for v in tabella.values():
        if rows is None:
            rows=len(v)
        elif rows!=len(v):
            raise ValueError("la tabella ha colonne di lunghezza diversa")
    if rows is None:
        raise ValueError("la tabella non ha campi")
        
    return rows

def formatta_riga(tabella,indice,vista):
    righe= n_righe_tabella(tabella)
    if indice  >= righe or indice < 0:
        raise ValueError("indice di riga non valido")
    
    text = []
    for nome,spazi,align in vista:

        if nome not in tabella.keys():
            raise ValueError("nome della colonna non valido")

        if align not in ['r','l']:
            raise ValueError("indicatore allineamento non valido")

        if len(str(tabella[nome][indice]))>spazi:
            raise ValueError("spazio per la colonna {} non sufficiente".format(nome))

        format_str=' {{: {0}{1}}} '.format('<' if align=='l' else '>',spazi)
        text.append(format_str.format(tabella[nome][indice]))

    return "|" + "|".join(text) + "|"

def formatta_tabella(tabella,colonne):
    nrighe = n_righe_tabella(tabella)

    vista = []

    for colonna in colonne:
        if colonna not in tabella.keys():
            raise ValueError("nome della colonna non valido")

        spazio = len(str(colonna))

        if len(tabella[colonna])>0:
            tmp =  max(len(str(x)) for x in tabella[colonna])
            spazio = max(spazio,tmp)
            
        numeric = all( type(x) in [float,int] for x in tabella[colonna])
        align = 'r' if numeric else 'l'

        vista.append((colonna,spazio,align))


    # intestazione
    temp ={ colonna : [colonna] for colonna in colonne }
    righe=["",""]
    righe[0] = formatta_riga(temp,0,vista)
    righe[1] = "|" + "+".join( '-'*(spazio+2) for _,spazio,_ in vista) + "|"

    for riga in range(nrighe):
        righe.append(formatta_riga(tabella,riga,vista))

    return "\n".join(righe)
