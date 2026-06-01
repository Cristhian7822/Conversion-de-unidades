from views.view_teoria import TheoryView
from model.model import Model

class TheoryController:
    """Controlador para subventanas individuales de teoría o temas."""

    def __init__(self, model: Model, topic: str) -> None:
        self.model = model
        self.view = TheoryView(topic, self)
        self.topic = topic
        self.show_theory({})
        self.view.show_table_button.clicked.connect(self.show_table)

    def show_theory(self, _data: dict) -> None:
        """Cargar y mostrar el contenido teórico desde el modelo."""
        data = self.model.get_theory(self.topic)
        self.view.show_theory(data)

    def show_table(self) -> None:
        """Cargar y mostrar una tabla teórica desde el modelo."""
        table_data = self.model.get_tables(self.topic)
        self.view.show_table(table_data)