from PySide6.QtWidgets import QMdiSubWindow, QSpinBox, QMessageBox, QCompleter, QInputDialog, QWidget
from PySide6.QtGui import QDoubleValidator
from PySide6.QtCore import Qt, Signal
from views.ui.archivos_py.ui_ventana_conversion import Ui_Form

class ConversionView(QMdiSubWindow, Ui_Form):
    """Vista para subventanas de conversión, incluyendo controles de entrada y salida."""

    conversion_realized = Signal(str, str, float, float, str)
    closed = Signal()

    def __init__(self, category: str) -> None:
        super().__init__()
        widget = QWidget()
        self.setWidget(widget)
        self.setupUi(widget)
        self.category = category
        self.numero_conversion.setValidator(QDoubleValidator())
        self.spin_decimals = QSpinBox()
        self.spin_decimals.setRange(0, 10)

    def show_result(self, result: float | None = None, explanation: str | None = None) -> None:
        """Mostrar el resultado de la conversión o mostrar un error cuando falte la salida."""
        if result is None or explanation is None:
            self.show_error("Para ver los pasos primero realice una conversión.")
            return
        if not self.chk_mostrar_pasos.isChecked():
            self.campo_explicacion.setText(f"Resultado: {result:.{self.spin_decimals.value()}f} {self.comboBox_destino.currentText()}")
        else:
            self.campo_explicacion.setText(explanation)

    def show_error(self, message: str) -> None:
        """Mostrar un mensaje de error en un cuadro de diálogo modal."""
        QMessageBox.critical(self, "Error", message)

    def populate_units(self, units: list) -> None:
        """Poblar los cuadros combinados de entrada y salida con las unidades proporcionadas."""
        self.comboBox_entrada.addItems([u.name for u in units])
        self.comboBox_entrada.setEditable(True)
        self.comboBox_destino.addItems([u.name for u in units])
        self.comboBox_destino.setEditable(True)

        input_completer = QCompleter(u.name for u in units)
        input_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.comboBox_entrada.setCompleter(input_completer)

        output_completer = QCompleter(u.name for u in units)
        output_completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.comboBox_destino.setCompleter(output_completer)

    def decimal_preference(self, parent=None) -> int:
        """Pedir al usuario el número de decimales preferido."""
        if parent is None:
            parent = self.widget() if self.widget() is not None else self
        decimals, ok = QInputDialog.getInt(
            parent,
            "Decimales",
            "Ingrese el número de decimales para el resultado:",
            minValue=0,
            maxValue=10,
            value=2
        )
        if ok:
            self.spin_decimals.setValue(decimals)
        else:
            self.spin_decimals.setValue(2)
        return self.spin_decimals.value()

    def closeEvent(self, event) -> None:
        self.closed.emit()
        super().closeEvent(event)