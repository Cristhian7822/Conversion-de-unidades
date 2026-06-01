from .base_repository import BaseRepository
from model.unidad import Unit
from utils import get_resource_path
import json


class UnitsRepository(BaseRepository):
    """Repositorio que carga definiciones de unidades desde un archivo JSON."""

    def __init__(self) -> None:
        self._path: str = get_resource_path("recursos/datos/unidades.json")

    def load(self, category: str) -> list[Unit]:
        """Cargar unidades para una categoría específica o devolver todas las unidades."""
        with open(self._path, encoding="utf-8") as file:
            data = json.load(file)

        result: list[Unit] = []
        if category == "Todas":
            for category_name, units in data.items():
                for u in units:
                    result.append(
                        Unit(
                            name=u["nombre"],
                            symbol=u["simbolo"],
                            category=category_name,
                            factor=u["factor"]
                        )
                    )
            return result

        for category_name, units in data.items():
            if category_name != category:
                continue
            for u in units:
                result.append(
                    Unit(
                        name=u["nombre"],
                        symbol=u["simbolo"],
                        category=category,
                        factor=u["factor"]
                    )
                )
        return result
            