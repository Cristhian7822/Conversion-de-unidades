from views.ui.archivos_py.dialog_datos_historial import Ui_Dialog
from PySide6.QtWidgets import QDialog
from model.historial import HistoryRecord

class HistoryDialog(QDialog, Ui_Dialog):
    """Diálogo para inspeccionar y tomar acciones sobre un registro de historial."""

    def __init__(self, record: HistoryRecord) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Historial")
        self.btn_recargar.clicked.connect(self.on_reload)
        self.btn_exportar.clicked.connect(self.on_export)
        self.btn_eliminar.clicked.connect(self.on_delete)
        self.btn_accept.clicked.connect(self.accept)
        self.record = record
        self.lbl_tiempo.setText(f"Fecha: {record.timestamp}")
        self.lbl_unidad_entrada.setText(f"Unidad de entrada: {record.input_unit}")
        self.lbl_unidad_salida.setText(f"Unidad de salida: {record.output_unit}")
        self.lbl_valor.setText(f"Valor de entrada: {record.input_value}")
        self.lbl_resultado.setText(f"Valor de salida: {record.output_value}")
        self.decision: list | None = None

    def on_reload(self) -> None:
        """Marcar el registro para recargar en el controlador principal."""
        self.accept()
        self.decision = [self.record, "recargar"]

    def on_delete(self) -> None:
        """Marcar el registro para eliminar en el controlador principal."""
        self.accept()
        self.decision = [self.record, "eliminar"]

    def on_export(self) -> None:
        """Marcar el registro para exportar en el controlador principal."""
        self.accept()
        self.decision = [self.record, "exportar"]

    def accept(self) -> None:
        super().accept()