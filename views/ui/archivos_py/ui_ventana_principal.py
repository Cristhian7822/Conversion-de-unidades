# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.act_realizar_conversion = QAction(MainWindow)
        self.act_realizar_conversion.setObjectName(u"act_realizar_conversion")
        self.act_exportar_csv = QAction(MainWindow)
        self.act_exportar_csv.setObjectName(u"act_exportar_csv")
        self.act_mostrar_historial = QAction(MainWindow)
        self.act_mostrar_historial.setObjectName(u"act_mostrar_historial")
        self.act_longitud = QAction(MainWindow)
        self.act_longitud.setObjectName(u"act_longitud")
        self.act_masa = QAction(MainWindow)
        self.act_masa.setObjectName(u"act_masa")
        self.act_tiempo = QAction(MainWindow)
        self.act_tiempo.setObjectName(u"act_tiempo")
        self.act_temperatura = QAction(MainWindow)
        self.act_temperatura.setObjectName(u"act_temperatura")
        self.act_velocidad = QAction(MainWindow)
        self.act_velocidad.setObjectName(u"act_velocidad")
        self.act_volumen = QAction(MainWindow)
        self.act_volumen.setObjectName(u"act_volumen")
        self.act_cascada = QAction(MainWindow)
        self.act_cascada.setObjectName(u"act_cascada")
        self.act_mosaico = QAction(MainWindow)
        self.act_mosaico.setObjectName(u"act_mosaico")
        self.act_cerrar_ventanas = QAction(MainWindow)
        self.act_cerrar_ventanas.setObjectName(u"act_cerrar_ventanas")
        self.act_tema_claro = QAction(MainWindow)
        self.act_tema_claro.setObjectName(u"act_tema_claro")
        self.act_tema_oscuro = QAction(MainWindow)
        self.act_tema_oscuro.setObjectName(u"act_tema_oscuro")
        self.act_ayuda = QAction(MainWindow)
        self.act_ayuda.setObjectName(u"act_ayuda")
        self.act_salir = QAction(MainWindow)
        self.act_salir.setObjectName(u"act_salir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuAplicacion = QMenu(self.menubar)
        self.menuAplicacion.setObjectName(u"menuAplicacion")
        self.menuTeoriasYTablas = QMenu(self.menubar)
        self.menuTeoriasYTablas.setObjectName(u"menuTeoriasYTablas")
        self.menuVentana = QMenu(self.menubar)
        self.menuVentana.setObjectName(u"menuVentana")
        self.menuTema = QMenu(self.menubar)
        self.menuTema.setObjectName(u"menuTema")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuAplicacion.menuAction())
        self.menubar.addAction(self.menuTeoriasYTablas.menuAction())
        self.menubar.addAction(self.menuVentana.menuAction())
        self.menubar.addAction(self.menuTema.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuAplicacion.addAction(self.act_realizar_conversion)
        self.menuAplicacion.addAction(self.act_exportar_csv)
        self.menuAplicacion.addAction(self.act_mostrar_historial)
        self.menuAplicacion.addSeparator()
        self.menuAplicacion.addAction(self.act_salir)
        self.menuTeoriasYTablas.addAction(self.act_longitud)
        self.menuTeoriasYTablas.addAction(self.act_masa)
        self.menuTeoriasYTablas.addAction(self.act_tiempo)
        self.menuTeoriasYTablas.addAction(self.act_temperatura)
        self.menuTeoriasYTablas.addSeparator()
        self.menuTeoriasYTablas.addAction(self.act_velocidad)
        self.menuTeoriasYTablas.addAction(self.act_volumen)
        self.menuVentana.addAction(self.act_cascada)
        self.menuVentana.addAction(self.act_mosaico)
        self.menuVentana.addSeparator()
        self.menuVentana.addAction(self.act_cerrar_ventanas)
        self.menuTema.addSeparator()
        self.menuTema.addAction(self.act_tema_claro)
        self.menuTema.addAction(self.act_tema_oscuro)
        self.menuAyuda.addAction(self.act_ayuda)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_realizar_conversion.setText(QCoreApplication.translate("MainWindow", u"Realizar conversion", None))
        self.act_exportar_csv.setText(QCoreApplication.translate("MainWindow", u"Exportar CSV", None))
        self.act_mostrar_historial.setText(QCoreApplication.translate("MainWindow", u"Mostrar Historial", None))
        self.act_longitud.setText(QCoreApplication.translate("MainWindow", u"Longitud", None))
        self.act_masa.setText(QCoreApplication.translate("MainWindow", u"Masa", None))
        self.act_tiempo.setText(QCoreApplication.translate("MainWindow", u"Tiempo", None))
        self.act_temperatura.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.act_velocidad.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.act_volumen.setText(QCoreApplication.translate("MainWindow", u"Volumen", None))
        self.act_cascada.setText(QCoreApplication.translate("MainWindow", u"Cascada", None))
        self.act_mosaico.setText(QCoreApplication.translate("MainWindow", u"Mosaico", None))
        self.act_cerrar_ventanas.setText(QCoreApplication.translate("MainWindow", u"Cerrar ventanas", None))
        self.act_tema_claro.setText(QCoreApplication.translate("MainWindow", u"Tema claro", None))
        self.act_tema_oscuro.setText(QCoreApplication.translate("MainWindow", u"Tema oscuro", None))
        self.act_ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.act_salir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.menuAplicacion.setTitle(QCoreApplication.translate("MainWindow", u"Aplicacion", None))
        self.menuTeoriasYTablas.setTitle(QCoreApplication.translate("MainWindow", u"Teorias y Tablas", None))
        self.menuVentana.setTitle(QCoreApplication.translate("MainWindow", u"Ventana", None))
        self.menuTema.setTitle(QCoreApplication.translate("MainWindow", u"Tema", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

