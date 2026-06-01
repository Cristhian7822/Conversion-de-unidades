from PySide6.QtCore import Qt, QSize, QRectF, QPointF, Signal
from PySide6.QtGui import QPainter, QColor, QPen, QFont
from PySide6.QtWidgets import QWidget


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


class VisualRuler(QWidget):
    """
    Widget personalizado que representa una regla física interactiva.
    Permite al usuario seleccionar valores deslizando un indicador visual.
    """
    valueChanged = Signal(float)

    def __init__(self, parent=None):
        """Inicializa las propiedades físicas y visuales de la regla."""
        super().__init__(parent)
        self.minimum = 0.0
        self.maximum = 100.0
        self.current_value = 0.0
        self.margin = 24
        self.handle_radius = 8
        self.dragging = False
        self.setMinimumHeight(120)
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)

    def sizeHint(self):
        """Define el tamaño sugerido del widget."""
        return QSize(360, 120)

    def usable_width(self):
        """Calcula el ancho real disponible para el dibujo, restando márgenes."""
        return max(1, self.width() - 2 * self.margin)

    def x_from_value(self, value):
        """Convierte un valor numérico a una posición de coordenadas X en el widget."""
        ratio = (value - self.minimum) / (self.maximum - self.minimum)
        return self.margin + ratio * self.usable_width()

    def value_from_x(self, x):
        """Convierte una coordenada X en el widget al valor numérico correspondiente."""
        ratio = clamp((x - self.margin) / self.usable_width(), 0.0, 1.0)
        return self.minimum + ratio * (self.maximum - self.minimum)

    def paintEvent(self, event):
        """Dibuja la regla, las marcas de graduación, los números y el indicador deslizante."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        linea_y = rect.center().y()
        start = QPointF(self.margin, linea_y)
        end = QPointF(rect.width() - self.margin, linea_y)

        painter.setPen(QPen(QColor("#2d2d2d"), 3))
        painter.drawLine(start, end)

        steps = 10
        long_mark = 12
        short_mark = 6
        font = QFont("Segoe UI", 8)
        painter.setFont(font)
        painter.setPen(QPen(QColor("#1a1a1a"), 2))

        for i in range(steps + 1):
            x = self.margin + i * (self.usable_width() / steps)
            height = long_mark if i % 2 == 0 else short_mark
            painter.drawLine(QPointF(x, linea_y - height), QPointF(x, linea_y + height))
            if i % 2 == 0:
                value = self.minimum + (self.maximum - self.minimum) * (i / steps)
                text = f"{value:.0f}"
                painter.drawText(QRectF(x - 20, linea_y + long_mark + 4, 40, 16), Qt.AlignCenter, text)

        handle_x = self.x_from_value(self.current_value)
        handle_center = QPointF(handle_x, linea_y)
        painter.setBrush(QColor("#f0a000"))
        painter.setPen(QPen(QColor("#805000"), 2))
        painter.drawEllipse(handle_center, self.handle_radius, self.handle_radius)

        # Etiqueta de valor de la regla
        label = f"Valor regla: {self.current_value:.1f}"
        painter.setFont(QFont("Segoe UI", 9, QFont.Bold))
        painter.setPen(QColor("#333333"))
        painter.drawText(QRectF(self.margin, 4, self.width() - 2 * self.margin, 20), Qt.AlignCenter, label)

    def mousePressEvent(self, event):
        """Detecta si el usuario hace clic sobre el indicador para iniciar el arrastre."""
        point = event.position() if hasattr(event, "position") else event.pos()
        handle_x = self.x_from_value(self.current_value)
        distance = abs(point.x() - handle_x)
        if distance <= self.handle_radius + 4:
            self.dragging = True
            event.accept()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Actualiza la posición del indicador y emite el nuevo valor mientras se arrastra el ratón."""
        if self.dragging:
            point = event.position() if hasattr(event, "position") else event.pos()
            new_value = self.value_from_x(point.x())
            if abs(new_value - self.current_value) > 0.01:
                self.current_value = new_value
                self.valueChanged.emit(self.current_value)
                self.update()
            event.accept()
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """Finaliza la acción de arrastre del indicador."""
        if self.dragging:
            self.dragging = False
            event.accept()
        else:
            super().mouseReleaseEvent(event)
