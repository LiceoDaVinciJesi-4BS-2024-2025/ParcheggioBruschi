#Bruschi Ginevra
#4BS
# livello 2

#importare i file veicolo, auto, moto
import veicolo
import auto
import moto
#importare il modulo datetime
import datetime

lettereTarga="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeriTarga="123456789"

#definire la classe
class PostoMezzo:
     def __init__(self):
         
         #le definisci
         self.__targa=""
         self.__tarmineOccupazione=None
         
        
     #def  str
     def __str__(self):
         return self.__class__.__name__ + str(self.__dict__)
    
     def __repr__(self):
         return self.__class__.__name__ + str(self.__dict__)
        
        
    # definirte le proprietà        
     @property
     def targa(self):
         return self.__targa
        
     @property
     def termineOccupazione(self):
         return self.__tarmineOccupazione
        
        
    # creare una funzione per vederre se il posto è occupato o no
     def postoOccupato(self):
         if self.__targa == "":
             return False #se la targa non c'è allora è libero
         return True
        
    # funzione libera posto
     def liberaPosto(self):
        self.__targa==""
        
     def occupaPosto(self,targaNuova:str):
         if self.__targa == targaNuova:
             raise ValueError ("il posto è ancora occupato")
        
         self.__targa=targaNuova
         self.__tarmineOccupazione=datetime.datetime.now()
        

#------------------------------------------
if __name__=="__main__":
    posto=PostoMezzo()
    print (posto)
    print("Occupato?:", posto.postoOccupato())
    print("libero il posto", posto.liberaPosto())
    print("Occupato?:", posto.postoOccupato())
    print(posto.occupaPosto("AB123CD") )
    print (posto)
    print("Occupato?:", posto.postoOccupato())
    
    print()
    
