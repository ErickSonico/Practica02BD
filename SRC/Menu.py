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
        
        if n != int:
            raise ValueError("Debes de telcear un numero entero")
        
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
        if n != int:
            raise ValueError("Debes de telcear un numero entero")
        
        if self.entidad is None:
            print("No se ha seleccionado una entidad\n")
            return False
        
        if n == 1: # Agregar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if rfc != str:
                    raise ValueError("El valor no es el esperado")
                nombre = input("Nombre: ")
                if nombre != str:
                    raise ValueError("El valor no es el esperado")
                apellidoPaterno = input("Apellido Paterno: ")
                if apellidoPaterno != str:
                    raise ValueError("El valor no es el esperado")
                apellidoMaterno = input("Apellido Materno: ")
                if apellidoMaterno != str:
                    raise ValueError("El valor no es el esperado")
                genero = input("Genero: ")
                if genero != str:
                    raise ValueError("El valor no es el esperado")
                nacimiento = input("Anio de nacimiento: ")
                if nacimiento != str:
                    raise ValueError("El valor no es el esperado")
                telefono = int(input("Telefono: "))
                if telefono != int:
                    raise ValueError("El valor no es el esperado")
                email = input("Email: ")
                if email != str:
                    raise ValueError("El valor no es el esperado")
                calle = input("Calle: ")
                if calle != str:
                    raise ValueError("El valor no es el esperado")
                numeroExt = int(input("Numero Exterior: "))
                if numeroExt != int:
                    raise ValueError("El valor no es el esperado")
                numeroInt = int(input("Numero Interior: "))
                if numeroInt != int:
                    raise ValueError("El valor no es el esperado")
                colonia = input("Colonia: ")
                if colonia != str:
                    raise ValueError("El valor no es el esperado")
                estado = input("Estado: ")
                if estado != str:
                    raise ValueError("El valor no es el esperado")
                especialidad = input("Especiealidad: ")
                if especialidad != str:
                    raise ValueError("El valor no es el esperado")
                salario = float(input("Salario: "))
                if salario != float:
                    raise ValueError("El valor no es el esperado")
                fechaIni = input("Fecha de Inicio: ")
                if fechaIni != str:
                    raise ValueError("El valor no es el esperado")
                fechaFin = input("Fecha de Fin: ")
                if fechaFin != str:
                    raise ValueError("El valor no es el esperado")
                self.entidad.agrega_veterinario({'rfc': rfc, 'nombre': nombre, 'apellido paterno': apellidoPaterno, 'apellido materno': apellidoPaterno, 
                                                 'genero': genero, 'nacimiento': nacimiento, 'telefono': telefono, 'email': email, 'calle': calle, 
                                                 'numero exterior': numeroExt, 'numero interior': numeroInt, 'colonia': colonia, 'estado': estado, 
                                                 'especialidad': especialidad, 'salario': salario, 'fecha de inicio': fechaIni, 'fecha de fin': fechaFin})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
                
            elif self.entidad == self.animales:
                idAnimal = input("ID: ")
                if idAnimal != int:
                    raise ValueError("El valor no es el esperado")
                nombreAnimal = input("Nombre: ")
                if nombreAnimal != str:
                    raise ValueError("El valor no es el esperado")
                especie = input("Especie: ")
                if especie != str:
                    raise ValueError("El valor no es el esperado")
                altura = input("Altura: ")
                if altura != float:
                    raise ValueError("El valor no es el esperado")
                peso = input("Peso: ")
                if peso != float:
                    raise ValueError("El valor no es el esperado")
                sexo = input("Sexo: ")
                if sexo != str:
                    raise ValueError("El valor no es el esperado")
                alimentacion = input("Alimentacion: ")
                if alimentacion != str:
                    raise ValueError("El valor no es el esperado")
                instruccionMed = input("Instraccion Medica: ")
                if instruccionMed != str:
                    raise ValueError("El valor no es el esperado")
                numeroJaula = input("Numero de Jaula: ")
                if numeroJaula != int:
                    raise ValueError("El valor no es el esperado")
                self.entidad.agrega_animal({'idAnimal': idAnimal, 'nombre': nombreAnimal, 'especie': especie, 'altura': altura, 'peso': peso, 'sexo': sexo,
                                            'alimentacion': alimentacion, 'instruccion medica': instruccionMed, 'numero de jaula': numeroJaula})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
                
            elif self.entidad == self.biomas:
                idBioma = int(input("ID: "))
                tipo = input("Tipo: ")
                clima = input("Clima: ")
                temperatura = input("Temperatura: ")
                cantidadJaulas = input("Numero de Jaulas: ")
                numeroAnimales = input("Numero de Animales: ")
                numeroCuidadores = input("Numero de Cuidadores")
                numeroVeterinaios = input("Numero de Veterinarios")
                self.entidad.agrega_bioma({'idBioma': idBioma, 'clima': clima, 'temperatura': temperatura})
                self.entidad.guarda_datos()
                self.entidad = None
                self.operacion = None
            
        elif n == 2: # Consultar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if rfc != str:
                    raise ValueError("El valor no es el esperado")
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