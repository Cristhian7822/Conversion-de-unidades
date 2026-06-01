from model.model import Model
from model.historial import HistoryRecord
from views.view_conversion import ConversionView
import datetime

class ConversionController:
    """Controlador para subventanas de conversión y la lógica de conversión."""

    def __init__(self, model: Model, category: str, reload_item: HistoryRecord | None = None) -> None:
        self.model = model
        self.category = category
        self.view = ConversionView(self.category)
        self.result: float | None = None
        self.explanation: str | None = None
        self.view.populate_units(self.model.categories[category].get_units())
        if reload_item is not None:
            self.reload_history_item(reload_item)

        self.view.pushButton_convertir.clicked.connect(self.perform_conversion)
        self.view.comboBox_destino.currentTextChanged.connect(self.on_unit_changed)
        self.view.conversion_realized.connect(self.save_history)
        self.view.chk_mostrar_pasos.stateChanged.connect(
            lambda checked: self.view.show_result(self.result, self.explanation)
        )

    def ask_decimals(self, parent=None) -> None:
        """Pedir al usuario el número de decimales preferido para la conversión."""
        self.view.decimal_preference(parent)

    def perform_conversion(self) -> None:
        """Ejecutar la conversión y mostrar el resultado."""
        try:
            value_text = self.view.numero_conversion.text()
            try:
                value = float(value_text)
            except ValueError:
                self.view.show_error("Error: Ingrese un número válido")
                return

            input_unit = self.view.comboBox_entrada.currentText()
            output_unit = self.view.comboBox_destino.currentText()
            result = self.model.convert(self.category, input_unit, output_unit, value)
            explanation = self.model.generate_explanation(self.category, input_unit, output_unit, value, result)
            self.result = result
            self.explanation = explanation
            self.view.show_result(self.result, self.explanation)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.view.conversion_realized.emit(input_unit, output_unit, value, result, timestamp)

        except Exception as error:
            self.view.show_error(str(error))

    def on_unit_changed(self) -> None:
        """Recalcular el resultado de conversión cuando cambia la unidad de salida seleccionada."""
        if self.result is None:
            return
        self.perform_conversion()

    def save_history(self, input_unit: str, output_unit: str, value: float, result: float, timestamp: str) -> None:
        """Guardar la última conversión en el repositorio de historial."""
        record = HistoryRecord(
            input_unit=input_unit,
            output_unit=output_unit,
            input_value=value,
            output_value=result,
            timestamp=timestamp
        )
        self.model.add_history(record)

    def reload_history_item(self, item: HistoryRecord) -> None:
        """Poblar la vista de conversión desde un registro de historial."""
        self.view.numero_conversion.setText(str(item.input_value))
        self.view.comboBox_entrada.setCurrentText(item.input_unit)
        self.view.comboBox_destino.setCurrentText(item.output_unit)
        self.result = item.output_value
        self.explanation = f"Resultado: {item.output_value}"
        self.view.campo_explicacion.setText(self.explanation)   