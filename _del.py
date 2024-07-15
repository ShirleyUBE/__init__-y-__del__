class Persona:
    """
    La clase Persona representa una persona con un nombre y edad.

    El constructor (__init__) se encarga de inicializar los atributos de nombre y edad cuando se crea un objeto de la clase.
    El destructor (__del__) se encarga de realizar alguna limpieza o cierre de recursos cuando el objeto es eliminado de la memoria.
    """

    def __init__(self, nombre, edad):
        """
        Inicializa los atributos de nombre y edad de la persona.

        Args:
            nombre (str): El nombre de la persona.
            edad (int): La edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una nueva persona: {self.nombre}, {self.edad} años.")

    def __del__(self):
        """
        Realiza la limpieza o cierre de recursos cuando el objeto es eliminado.

        En este caso, simplemente imprime un mensaje indicando que el objeto ha sido eliminado.
        """
        print(f"La persona {self.nombre} ha sido eliminada.")


# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

# Eliminar los objetos de la clase Persona
del persona1
del persona2
