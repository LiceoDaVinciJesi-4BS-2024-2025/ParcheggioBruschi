#Bruschi Ginevra
#4BS
# classe veicolo

listaMarche=["ferrari","lamborghini","maserati","audi","alfaromeo","mercedes","honda","suzuki","ktm","lambretta","harley","guzzi"]


listaColori=["nero", "bianco", "rosso", "blu", "viola", "grigio", "giallo", "celeste"]
listaAlimentazione=["benzina","disel","metano", "elettrico","ibrido"]

lettereTarga="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeriTarga="123456789"

#definire la classe
class Veicolo:
    def __init__(self, targa:str):
        self.__marca="maserati"
        self.__modello="MC20Cielo"
        self.__colore="grigio"
        self.__cilindrata=4000
        self.__alimentazione="ibrido"
                     
        if len(targa) != 7:
            raise ValueError ("la targa deve essere di sette caratteri")
        
        if targa[0] in lettereTarga and targa[1] in lettereTarga and targa[5] in lettereTarga and targa[6] in lettereTarga and targa[2] in numeriTarga and targa[3] in numeriTarga and targa[4] in numeriTarga:
                self.__targa = targa
        else:
            raise ValueError("Targa errata")
        
        for x in targa:
            if targa[0] in lettereTarga and targa[1] in lettereTarga and targa[5] in lettereTarga and targa[6] in lista in targa and targa[2] and targa[3] and targa[4] in numeriTarga:
                self.__targa = targa 

        
    #def  str
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    def __repr__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    #definire le property--------------------------------------
    @property
    def marca(self):
        return marca
    
    @property
    def modello():
        return modello
        
    @property
    def colore(self):
        return colore
    
    @property
    def cilindrata(self):
        return cilindrata
    
    @property
    def alimentazione(self):
        return alimentazione
    
    #solo questa non si può cambiare
    @property
    def targa (self):
        return self.__targa
        
    #definire le setter------------------------------
    @marca.setter
    def marca(self,value):
        if value not in listaMarche:
            raise ValueError ("il tipo di marca non è presente nelle liste")
        self.__marca=value
        return
    
    @modello.setter
    def modello (self,value):
        self.__modello=value
        return
        
    
    @colore.setter
    def colore(self,value):
        if value not in listaColori:
            raise ValueError ("il colore non è disponibile")
        self.__colore=value
        return
    
    #intero positivo multiplo di 100
    @cilindrata.setter
    def cilindrata (self,value):
        if value < 100 and value%100 != 0:
            raise ValueError ("il valore della cilindrata non è valido")
        self.__cilindrata=value
        return
    
    
    @alimentazione.setter
    def alimentazione (self,value):
        if value not in listaAlimentazione:
            raise ValueError ("non esiste questo tipo di alimentazione")
        self.__alimentazione=value
        return
    
    #----------------------------------------------------------------------
    #ordinabili alfabeticamente per marca, modello e numericamente (dal più piccolo al più grande) per cilindrata.
    def __lt__(self, other):
        if self.__marca < other.__marca:
            return True
        elif self.__marca == other.__marca:
            if self.__modello < other.__modello:
                return True
            elif self.__modello == other.__modello:
                if self.__cilindrata < other.__cilindrata:
                    return True
                
        return False
    
    #-----------------------------------------------------------------------
    
if __name__=="__main__":
    veicolo1=Veicolo("AB123CD")
    print(veicolo1)
    print()
    veicolo2=Veicolo("AC342GF")
    listaVeicolo=[veicolo1,veicolo2]
    listaVeicolo.sort()
    print(listaVeicolo)
    
