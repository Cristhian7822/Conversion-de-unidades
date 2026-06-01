from .categoria import Category
from .unidad import Unit

class TemperatureCategory(Category):
    """Conversión de temperaturas entre Celsius, Fahrenheit, Kelvin y Rankine."""

    def __init__(self, units: list[Unit]) -> None:
        self.units = units

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convertir entre unidades de temperatura usando la fórmula adecuada."""
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
            elif to_unit == "Rankine":
                return (value + 273.15) * 1.8
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            elif to_unit == "Rankine":
                return value + 459.67
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            elif to_unit == "Rankine":
                return value * 1.8
        elif from_unit == "Rankine":
            if to_unit == "Celsius":
                return (value - 491.67) * 5/9
            elif to_unit == "Fahrenheit":
                return value - 459.67
            elif to_unit == "Kelvin":
                return value / 1.8
        raise ValueError(f"Conversión de temperatura no soportada de {from_unit} a {to_unit}.")

    def get_units(self) -> list[Unit]:
        """Devolver los objetos de unidad de temperatura compatibles."""
        return self.units

