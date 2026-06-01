import json
from pathlib import Path
from repositorios.base_repository import BaseRepository
from model.historial import HistoryRecord
from utils import get_resource_path

class HistoryRepository(BaseRepository):
    """Repositorio que carga y guarda registros de historial en un archivo JSON."""

    def __init__(self) -> None:
        self._path = get_resource_path("recursos/datos/historial.json")

    def _ensure_file(self) -> None:
        path = Path(self._path)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text("{}", encoding="utf-8")

    def _load_json(self) -> dict:
        self._ensure_file()
        try:
            with open(self._path, encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            with open(self._path, "w", encoding="utf-8") as file:
                json.dump({}, file, indent=4, ensure_ascii=False)
            return {}

    def _save_json(self, data: dict) -> None:
        with open(self._path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load(self) -> list[list[HistoryRecord | str]]:
        """Cargar registros de historial almacenados y preservar la clave de etiqueta."""
        data = self._load_json()

        history: list[list[HistoryRecord | str]] = []
        for label, item in data.items():
            history.append([
                HistoryRecord(
                    input_unit=item["unidad_entrada"],
                    output_unit=item["unidad_salida"],
                    input_value=item["valor_entrada"],
                    output_value=item["valor_salida"],
                    timestamp=item["timestamp"]
                ),
                label
            ])
        return history

    def add(self, record: HistoryRecord) -> None:
        """Agregar un registro de historial al archivo JSON."""
        data = self._load_json()

        data[f"{record.input_value} {record.input_unit} -> {record.output_value} {record.output_unit}"] = {
            "unidad_entrada": record.input_unit,
            "unidad_salida": record.output_unit,
            "valor_entrada": record.input_value,
            "valor_salida": record.output_value,
            "timestamp": record.timestamp
        }

        self._save_json(data)

    def remove(self, record: HistoryRecord) -> None:
        """Eliminar un registro de historial del archivo JSON."""
        record_key = f"{record.input_value} {record.input_unit} -> {record.output_value} {record.output_unit}"
        data = self._load_json()

        if record_key in data:
            del data[record_key]

        self._save_json(data)