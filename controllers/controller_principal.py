from PySide6.QtWidgets import QFileDialog, QMessageBox, QMdiSubWindow
from model.model import Model
from views.view_principal import MainView
from views.regla_visual import VisualRuler
from controllers.controller_conversion import ConversionController
from controllers.controller_teoria import TheoryController
from views.dialog_historial import HistoryDialog

class MainController:
    """Controlador para la ventana principal de la aplicación y las acciones del menú."""

    def __init__(self) -> None:
        self.model = Model()
        self.view = MainView(self)
        self.conversion_controllers: dict[str, ConversionController] = {}
        self.theory_controllers: dict[str, TheoryController] = {}

        # Menu Aplicacion
        self.view.act_realizar_conversion.triggered.connect(lambda: self.open_conversion(category=None))
        self.view.act_exportar_csv.triggered.connect(lambda checked=False: self.export_csv())
        self.view.act_mostrar_historial.triggered.connect(lambda: self.view.show_history(self.model.get_history()))
        self.view.act_salir.triggered.connect(self.view.close)

        # Menu Teoria
        self.view.act_longitud.triggered.connect(lambda: self.open_theory("Longitud"))
        self.view.act_masa.triggered.connect(lambda: self.open_theory("Masa"))
        self.view.act_tiempo.triggered.connect(lambda: self.open_theory("Tiempo"))
        self.view.act_temperatura.triggered.connect(lambda: self.open_theory("Temperatura"))
        self.view.act_volumen.triggered.connect(lambda: self.open_theory("Volumen"))
        self.view.act_velocidad.triggered.connect(lambda: self.open_theory("Velocidad"))

        # Menu Ventana
        self.view.act_cascada.triggered.connect(self.cascade_windows)
        self.view.act_mosaico.triggered.connect(self.tile_windows)
        self.view.act_cerrar_ventanas.triggered.connect(self.close_all_windows)

        # Menu Tema
        self.view.act_tema_claro.triggered.connect(lambda: self.change_theme("claro"))
        self.view.act_tema_oscuro.triggered.connect(lambda: self.change_theme("oscuro"))

        # Menu Ayuda
        self.view.act_ayuda.triggered.connect(self.about)

        # Regla visual
        self.view.act_visual_ruler.triggered.connect(self.open_visual_ruler)

        # Historial detalles
        self.view.history_list_widget.itemClicked.connect(self.show_history_details)

    def open_conversion(self, category: str | None = None, reload_item=None) -> None:
        """Abrir o activar una subventana de conversión existente para una categoría."""
        if category is None:
            category = self.view.select_category()
        if not category:
            return

        if category in self.conversion_controllers:
            controller = self.conversion_controllers[category]
            if reload_item is not None:
                controller.reload_history_item(reload_item)
            subwindow = controller.view
            if subwindow.isVisible():
                self.view.mdi_area.setActiveSubWindow(subwindow)
                self.view.show_status(f"Conversión de {category} ya está abierta")
                return
            # Si la ventana fue cerrada previamente, recrear el controlador para evitar una vista vacía
            del self.conversion_controllers[category]

        controller = ConversionController(self.model, category, reload_item)
        controller.view.closed.connect(lambda cat=category: self._unregister_conversion_controller(cat))
        self.conversion_controllers[category] = controller
        controller.view.setWindowTitle(f"Conversión de {category}")
        self.view.open_subwindow(controller.view)
        # Mostrar el diálogo de decimales con la subventana como padre para que aparezca en primer plano
        controller.ask_decimals(controller.view)
        self.view.show_status(f"Conversión de {category} abierta")

    def open_theory(self, topic: str) -> None:
        """Abrir o activar una subventana de teoría existente."""
        if not topic:
            return

        if topic in self.theory_controllers:
            controller = self.theory_controllers[topic]
            subwindow = controller.view
            if subwindow.isVisible():
                self.view.mdi_area.setActiveSubWindow(subwindow)
                self.view.show_status(f"Teoría de {topic} ya está abierta")
            else:
                del self.theory_controllers[topic]

        controller = TheoryController(self.model, topic)
        self.theory_controllers[topic] = controller
        self.view.open_subwindow(controller.view)
        self.view.show_status(f"Teoría de {topic} abierta")

    def cascade_windows(self) -> None:
        self.view.mdi_area.cascadeSubWindows()

    def tile_windows(self) -> None:
        self.view.mdi_area.tileSubWindows()

    def close_all_windows(self) -> None:
        self.view.mdi_area.closeAllSubWindows()

    def change_theme(self, name: str) -> None:
        self.view._theme_manager.apply_theme(name)
        self.view.show_status(f"Tema cambiado a {name}")

    def open_visual_ruler(self) -> None:
        """Abrir la subventana de regla visual o activarla si ya está abierta."""
        if hasattr(self, '_visual_ruler_subwindow') and self._visual_ruler_subwindow is not None:
            subwindow = self._visual_ruler_subwindow
            if subwindow.isVisible():
                self.view.mdi_area.setActiveSubWindow(subwindow)
                self.view.show_status("Regla visual ya está abierta")
                return
        # Crear y mostrar la regla visual si no existe o no está visible
        subwindow = QMdiSubWindow()
        ruler = VisualRuler()
        ruler.valueChanged.connect(lambda value: self.view.show_status(f"Regla visual: {value:.2f}"))
        subwindow.setWidget(ruler)
        subwindow.setWindowTitle("Regla visual")
        self._visual_ruler_subwindow = subwindow
        self.view.open_subwindow(subwindow)
        self.view.show_status("Regla visual abierta")

    def _unregister_conversion_controller(self, category: str) -> None:
        """Eliminar el controlador de conversión cuando se cierra su subventana."""
        if category in self.conversion_controllers:
            del self.conversion_controllers[category]

    def export_csv(self, item=None) -> None:
        """Exportar el historial completo o un registro seleccionado a CSV."""
        path, _ = QFileDialog.getSaveFileName(
            self.view,
            "Guardar historial como CSV",
            "historial.csv",
            "Archivos CSV (*.csv);;Todos los archivos (*)"
        )
        if not path:
            return
        if not path.lower().endswith(".csv"):
            path += ".csv"

        history = None
        if item is not None:
            history = [item]

        try:
            self.model.export_history_csv(path, history)
            QMessageBox.information(self.view, "Exportar CSV", f"Historial exportado correctamente a:\n{path}")
        except Exception as e:
            QMessageBox.critical(self.view, "Exportar CSV", f"No se pudo exportar el historial:\n{e}")

    def about(self) -> None:
        """Mostrar el cuadro de diálogo Acerca de de la aplicación."""
        QMessageBox.information(self.view, "Acerca de", "Conversor multimedia versión 1.0")

    def show_history_details(self, item=None) -> None:
        """Abrir el diálogo de historial para el elemento seleccionado."""
        if item is None:
            return

        history_line = item.text()
        dialog = None
        for record, label in self.model.get_history():
            if label.strip() == history_line.strip():
                dialog = HistoryDialog(record)
                dialog.exec()
                break

        if dialog is None or not dialog.decision:
            return

        record, action = dialog.decision
        if action == "recargar":
            category = None
            for unit in self.model.get_units():
                if unit.name == record.input_unit:
                    category = unit.category
                    break
            if category:
                self.open_conversion(category.strip(), reload_item=record)
        elif action == "eliminar":
            self.model.delete_history(record)
            self.view.show_history(self.model.get_history())
        elif action == "exportar":
            self.export_csv(record)