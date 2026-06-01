from PySide6.QtWidgets import (QMdiArea, QMainWindow,
    QInputDialog, QListWidget, QDockWidget, QStyle)
from PySide6.QtGui import QAction, QIcon
import os
from utils import get_resource_path
from PySide6.QtCore import Qt, QSize
from views.ui.archivos_py.ui_ventana_principal import Ui_MainWindow
from gestor_temas import ThemeManager
from views.dialog_historial import HistoryDialog

class MainView(QMainWindow, Ui_MainWindow):
    """Ventana principal de la aplicación que aloja el área MDI y el dock de historial."""

    def __init__(self, controller) -> None:
        super().__init__()
        self.setupUi(self)
        self.mdi_area = QMdiArea()
        self.history_list_widget = QListWidget()
        self._history_dock: QDockWidget | None = None
        self._theme_manager = ThemeManager()
        self.setCentralWidget(self.mdi_area)
        self.act_visual_ruler = QAction(self)
        self.act_visual_ruler.setObjectName("act_regla_visual")
        self.act_visual_ruler.setText("Regla visual")
        self._setup_menu()
        self._setup_toolbar()

    def _setup_menu(self) -> None:
        """Insertar acciones adicionales en la estructura de menú cargada."""
        self.menuAplicacion.insertAction(self.act_exportar_csv, self.act_visual_ruler)

    def _setup_toolbar(self) -> None:
        """Configurar los iconos de la barra de herramientas y agregar acciones."""
        self.toolBar.setIconSize(QSize(24, 24))
        self.toolBar.setMovable(False)

        # Intentar cargar iconos personalizados, con fallback a iconos estándar
        def load_icon(name, fallback):
            path = get_resource_path(f"recursos/icons/{name}.svg")
            if os.path.exists(path):
                return QIcon(path)
            return self.style().standardIcon(fallback)

        self.act_realizar_conversion.setIcon(load_icon('convert', QStyle.SP_DialogYesButton))
        self.act_visual_ruler.setIcon(load_icon('ruler', QStyle.SP_MessageBoxInformation))
        self.act_exportar_csv.setIcon(load_icon('save', QStyle.SP_DialogSaveButton))
        self.act_mostrar_historial.setIcon(load_icon('history', QStyle.SP_FileDialogDetailedView))
        self.act_cascada.setIcon(load_icon('cascade', QStyle.SP_ArrowDown))
        self.act_mosaico.setIcon(load_icon('tile', QStyle.SP_DirOpenIcon))
        self.act_salir.setIcon(load_icon('close', QStyle.SP_DialogCloseButton))

        self.toolBar.addAction(self.act_realizar_conversion)
        self.toolBar.addAction(self.act_visual_ruler)
        self.toolBar.addAction(self.act_exportar_csv)
        self.toolBar.addAction(self.act_mostrar_historial)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_cascada)
        self.toolBar.addAction(self.act_mosaico)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.act_salir)

    def show_status(self, message: str) -> None:
        """Mostrar un mensaje de estado transitorio en la barra de estado."""
        self.status_bar.showMessage(message, 5000)

    def select_category(self) -> str | None:
        """Mostrar un diálogo para seleccionar una categoría de conversión."""
        categories = ["Longitud", "Masa", "Tiempo", "Temperatura", "Volumen", "Velocidad"]
        selected_category, ok = QInputDialog.getItem(self, "Seleccionar categoría",
                                                     "Categoría:", categories, 0, False)
        if ok and selected_category:
            return selected_category
        return None

    def open_subwindow(self, subwindow) -> None:
        """Agregar la subventana al área MDI si no está ya presente."""
        if subwindow not in self.mdi_area.subWindowList():
            self.mdi_area.addSubWindow(subwindow)
        subwindow.show()

    def show_history(self, history: list[list[object]]) -> None:
        """Mostrar una lista resumida de historial dentro del widget dock."""
        history_lines: list[str] = []
        self.history_list_widget.clear()
        for record, _label in history:
            history_lines.append(
                f"{record.input_value} {record.input_unit} -> {record.output_value} {record.output_unit} "
            )
        history_lines.sort(reverse=True)
        self.history_list_widget.addItems(history_lines)

        if self._history_dock is None:
            self._history_dock = QDockWidget("Historial", self)
            self._history_dock.setWidget(self.history_list_widget)
            self.addDockWidget(Qt.RightDockWidgetArea, self._history_dock)
        else:
            self._history_dock.show()
            self._history_dock.raise_()