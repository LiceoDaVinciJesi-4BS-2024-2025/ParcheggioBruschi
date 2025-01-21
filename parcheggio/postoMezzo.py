#Bruschi Ginevra
#4BS
# livello 2

#importare la classe veicolo
from veicolo import Veicolo
#importare il modulo datetime
import datetime

#definire la classe
class PostoMezzo(Veicolo):
     def __init__(self, targa):
        super().__init__(targa)
        