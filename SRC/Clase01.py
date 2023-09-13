import os.path
from Veterinarios import *
from Animales import *
from Biomas import *

dir = os.path.dirname(__file__)
file_vet = dir + '/Veterinarios.csv'
veterinarios = Veterinarios(file_vet)

file_animales = dir+ '/Animales.csv'
animales = Animales(file_animales)

file_biomas = dir + '/Biomas.csv'
biomas = Biomas(file_biomas)

print('\n')
print(veterinarios.doc_veterinario)
veterinarios.actualiza_dato('GAVE23','nombre','Goku')
#veterinarios.guarda_datos();
print('\n')
print(veterinarios.doc_veterinario)

print('\n')
print(animales.doc_animales)
animales.actualiza_dato(4567,'edad',7)
#animales.guarda_datos()
print('\n')
print(animales.doc_animales)

print('\n')
print(biomas.doc_biomas)
biomas.actualiza_dato(22,'temperatura',1)
#biomas.guarda_datos()
print('\n')
print(biomas.doc_biomas)

#Ejemplo para agregar un nuevo bioma.
nuevo_bioma = {'idBioma':10,'clima':'arenoso','temperatura':60}
biomas.agrega_bioma(nuevo_bioma)
print(biomas.doc_biomas)