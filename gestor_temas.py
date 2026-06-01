from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from utils import get_resource_path

class ThemeManager:
    """Administrar la selección de temas y la persistencia para la aplicación."""

    def __init__(self) -> None:
        self.settings = QSettings("ThemeManager", "Theme")
        self.current_theme: str = self.settings.value("tema_actual", "claro")
        self.themes: dict[str, str] = {
            "claro": get_resource_path("recursos/estilos/claro.qss"),
            "oscuro": get_resource_path("recursos/estilos/oscuro.qss")
        }
        self.apply_theme(self.current_theme)

    def apply_theme(self, name: str) -> None:
        """Cargar la hoja de estilo del tema y aplicarla a la aplicación."""
        with open(self.themes[name], encoding="utf-8") as theme_file:
            qss = theme_file.read()
        QApplication.instance().setStyleSheet(qss)
        self.current_theme = name
        self.settings.setValue("tema_actual", name)

    def get_current_theme(self) -> str:
        """Devolver el nombre del tema actualmente activo."""
        return self.settings.value("tema_actual")

    def available_themes(self) -> list[str]:
        """Devolver los identificadores de temas disponibles."""
        return list(self.themes.keys())