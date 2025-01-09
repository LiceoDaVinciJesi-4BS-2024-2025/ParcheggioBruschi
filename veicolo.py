#Bruschi Ginevra
#4BS
# classe veicolo

listaMarcheAuto=["ferrari","lamborghini","maserati","audi","alfaromeo","mercedes"]
listaMarcheMoto=["honda","suzuki","ktm","lambretta","harley","guzzi"]

listaColori=["nero", "bianco", "rosso", "blu", "viola", "grigio", "giallo", "celeste"]
listaAlimentazione=["benzina","disel","metano", "elettrico","ibrido"]

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
    
    #definire le property
    @property
    def marca(self):
        return
    
    @property
    def modello():
        
    @property
    def colore(self):
        return
    
    @property
    def cilindrata(self):
        return
    
    @property
    def alimentazione(self):
        return
        
    #definire le setter
    @marca.setter
    def marca(self,value):
        if 
    
    