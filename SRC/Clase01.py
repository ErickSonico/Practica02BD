import os.path
from ReadCSV import *

dir = os.path.dirname(__file__)
file = dir + '/Veterinarios.csv'
lector = ReadCSV()
lector.leerCSV(file)

print(lector.diccVeterinario["rfc","nombre","direccion"])


