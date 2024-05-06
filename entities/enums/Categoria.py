from enum import Enum


class Categoria(Enum):
    ACCESORIO_ELECTRONICO = 1
    ROPA = 2
    COMPUTADORES = 3
    CELULARES = 4

    def __str__(self):
        return self.name.replace('_', ' ').capitalize()