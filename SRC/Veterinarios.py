import pandas as pd

class Veterinarios:   

    def __init__(self, file):
        self.doc_veterinario = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        self.doc_veterinario.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        self.doc_veterinario.loc[self.doc_veterinario['rfc'] == llave, columna] = valor_nuevo
        