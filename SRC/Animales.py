import pandas as pd

class Animales:   

    def __init__(self, file):
        self.doc_animales = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        self.doc_animales.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        self.doc_animales.loc[self.doc_animales['idAnimal'] == llave, columna] = valor_nuevo

    def agrega_animal(self,renglon):
        self.doc_animales.loc[len(self.doc_animales)] = renglon