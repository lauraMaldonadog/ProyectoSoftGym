class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'membresia': self.membresia}
