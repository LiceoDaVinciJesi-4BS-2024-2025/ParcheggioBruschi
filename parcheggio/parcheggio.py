#Bruschi Ginevra
#4BS
# esercizio

from postoMezzo import *
from veicolo import *
from auto import *
from moto import *

MAX_AUTO = 1000
MAX_MOTO = 200

class Parcheggio:
    def __init__(self):
        
        self.__postiAuto=[]
        for n in range(MAX_AUTO):
            posto = PostoMezzo()
            self.__postiAuto.append(posto)
        
        self.__postiMoto = []
        for n in range(MAX_MOTO):
            posto = PostoMezzo()
            self.__postiMoto.append(posto)
    
    def __str__(self):
        return __class__.__name__ + str(self.__dict__)
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
    
    
    def parcheggia(self, veicolo:Veicolo):
        if isinstance(veicolo, Auto):
            
            # allora è un auto...
            for posto in self.__postiAuto:
                if not posto.postoOccupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            # posti auto pieni
            if len(self.__postiAuto)>= MAX_AUTO:
                raise ValueError ("i posti per le macchine sono pieni")
            return False
                    
                    
        if isinstance(veicolo, Moto):
            # allora è una moto...
            for posto in self.__postiMoto:
                if not posto.postoOccupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            #posti moto pieni
            if len(self.__postiMoto)>= MAX_MOTO:
                raise ValueError ("il parcheggio per le moto è pieno")
            return False
        
    def liberaParcheggio (self, targa:str):
        
        for parcheggio in self.__postiAuto:
            if parcheggio.targa == targa:
                parcheggio.liberaPosto()
                break
        return False
            
        for parcheggio in self.__postiMoto:
            if parcheggio.targa == targa:
                parcheggio.liberaPosto()
                break
            
        return False
        
    
        
#-----------------------------------------------
if __name__=="__main__":
    parcheggio=Parcheggio()
    print(parcheggio)

    mezzo1=Auto("AB123CD", 5,2)
    print("parcheggiare la macchina", parcheggio.parcheggia(mezzo1))
    
    mezzo2=Moto("PO567RF",2,1)
    print("parcheggiare la moto",parcheggio.parcheggia(mezzo2))
    
    print(parcheggio)
    
    print(parcheggio.liberaParcheggio(mezzo1.targa))
    
    print(parcheggio)
    