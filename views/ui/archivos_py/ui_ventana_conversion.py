# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_conversion.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(766, 486)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.comboBox_entrada = QComboBox(Form)
        self.comboBox_entrada.setObjectName(u"comboBox_entrada")

        self.gridLayout.addWidget(self.comboBox_entrada, 3, 0, 1, 1)

        self.comboBox_destino = QComboBox(Form)
        self.comboBox_destino.setObjectName(u"comboBox_destino")

        self.gridLayout.addWidget(self.comboBox_destino, 3, 2, 1, 1)

        self.pushButton_convertir = QPushButton(Form)
        self.pushButton_convertir.setObjectName(u"pushButton_convertir")

        self.gridLayout.addWidget(self.pushButton_convertir, 4, 1, 1, 1)

        self.numero_conversion = QLineEdit(Form)
        self.numero_conversion.setObjectName(u"numero_conversion")

        self.gridLayout.addWidget(self.numero_conversion, 2, 0, 1, 3)

        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setStyleSheet(u"font: 26pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.lbl_titulo, 0, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.campo_explicacion = QTextEdit(Form)
        self.campo_explicacion.setObjectName(u"campo_explicacion")

        self.gridLayout.addWidget(self.campo_explicacion, 5, 0, 1, 3)

        self.chk_mostrar_pasos = QCheckBox(Form)
        self.chk_mostrar_pasos.setObjectName(u"chk_mostrar_pasos")

        self.gridLayout.addWidget(self.chk_mostrar_pasos, 1, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Categorias :Tiempo,Temperatura,Velocidad,Volumen,Longitud,Masa", None))
        self.pushButton_convertir.setText(QCoreApplication.translate("Form", u"Realizar conversion", None))
        self.numero_conversion.setPlaceholderText(QCoreApplication.translate("Form", u"Escriba el numero ...", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"Conversor de unidades", None))
        self.chk_mostrar_pasos.setText(QCoreApplication.translate("Form", u"Mostrar pasos", None))
    # retranslateUi

