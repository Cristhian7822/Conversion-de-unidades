import os
import sys
from PySide6.QtWidgets import QApplication
from controllers.controller_principal import MainController

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

app = QApplication(sys.argv)
main_controller = MainController()
main_controller.view.show()
sys.exit(app.exec())