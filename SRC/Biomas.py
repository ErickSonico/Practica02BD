import pandas as pd

class Biomas:   

    def __init__(self, file):
        self.doc_biomas = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        self.doc_biomas.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        self.doc_biomas.loc[self.doc_biomas['idBioma'] == llave, columna] = valor_nuevo

    def agrega_bioma(self,renglon):
        self.doc_biomas.loc[len(self.doc_biomas)] = renglon

    def elimina_bioma(self,llave):
        self.doc_biomas = self.doc_biomas.drop(self.doc_biomas[self.doc_biomas['idBioma'] == llave].index)

    def get_bioma(self,llave):
        return self.doc_biomas.loc[self.doc_biomas['idBioma'] == llave]