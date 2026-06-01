from .categoria import Category
from .unidad import Unit

class LinearCategory(Category):
    """Categoría de conversión lineal para unidades que convierten por razón de factores."""

    def __init__(self, units: list[Unit]) -> None:
        self.units = units

    def _get_factor(self, unit_name: str) -> float:
        for unit in self.units:
            if unit.name == unit_name:
                return unit.factor
        raise ValueError(f"Unidad no encontrada: {unit_name}")

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        input_factor = self._get_factor(from_unit)
        output_factor = self._get_factor(to_unit)
        return value * (input_factor / output_factor)

    def get_units(self) -> list[Unit]:
        """Devolver los objetos de unidad en esta categoría lineal."""
        return self.units