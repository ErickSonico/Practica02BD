import os.path
from Veterinarios import *
from Animales import *
from Biomas import *

class Menu:

    def __init__(self, veterinarios, animales, biomas):
        self.veterinarios = veterinarios
        self.animales = animales
        self.biomas = biomas


    def selecciona_entidad(self, n):
        if n == 1:
            self.entidad = self.veterinarios
        elif n == 2:
            self.entidad = self.animales
        elif n == 3:
            self.entidad = self.biomas
        else:
            print("No existe esa entidad\n")
            return False
        return True

    def selecciona_operacion(self, n):
        if self.entidad is None:
            print("No se ha seleccionado una entidad\n")
            return False
        if n == 1: # Agregar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                nombre = input("Nombre: ")
                direccion = input("Direccion: ")
                self.entidad.agrega_veterinario({'rfc': rfc, 'nombre': nombre, 'direccion': direccion})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.animales:
                idAnimal = int(input("ID: "))
                especie = input("Especie: ")
                edad = input("Edad: ")
                peso = input("Peso: ")
                self.entidad.agrega_animal({'idAnimal': idAnimal, 'especie': especie, 'edad': edad, 'peso': peso})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.biomas:
                idBioma = int(input("ID: "))
                clima = input("Clima: ")
                temperatura = input("Temperatura: ")
                self.entidad.agrega_bioma({'idBioma': idBioma, 'clima': clima, 'temperatura': temperatura})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            
        elif n == 2: # Consultar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                print('\n' + str(self.entidad.get_veterinario(rfc)) + '\n')
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.animales:
                id = int(input("ID: "))
                print('\n' + str(self.entidad.get_animal(id)) + '\n')
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.biomas:
                id = int(input("ID: "))
                print('\n' + str(self.entidad.get_bioma(id)) + '\n')
                self.entidad = None
                self.operacion = None

        elif n == 3: # Editar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                columna = input("Columna: ")
                valor = input("Valor: ")
                self.entidad.actualiza_dato(rfc, columna, valor)
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.animales or self.entidad == self.biomas:
                id = int(input("ID: "))
                columna = input("Columna: ")
                valor = input("Valor: ")
                self.entidad.actualiza_dato(id, columna, valor)
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None

        elif n == 4: # Eliminar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                self.entidad.elimina_veterinario(rfc)
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.animales:
                id = int(input("ID: "))
                self.entidad.elimina_animal(id)
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.biomas:
                id = int(input("ID: "))
                self.entidad.elimina_bioma(id)
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None

        return True