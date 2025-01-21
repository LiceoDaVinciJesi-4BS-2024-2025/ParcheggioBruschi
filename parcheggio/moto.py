#Bruschi Ginevra
#4BS
# livello 1

from veicolo import*

class Moto(Veicolo):
    def __init__(self, targa:str, numeroMassimoPasseggeri:int, passeggeriTrasportati:int):
        super().__init__(targa)
        
        #controllare il numero masimo di passeggeri
        if numeroMassimoPasseggeri <= 0 or numeroMassimoPasseggeri >2:
            raise ValueError ("il numero non è valido")
        self.__numeroMassimoPasseggeri=numeroMassimoPasseggeri
        
        #controllare il numero di passeggeri trasportati
        if passeggeriTrasportati < 0 or passeggeriTrasportati > (numeroMassimoPasseggeri-1):
            raise ValueError ("il numero non è valido")
        self.__passeggeriTrasportati = passeggeriTrasportati
    
    #-----------------------------------------------------------
    #difinire le proprietà
    @property
    def numeroMassimoPasseggeri (self):
        return self.__numeroMassimoPasseggeri
    
    @property
    def passeggeriTrasportati (self):
        return self.__passeggeriTrasportati
    
    #----------------------------------------------------------
    #definire le setter
    @numeroMassimoPasseggeri.setter
    def numeroMassimoPasseggeri (self, value):
        if value <= 0 or value > 2:
            raise ValueError ("non valido")
        self.__numeroMassimoPasseggeri=value
        return
    
    @passeggeriTrasportati.setter
    def passeggeriTrasportati (self, value):
        if value < 0 or value > (numeroMassimoPasseggeri-1):
            raise ValueError ("non valido")
        self.__passeggeriTrasportati=value
        return
    
    #-----------------------------------------------------
        
if __name__=="__main__":
    veicolo=Veicolo("AB123CD")
    print (veicolo)
    
    print(veicolo.numeroMassimoPasseggeri())
