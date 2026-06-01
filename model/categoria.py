from abc import ABC, abstractmethod
from .unidad import Unit

class Category(ABC):
    _name: str
    _units: list[Unit]

    def get_units(self) -> list[Unit]:
        """Devolver las unidades que pertenecen a esta categoría."""
        return self._units

    @abstractmethod
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convertir un valor de una unidad a otra dentro de la categoría."""
        raise NotImplementedError
