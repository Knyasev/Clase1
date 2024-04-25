from enum import Enum

class TipoEstadoCivil(Enum):
    SOLTERO = 'Soltero'
    CASADO = 'Casado'
    DIVORCIADO = 'Divorciado'
    VIUDO = 'Viudo'

    def serialize(self):
        return self.name