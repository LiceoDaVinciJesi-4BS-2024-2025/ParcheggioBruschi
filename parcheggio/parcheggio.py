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
            
    
    def parcheggia(self, veicolo:Veicolo):
        if isinstance(veicolo, Auto):
            # allora è un auto...
            for posto in self.__postiAuto:
                if not posto.postoOccupato():
                    posto.occupaPosto(veicolo.targa)
                    return True
            
            # posti auto pieni
            return False
                    
                    
        if isinstance(veicolo, Moto):
            # allora è una moto...
        
        