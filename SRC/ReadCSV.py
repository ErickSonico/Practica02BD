import csv
import os.path
import pandas as pd

class ReadCSV:

    diccVeterinario = {}
    diccAnimal      = {}
    diccBioma       = {}
    
    def leerCSV(self, file):
        self.diccVeterinario = pd.read_csv(file)
        
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
        