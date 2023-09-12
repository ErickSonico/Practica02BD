import csv
import os.path

class ReadCSV:
    current_directory = os.path.dirname(__file__)
    with open(current_directory + '/Veterinarios.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print("Datos Veterinarios")
        for line in csv_reader:
            print(line)
            print("Nombre:")
            print(line['nombre'])
        