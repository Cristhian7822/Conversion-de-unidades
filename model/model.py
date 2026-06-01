import csv
from model.categoria_lineal import LinearCategory
from model.historial import HistoryRecord
from model.categoria_temperatura import TemperatureCategory
from repositorios.unidades_repository import UnitsRepository
from repositorios.historial_repository import HistoryRepository
from repositorios.teoria_repository import TheoryRepository

class Model:
    """Modelo principal de la aplicación que maneja la lógica de conversión y persistencia."""

    def __init__(self) -> None:
        self._units_repository = UnitsRepository()
        self._history_repository = HistoryRepository()
        self._theory_repository = TheoryRepository()
        self._history: list[list[HistoryRecord | str]] = self._history_repository.load()

        all_units = self._units_repository.load("Todas")
        self.categories = {
            "Longitud": LinearCategory([u for u in all_units if u.category == "Longitud"]),
            "Masa": LinearCategory([u for u in all_units if u.category == "Masa"]),
            "Volumen": LinearCategory([u for u in all_units if u.category == "Volumen"]),
            "Tiempo": LinearCategory([u for u in all_units if u.category == "Tiempo"]),
            "Velocidad": LinearCategory([u for u in all_units if u.category == "Velocidad"]),
            "Temperatura": TemperatureCategory([u for u in all_units if u.category == "Temperatura"])
        }

    def convert(self, category: str, from_unit: str, to_unit: str, value: float) -> float:
        """Convertir un valor numérico de una unidad a otra dentro de la categoría indicada."""
        if category not in self.categories:
            raise ValueError(f"Categoría no soportada: {category}")
        return self.categories[category].convert(value, from_unit, to_unit)

    def generate_explanation(self, category: str, from_unit: str, to_unit: str, value: float, result: float) -> str:
        """Generar una explicación detallada de la conversión para las unidades indicadas."""
        if category in ["Longitud", "Masa", "Volumen", "Tiempo", "Velocidad"]:
            units = self._units_repository.load(category)
            input_factor = None
            output_factor = None
            for unit in units:
                if unit.name == from_unit:
                    input_factor = unit.factor
                if unit.name == to_unit:
                    output_factor = unit.factor
            if input_factor is None:
                raise ValueError(f"Unidad de entrada no válida: {from_unit}")
            if output_factor is None:
                raise ValueError(f"Unidad de salida no válida: {to_unit}")
            direct_factor = input_factor / output_factor

            explanation = (
                f"Explicación de la conversión de {value} {from_unit} a {to_unit}:\n\n"
                f"1) Categoría: Ambas unidades pertenecen a la categoría '{category}', por lo que la conversión es válida.\n"
                f"2) Factores relativos: el factor de la unidad de entrada ({from_unit}) es {input_factor} y el de la unidad de salida ({to_unit}) es {output_factor}.\n"
                "   Estos factores representan la relación de cada unidad respecto a una unidad base común.\n"
                f"3) Método de conversión: para pasar de {from_unit} a la unidad base se multiplica por {input_factor}, y para pasar de la unidad base a {to_unit} se divide entre {output_factor}.\n"
                "   Para simplificar se calcula un factor de conversión directo entre las dos unidades.\n"
                f"4) Cálculo del factor directo: factor_directo = factor_entrada / factor_salida = {input_factor} / {output_factor} = {direct_factor}.\n"
                f"   Esto significa que 1 {from_unit} equivale a {direct_factor} {to_unit}.\n"
                f"5) Aplicando al valor: resultado = {value} * {direct_factor} = {result} {to_unit}.\n\n"
            )
            return explanation
        if category == "Temperatura":
            if from_unit == to_unit:
                return (
                    f"Explicación de la conversión de {value} {from_unit} a {to_unit}:\n\n"
                    f"1) Ambas unidades son iguales ({from_unit}).\n"
                    f"2) El valor permanece igual: {value} {from_unit} = {result} {to_unit}.\n"
                )
            explanation = (
                f"Explicación de la conversión de {value} {from_unit} a {to_unit}:\n\n"
                f"1) Categoría: Ambas unidades pertenecen a la categoría 'Temperatura', por lo que la conversión es válida.\n"
                "2) Método de conversión: La conversión entre unidades de temperatura no se basa en factores multiplicativos simples debido a las diferencias en los puntos de congelación y ebullición del agua.\n"
                "   En su lugar, se utilizan fórmulas específicas para cada par de unidades.\n"
                f"3) Fórmula aplicada: Para convertir de {from_unit} a {to_unit}, se aplicó la fórmula correspondiente:\n"
            )
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                explanation += f"   °F = (°C * 9/5) + 32\n   Resultado: °F = ({value} * 9/5) + 32 = {result} °F\n"
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                explanation += f"   K = °C + 273.15\n   Resultado: K = {value} + 273.15 = {result} K\n"
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                explanation += f"   °C = (°F - 32) * 5/9\n   Resultado: °C = ({value} - 32) * 5/9 = {result} °C\n"
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                explanation += f"   K = (°F - 32) * 5/9 + 273.15\n   Resultado: K = ({value} - 32) * 5/9 + 273.15 = {result} K\n"
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                explanation += f"   °C = K - 273.15\n   Resultado: °C = {value} - 273.15 = {result} °C\n"
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                explanation += f"   °F = (K - 273.15) * 9/5 + 32\n   Resultado: °F = ({value} - 273.15) * 9/5 + 32 = {result} °F\n"
            elif from_unit == "Celsius" and to_unit == "Rankine":
                explanation += f"   °Ra = (°C + 273.15) * 1.8\n   Resultado: °Ra = ({value} + 273.15) * 1.8 = {result} °Ra\n"
            elif from_unit == "Fahrenheit" and to_unit == "Rankine":
                explanation += f"   °Ra = °F + 459.67\n   Resultado: °Ra = {value} + 459.67 = {result} °Ra\n"
            elif from_unit == "Kelvin" and to_unit == "Rankine":
                explanation += f"   °Ra = K * 1.8\n   Resultado: °Ra = {value} * 1.8 = {result} °Ra\n"
            elif from_unit == "Rankine" and to_unit == "Celsius":
                explanation += f"   °C = (°Ra - 491.67) * 5/9\n   Resultado: °C = ({value} - 491.67) * 5/9 = {result} °C\n"
            elif from_unit == "Rankine" and to_unit == "Fahrenheit":
                explanation += f"   °F = °Ra - 459.67\n   Resultado: °F = {value} - 459.67 = {result} °F\n"
            elif from_unit == "Rankine" and to_unit == "Kelvin":
                explanation += f"   K = °Ra / 1.8\n   Resultado: K = {value} / 1.8 = {result} K\n"
            else:
                explanation += "   No se encontró una fórmula de conversión para estas unidades de temperatura.\n"
            return explanation
        raise ValueError(f"Categoría no soportada: {category}")

    def add_history(self, record: HistoryRecord) -> None:
        """Guardar un registro de historial en memoria y persistirlo."""
        label = f"{record.input_value} {record.input_unit} -> {record.output_value} {record.output_unit}"
        self._history.append([record, label])
        self._history_repository.add(record)

    def delete_history(self, record: HistoryRecord) -> None:
        """Eliminar un registro de historial de la memoria y del almacenamiento persistente."""
        self._history = [entry for entry in self._history if not (entry[0] == record)]
        self._history_repository.remove(record)

    def get_history(self) -> list[list[HistoryRecord | str]]:
        """Devolver los registros de historial cargados."""
        return self._history

    def export_history_csv(self, path: str, history=None) -> None:
        """Exportar registros de historial a un archivo CSV."""
        # Normalizar el parámetro `history` a una lista de HistoryRecord
        if history is None:
            records = [entry for entry, _ in self._history]
        elif isinstance(history, HistoryRecord):
            records = [history]
        elif isinstance(history, list):
            records = []
            for item in history:
                # aceptar tanto HistoryRecord como pares [record, label]
                if isinstance(item, HistoryRecord):
                    records.append(item)
                elif isinstance(item, (list, tuple)) and len(item) >= 1 and isinstance(item[0], HistoryRecord):
                    records.append(item[0])
                else:
                    raise ValueError("Lista de historial contiene elementos no válidos para exportar")
        else:
            raise ValueError("Parámetro 'history' no válido para exportación CSV")

        with open(path, mode="w", encoding="utf-8", newline="") as output_file:
            writer = csv.writer(output_file)
            writer.writerow(["Unidad entrada", "Unidad salida", "Valor entrada", "Valor salida", "Fecha de conversión"])
            for record in records:
                writer.writerow([
                    record.input_unit,
                    record.output_unit,
                    record.input_value,
                    record.output_value,
                    record.timestamp,
                ])

    def get_units(self) -> list:
        """Devolver todas las unidades desde el repositorio."""
        return self._units_repository.load('Todas')

    def get_theory(self, category: str) -> dict:
        """Devolver el contenido teórico para una categoría."""
        return self._theory_repository.load(category)

    def get_tables(self, category: str) -> dict:
        """Devolver el contenido de tablas para una categoría."""
        return self._theory_repository.load_tables(category)
