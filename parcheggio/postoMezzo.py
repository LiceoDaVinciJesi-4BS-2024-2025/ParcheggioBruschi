#Bruschi Ginevra
#4BS
# livello 2

#importare la classe veicolo
from veicolo import Veicolo
#importare il modulo datetime
import datetime

#definire la classe
class PostoMezzo(Veicolo):
     def __init__(self, targa, postoLibero:bool,):
        super().__init__(targa)
        
        

#Definire in esso se è libero oppure occupato, la targa del mezzo che lo occupa, la data/ora di termine occupazione.
