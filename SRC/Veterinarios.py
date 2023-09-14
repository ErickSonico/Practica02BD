import pandas as pd

class Veterinarios:   

    def __init__(self, file):
        self.doc_veterinario = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        self.doc_veterinario.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        self.doc_veterinario.loc[self.doc_veterinario['rfc'] == llave, columna] = valor_nuevo

    def agrega_veterinario(self,renglon):
        self.doc_veterinario.loc[len(self.doc_veterinario)] = renglon

    def elimina_veterinario(self,llave):
        self.doc_veterinario = self.doc_veterinario.drop(self.doc_veterinario[self.doc_veterinario['rfc'] == llave].index)

    def get_veterinario(self,llave):
        return self.doc_veterinario.loc[self.doc_veterinario['rfc'] == llave].to_dict('records')[0]