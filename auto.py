#Bruschi Ginevra
#4BS
# livello 1

#importare il file veicolo
from veicolo import*

#definire la classe auto numero massimo di passeggeri e numero di passeggeri trasportati,
class Auto(Veicolo):
    def __init__(self,numeroMassimoPasseggeri:int, passeggeriTrasportati:int):
        