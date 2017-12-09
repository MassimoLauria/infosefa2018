# MinMods - scheletro della funzione.
from infosefa import testErrore,testRisultato

def minmods(L,k):
    """Il minimo delle k sottosequenze di passo k

    Restituisce una lista di k numeri. L'i-esimo numero della
    lista in output è il minimo della sottosequenza
    di L che corrisponde alle posizioni i,i+k,i+2k,i+3k.

    Parametri
    - L: una lista di numeri
    - k: un numero intero strettamente positivo
    
    Restituisce
    - Lista di k numeri
    
    Errori sollevati
    - ValueError se k<1
    - ValueError se L ha lunghezza minore di k
    - TypeError  se L contiene valori non numerici
    """
    return []



if __name__ == '__main__':
    testErrore("1",ValueError,minmods,[1,2,3],4)
    testErrore("2",TypeError,minmods,[1,2,'a',4],3)
    testErrore("3",ValueError,minmods,[1],0)
    testErrore("4",ValueError,minmods,[1],-2)
    testErrore("5",ValueError,minmods,[1],3.2)
    
    testRisultato("6",[1],minmods,[1],1)
    testRisultato("7",[2,2,2,2],minmods,[2,2,2,2],4)
    
    testRisultato("8",[1,9],minmods,[3,9,2,10,1],2)
    testRisultato("9",[1,1,2],minmods,[4,4,4,3,3,3,2,2,2,1,1],3)
