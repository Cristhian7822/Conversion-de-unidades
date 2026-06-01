# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_datos_historial.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(576, 473)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_eliminar = QPushButton(Dialog)
        self.btn_eliminar.setObjectName(u"btn_eliminar")

        self.gridLayout.addWidget(self.btn_eliminar, 7, 0, 1, 1)

        self.btn_accept = QPushButton(Dialog)
        self.btn_accept.setObjectName(u"btn_accept")

        self.gridLayout.addWidget(self.btn_accept, 7, 2, 1, 1)

        self.lbl_unidad_entrada = QLabel(Dialog)
        self.lbl_unidad_entrada.setObjectName(u"lbl_unidad_entrada")

        self.gridLayout.addWidget(self.lbl_unidad_entrada, 2, 0, 1, 3)

        self.lbl_unidad_salida = QLabel(Dialog)
        self.lbl_unidad_salida.setObjectName(u"lbl_unidad_salida")

        self.gridLayout.addWidget(self.lbl_unidad_salida, 4, 0, 1, 3)

        self.lbl_tiempo = QLabel(Dialog)
        self.lbl_tiempo.setObjectName(u"lbl_tiempo")

        self.gridLayout.addWidget(self.lbl_tiempo, 1, 0, 1, 3)

        self.lbl_valor = QLabel(Dialog)
        self.lbl_valor.setObjectName(u"lbl_valor")

        self.gridLayout.addWidget(self.lbl_valor, 5, 0, 1, 3)

        self.lbl_resultado = QLabel(Dialog)
        self.lbl_resultado.setObjectName(u"lbl_resultado")

        self.gridLayout.addWidget(self.lbl_resultado, 6, 0, 1, 3)

        self.btn_recargar = QPushButton(Dialog)
        self.btn_recargar.setObjectName(u"btn_recargar")
        self.btn_recargar.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btn_recargar, 7, 1, 1, 1)

        self.btn_exportar = QPushButton(Dialog)
        self.btn_exportar.setObjectName(u"btn_exportar")

        self.gridLayout.addWidget(self.btn_exportar, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.btn_accept.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.btn_accept.setText(QCoreApplication.translate("Dialog", u"Ok", None))
        self.lbl_unidad_entrada.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lbl_unidad_salida.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lbl_tiempo.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lbl_valor.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.lbl_resultado.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.btn_recargar.setText(QCoreApplication.translate("Dialog", u"Cargar en conversion", None))
        self.btn_exportar.setText(QCoreApplication.translate("Dialog", u"Exportar a CSV", None))
    # retranslateUi

