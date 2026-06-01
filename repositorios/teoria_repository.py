from .base_repository import BaseRepository
from utils import get_resource_path
import json


class TheoryRepository(BaseRepository):
    """Repositorio que carga contenido teórico y tablas desde archivos JSON."""

    def __init__(self) -> None:
        self._theory_path: str = get_resource_path("recursos/datos/teoria.json")
        self._tables_path: str = get_resource_path("recursos/datos/tablas.json")

    def load(self, topic: str) -> dict:
        """Cargar contenido teórico que coincida con el tema proporcionado."""
        content: dict[str, str] = {}
        with open(self._theory_path, encoding="utf-8") as file:
            data = json.load(file)
        topic_lower = topic.lower()
        for topic_name, theory in data.items():
            if topic_name.lower() == topic_lower:
                content[topic] = theory
                return content
        return content

    def load_tables(self, topic: str) -> dict:
        """Cargar tablas que coincidan con el tema proporcionado."""
        content: dict[str, str] = {}
        with open(self._tables_path, encoding="utf-8") as file:
            data = json.load(file)
        for topic_name, tables in data.items():
            if topic_name == topic:
                content[topic] = tables
                return content
        return content