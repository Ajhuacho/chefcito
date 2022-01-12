#reprecentacion
class Receta:

    def __init__(self, nombre, complejidad):
        self.nombre = nombre
        self.complejidad = complejidad
        self.ingredientes = []
        self.pasos_de_preparacion = []
        self.hora_consumo = None#valores posibles desayuno , almuerzo y cena

    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def add_paso_preparacion(self, paso):#add= agregar    get = obtener
        self.pasos_de_preparacion.append(paso)

    def set_hora_consumo(self, hora_consumo):#set = pasar
        self.hora_consumo = hora_consumo
