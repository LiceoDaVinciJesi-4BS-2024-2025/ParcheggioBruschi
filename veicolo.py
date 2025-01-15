#Bruschi Ginevra
#4BS
# classe veicolo

listaMarcheAuto=["ferrari","lamborghini","maserati","audi","alfaromeo","mercedes"]
listaMarcheMoto=["honda","suzuki","ktm","lambretta","harley","guzzi"]

listaColori=["nero", "bianco", "rosso", "blu", "viola", "grigio", "giallo", "celeste"]
listaAlimentazione=["benzina","disel","metano", "elettrico","ibrido"]

lettereTarga=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
numeriTarga=[1,2,3,4,5,6,7,8,9,0]

#definire la classe
class Veicolo:
    def __init__(self, targa:str):
        self.__marca="maserati"
        self.__modello="MC20Cielo"
        self.__colore="grigio"
        self.__cilindrata=4000
        self.__alimentazione="ibrido"
        self.__targa= targa# devi far si che sia valida
        
    #def  str
    def __str__(self):
        return self.__class__.__name__ + str(self.__dict__)
    
    #definire le property--------------------------------------
    @property
    def marca(self):
        return
    
    @property
    def modello():
        return
        
    @property
    def colore(self):
        return
    
    @property
    def cilindrata(self):
        return
    
    @property
    def alimentazione(self):
        return
        
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
    
    #-----------------------------------------------------------------------