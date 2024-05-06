from enum import Enum


class CustomerType(Enum):
    OCASIONAL = 1;
    MAYORISTA = 2;

    def __str__(self):
        return self.name.replace('_', ' ').capitalize()
