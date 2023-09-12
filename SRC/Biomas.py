import pandas as pd

class Biomas:   

    def __init__(self, file):
        self.doc_biomas = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        self.doc_biomas.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        self.doc_biomas.loc[self.doc_biomas['idBioma'] == llave, columna] = valor_nuevo