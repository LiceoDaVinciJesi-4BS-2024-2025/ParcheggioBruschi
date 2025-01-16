#Bruschi Ginevra
#4BS
# classe veicolo

listaMarcheAuto=["ferrari","lamborghini","maserati","audi","alfaromeo","mercedes"]
listaMarcheMoto=["honda","suzuki","ktm","lambretta","harley","guzzi"]

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
        
        # devi far si che sia valida
        listaTarga=[]
        for x in targa:
            listaTarga.append(x)
        
        for x in listaTarga:
            if listaTarga[0] and listaTarga[1] and listaTarga[5] and listaTarga[6] in lettereTarga and listaTarga[2] and listaTarga[3] and listaTarga[4] in numeriTarga:
                self.__targa = targa 
        
    #def  str
    def __str__(self):
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
        if value not in listaMarcheAuto or value not in listaMarcheMoto:
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
    veicolo=Veicolo("AB123CD")
    print(veicolo)
