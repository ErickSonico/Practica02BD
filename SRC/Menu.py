from Veterinarios import *
from Animales import *
from Biomas import *

class Menu:
    """Clase para poder mostrar y realizar opciones
    """

    
    def __init__(self, veterinarios, animales, biomas):
        """Método constructor de la clase Menu, recibe tres clases:
            + Veterinario 
            + Animales  
            + Biomas
        

        Args:
            veterinarios (Veterinarios): clase que nos ayuda a leer el csv de Veterinarios.
            animales (Animales): clase que nos ayuda a leer el csv de Animales.
            biomas (Biomas): clase que nos ayuda a leer el csv de Biomas.
        """
        self.veterinarios = veterinarios
        self.animales = animales
        self.biomas = biomas


    def selecciona_entidad(self, n):
        """Método que nos ayuda a seleccionar con que entidad trabajaremos:
            1 - Veterinarios
            2 - Animales
            3 - Biomas

        Args:
            n (int): Número que nos ayuda a seleccionar que con que entidad trabajaremos

        Raises:
            ValueError: Si el valor no es el esperado, números enteros.

        Returns:
            bool: Bandera para el menu.
        """
        
        if type(n) != int:
            raise ValueError("Debes de teclear un número entero")
        
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
        """Método que nos ayuda a seleccionar y realizar una acción:
            1 - Agregar
            2 - Consultar
            3 - Editar
            4 - Eliminar

        Args:
            n (int): Número que nos ayuda a seleccionar que operación se realizará.

        Raises:
            ValueError: Si el valor no es el esperado.
            

        Returns:
            bool: Bandera para el menu.
        """
        
        if type(n) != int:
            raise ValueError("Debes de teclear un número entero")
        
        if self.entidad is None:
            print("No se ha seleccionado una entidad\n")
            return False
        
        if n == 1: # Agregar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if len(rfc) > 13 or rfc == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                nombre = input("Nombre: ")
                if nombre == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                apellidoPaterno = input("Apellido Paterno: ")
                if apellidoPaterno == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                apellidoMaterno = input("Apellido Materno: ")
                if apellidoMaterno == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                genero = input("Genero: ")
                if genero == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                nacimiento = input("Anio de nacimiento: ")
                if nacimiento == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    telefono = int(input("Teléfono: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                email = input("Email: ")
                if "@" not in email:
                    print("El valor no es el esperado. El correo debe llevar @")
                    raise ValueError()
                calle = input("Calle: ")
                if calle == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroExt = int(input("Número Exterior: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroInt = int(input("Número Interior: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                colonia = input("Colonia: ")
                if colonia == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                estado = input("Estado: ")
                if estado == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                especialidad = input("Especialidad: ")
                if especialidad == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    salario = float(input("Salario: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                fechaIni = input("Fecha de Inicio: ")
                if fechaIni == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                fechaFin = input("Fecha de Fin: ")
                if fechaFin == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                self.entidad.agrega_veterinario({'rfc': rfc, 'nombre': nombre, 'apellido paterno': apellidoPaterno, 'apellido materno': apellidoMaterno, 
                                                 'genero': genero, 'nacimiento': nacimiento, 'telefono': telefono, 'email': email, 'calle': calle, 
                                                 'numero exterior': numeroExt, 'numero interior': numeroInt, 'colonia': colonia, 'estado': estado, 
                                                 'especialidad': especialidad, 'salario': salario, 'fecha de inicio': fechaIni, 'fecha de fin': fechaFin})
                self.entidad.guarda_datos()
                print("Veterinario guardado exitosamente")
                self.entidad = None
                self.operacion = None
                
            elif self.entidad == self.animales:
                try:
                    idAnimal = int(input("ID: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                nombreAnimal = input("Nombre: ")
                if nombreAnimal == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                especie = input("Especie: ")
                if especie == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    altura = float(input("Altura: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    peso = float(input("Peso: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                sexo = input("Sexo: ")
                if sexo == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                alimentacion = input("Alimentacion: ")
                if alimentacion == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                instruccionMed = input("Instruccion Medica: ")
                if instruccionMed == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroJaula = int(input("Numero de Jaula: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                self.entidad.agrega_animal({'idAnimal': idAnimal, 'nombre': nombreAnimal, 'especie': especie, 'altura': altura, 'peso': peso, 'sexo': sexo,
                                            'alimentacion': alimentacion, 'instruccion medica': instruccionMed, 'numero de jaula': numeroJaula})
                self.entidad.guarda_datos()
                print("Animal guardado exitosamente")
                self.entidad = None
                self.operacion = None
                
            elif self.entidad == self.biomas:
                try:
                    idBioma = int(input("ID: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                tipo = input("Tipo: ")
                if tipo == '':
                    raise ValueError("EL valor no es el esperado")
                clima = input("Clima: ")
                if clima == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    temperatura = float(input("Temperatura: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    cantidadJaulas = int(input("Numero de Jaulas: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroAnimales = int(input("Numero de Animales: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroCuidadores = int(input("Numero de Cuidadores: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    numeroVeterinaios = int(input("Numero de Veterinarios: "))
                except Exception:
                    print("El valor no es el esperado")
                    raise ValueError()
                self.entidad.agrega_bioma({'idBioma': idBioma, 'tipo': tipo, 'clima': clima, 'temperatura': temperatura, 'numero de jaulas': cantidadJaulas,
                                           'numero de animales': numeroAnimales, 'numero de cuidadores': numeroCuidadores, 'numero de veterinarios': numeroVeterinaios})
                self.entidad.guarda_datos()
                print("Bioma guardado exitosamente")
                self.entidad = None
                self.operacion = None
            
        elif n == 2: # Consultar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if rfc == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                try:
                    print('\n' + str(self.entidad.get_veterinario(rfc)) + '\n')
                except Exception:
                    print("Veterinario no encontrado")
                    raise ValueError()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.animales:
                try:
                    id = int(input("ID: "))
                except Exception:
                    raise ValueError("El valor tiene que ser numérico")
                try:
                    print('\n' + str(self.entidad.get_animal(id)) + '\n')
                except Exception:
                    print("Animal no encontrado")
                    raise ValueError()
                self.entidad = None
                self.operacion = None
            elif self.entidad == self.biomas:
                try:
                    id = int(input("ID: "))
                except Exception:
                    raise ValueError("El valor tiene que ser numérico")
                try:
                    print('\n' + str(self.entidad.get_bioma(id)) + '\n')
                except Exception:
                    print("Bioma no encontrado")
                    raise ValueError()
                self.entidad = None
                self.operacion = None

        elif n == 3: # Editar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if rfc == '' or not self.entidad.busca_veterinario(rfc):
                    print("El valor no es el esperado o no existe")
                    raise ValueError()
                columna = input("Atributo: ")
                if columna == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                valor = input("Valor: ")
                if valor == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                if self.entidad.pertenece_columna(columna):
                    self.entidad.actualiza_dato(rfc, columna, valor)
                    self.entidad.guarda_datos()
                    self.entidad = None
                    self.operacion = None
                else:
                    print("El atributo no existe")
            elif self.entidad == self.animales or self.entidad == self.biomas:
                try:
                    id = int(input("ID: "))
                except Exception:
                    print("El valor tiene que ser numérico")
                    raise ValueError()
                if not self.entidad.busca_instancia(id):
                    print("ID inexistente")
                    raise ValueError
                columna = input("Atributo: ")
                if columna == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                valor = input("Valor: ")
                if valor == '':
                    print("El valor no es el esperado")
                    raise ValueError()
                if self.entidad.pertenece_columna(columna):
                    self.entidad.actualiza_dato(id, columna, valor)
                    self.entidad.guarda_datos()
                    self.entidad = None
                    self.operacion = None
                else:
                    print("El atributo no existe")

        elif n == 4: # Eliminar
            if self.entidad == self.veterinarios:
                rfc = input("RFC: ")
                if rfc == '':
                    print("El valor no es esperado")
                    raise ValueError()
                if self.entidad.busca_veterinario(rfc):
                    self.entidad.elimina_veterinario(rfc)
                    self.entidad.guarda_datos()
                    self.entidad = None
                    self.operacion = None
                else:
                    print("Veterinario no encontrado para eliminar")
            elif self.entidad == self.animales:
                try:
                    id = int(input("ID: "))
                except Exception:
                    print("El valor tiene que ser numérico")
                    raise ValueError()
                if self.entidad.busca_instancia(id):
                    self.entidad.elimina_animal(id)
                    self.entidad.guarda_datos()
                    self.entidad = None
                    self.operacion = None
                else:
                    print("Animal no encontrado para eliminar")
            elif self.entidad == self.biomas:
                try:
                    id = int(input("ID: "))
                except Exception:
                    print("El valor tiene que ser numérico")
                    raise ValueError()
                if self.entidad.busca_instancia(id):
                    self.entidad.elimina_bioma(id)
                    self.entidad.guarda_datos()
                    self.entidad = None
                    self.operacion = None
                else:
                    print("Bioma no encontrado para eliminar")

        return True