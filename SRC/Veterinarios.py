import pandas as pd

class Veterinarios:   

    def __init__(self, file):
        """Clase que ayuda a leer cvs de la entidad Veterinario
        """  
        self.doc_veterinario = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        """Metodo que guarda los datos en el csv
        """
        self.doc_veterinario.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        """Metodo que recibe tres datos para actualizarlos en el csv

        Args:
            llave (str): llave de la entidad
            columna (str): valor a actualizar
            valor_nuevo (int, srt, float): nuevo valor para actualizar
        """
        self.doc_veterinario.loc[self.doc_veterinario['rfc'] == llave, columna] = valor_nuevo

    def agrega_veterinario(self,renglon):
        """Metodo que agrega un nuevo renglon a la csv de la entidad

        Args:
            renglon (dicc{}): el reglon a introducir en el csv
        """
        self.doc_veterinario.loc[len(self.doc_veterinario)] = renglon

    def elimina_veterinario(self,llave):
        """Método que elimina un reglon del csv de la entidad

        Args:
            llave (int): reglon a eliminar
        """
        self.doc_veterinario = self.doc_veterinario.drop(self.doc_veterinario[self.doc_veterinario['rfc'] == llave].index)

    def get_veterinario(self,llave):
        """Metdo que devueleve un reglon del csv de la entidad

        Args:
            llave (int): renglon a devolver

        Returns:
            dicc{}: reglon que devuelve
        """
        return self.doc_veterinario.loc[self.doc_veterinario['rfc'] == llave].to_dict('records')[0]
    
    def busca_veterinario(self,llave):
        return llave in self.doc_veterinario.values