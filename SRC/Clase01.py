import os.path
from Veterinarios import *

dir = os.path.dirname(__file__)
file = dir + '/Veterinarios.csv'
veterinarios = Veterinarios(file)

print(veterinarios.docVeterinario["nombre"])

veterinarios.docVeterinario.loc[veterinarios.docVeterinario['rfc'] == 'GAVE23', 'nombre'] = 'Goku'
veterinarios.docVeterinario.to_csv(file, index=False)
