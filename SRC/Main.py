import os.path
from Veterinarios import *
from Animales import *
from Biomas import *
from Menu import *

dir = os.path.dirname(__file__)
file_vet = dir + '/Veterinarios.csv'
veterinarios = Veterinarios(file_vet)

file_animales = dir+ '/Animales.csv'
animales = Animales(file_animales)

file_biomas = dir + '/Biomas.csv'
biomas = Biomas(file_biomas)

menu = Menu(veterinarios,animales,biomas)
entidad = 0

print('\n')
while True:
    print('Selecciona la entidad con la que deseas trabajar:')
    print('1. Veterinarios')
    print('2. Animales')
    print('3. Biomas')
    print('4. Salir')
    try:
        entidad = int(input(''))
        if entidad == 4:
            break
    except ValueError:
        print('Opción no válida\n')
        continue
    if(not menu.selecciona_entidad(entidad)):
        continue
    print('Selecciona la operación que deseas realizar:')
    print('1. Agregar')
    print('2. Consultar')
    print('3. Editar')
    print('4. Eliminar')
    try:
        menu.selecciona_operacion(int(input('')))
    except ValueError:
        print('Opción no válida\n')