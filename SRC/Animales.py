import pandas as pd

class Animales:
    """Clase que ayuda a leer cvs de la entidad Animal
    """   

    def __init__(self, file):
        """Método constructor que recibe archivos csv para su edición y manejo de animales

        Args:
            file (.csv): archivo que se editará
        """
        self.doc_animales = pd.DataFrame(pd.read_csv(file))
        self.file = file

    def guarda_datos(self):
        """Método que guarda los datos en el csv
        """
        self.doc_animales.to_csv(self.file,index=False)
    
    def actualiza_dato(self,llave,columna,valor_nuevo):
        """Método que recibe tres datos para actualizarlos en el csv

        Args:
            llave (int): llave de la entidad
            columna (str): valor a actualizar
            valor_nuevo (int, srt, float): nuevo valor para actualizar
        """
        self.doc_animales.loc[self.doc_animales['idAnimal'] == llave, columna] = valor_nuevo

    def agrega_animal(self,renglon):
        """Método que agrega un nuevo renglón a la csv de la entidad

        Args:
            renglon (dicc{}): el reglón a introducir en el csv
        """
        self.doc_animales.loc[len(self.doc_animales)] = renglon

    def elimina_animal(self,llave):
        """Método que elimina un reglón del csv de la entidad

        Args:
            llave (int): reglón a eliminar
        """
        self.doc_animales = self.doc_animales.drop(self.doc_animales[self.doc_animales['idAnimal'] == llave].index)

    def get_animal(self,llave):
        """Método que devueleve un reglón del csv de la entidad

        Args:
            llave (int): renglón a devolver

        Returns:
            dicc{}: reglón que devuelve
        """
        return self.doc_animales.loc[self.doc_animales['idAnimal'] == llave].to_dict('records')[0]
    
    def busca_instancia(self,llave):
        """Método que verifica si un animal está en el archivo a partir de su llave

        Args:
            llave (int): id a buscar

        Returns:
            boolean: True si el animal está dentro del archivo. False e.o.c.
        """
        return llave in self.doc_animales.values
    
    def pertenece_columna(self,columna):
        """Método que checa si el argumento es una columna del dataframe

        Args:
            columna (str): atributo a checar

        Returns:
            boolean: True si el argumento es un nombre de columna. False e.o.c.
        """
        return columna in self.doc_animales.columns.values.tolist()