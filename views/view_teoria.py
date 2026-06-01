from PySide6.QtWidgets import QMdiSubWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget

class TheoryView(QMdiSubWindow):
    """Vista de subventana para mostrar contenido de teoría y tablas."""

    def __init__(self, topic: str, controller) -> None:
        super().__init__()
        self.topic: str = topic
        self.controller = controller
        self._table_shown = False
        self.setWindowTitle(topic)

        self.title_label = QLabel(topic)
        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        self.show_table_button = QPushButton("Mostrar tabla")

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.content_text)
        layout.addWidget(self.show_table_button)

        container = QWidget()
        container.setLayout(layout)
        self.setWidget(container)

    def show_theory(self, data: dict) -> None:
        """Insertar el texto de la teoría en el área de contenido."""
        self.content_text.insertPlainText(data.get(self.topic, "No se encontró teoría para este tema."))

    def show_table(self, table_data: dict) -> None:
        """Insertar el contenido de la tabla una vez por instancia de vista."""
        if self._table_shown:
            return
        table_html = table_data.get(self.topic, "<p>No se encontró tabla para este tema.</p>")
        self.content_text.insertHtml("<br><br>" + table_html)
        self._table_shown = True

