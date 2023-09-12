import csv
import os.path
from typing import Any
import pandas as pd

class Veterinarios:   

    def __init__(self, file):
        self.docVeterinario = pd.DataFrame(pd.read_csv(file))

    def leerCSV(self, file):
        self.diccVeterinario = pd.DataFrame(pd.read_csv(file))
        
    '''
    with open(current_directory + '/Veterinarios.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("Datos Veterinarios")
        for line in csv_reader:
            print(line)
            print("Nombre:")
            print(line['rfc'])
            dic.setdefault(line['rfc'], line)
            print(dic)"
    '''        
        