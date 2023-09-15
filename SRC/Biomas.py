import pandas as pd

class Biomas:   
    """Clase que ayuda a leer cvs de la entidad Animal
    """

    def __init__(self, file):
        """Metodo constructor que recibe archivos csv para su edicion y manejo de biomas.

        Args:
            file (.csv): archivo que se editara
        """
        self.doc_biomas = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        """Metodo que guarda los datos en el csv
        """
        self.doc_biomas.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        """Metodo que recibe tres datos para actualizarlos en el csv

        Args:
            llave (int): llave de la entidad
            columna (str): valor a actualizar
            valor_nuevo (int, srt, float): nuevo valor para actualizar
        """
        self.doc_biomas.loc[self.doc_biomas['idBioma'] == llave, columna] = valor_nuevo

    def agrega_bioma(self,renglon):
        """Metodo que agrega un nuevo renglon a la csv de la entidad

        Args:
            renglon (dicc{}): el reglon a introducir en el csv
        """
        self.doc_biomas.loc[len(self.doc_biomas)] = renglon

    def elimina_bioma(self,llave):
        """Método que elimina un reglon del csv de la entidad

        Args:
            llave (int): reglon a eliminar
        """
        self.doc_biomas = self.doc_biomas.drop(self.doc_biomas[self.doc_biomas['idBioma'] == llave].index)

    def get_bioma(self,llave):
        """Metdo que devueleve un reglon del csv de la entidad

        Args:
            llave (int): renglon a devolver

        Returns:
            dicc{}: reglon que devuelve
        """
        return self.doc_biomas.loc[self.doc_biomas['idBioma'] == llave].to_dict('records')[0]