from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(613, 528)
        MainWindow.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -30, 621, 151))
        self.frame.setStyleSheet(u"background-color: rgb(52, 165, 201);\n"
"color : rgb(255, 255, 255);\n"
"border-radius :30px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 261, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 271, 51))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 140, 291, 171))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"color : rgb(22, 71, 86);\n"
"border-radius :10px;\n"
"border: 1px solid rgb(52, 165, 201);")
        self.cancel = QPushButton(self.groupBox)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(10, 120, 131, 31))
        self.cancel.setFont(font)
        self.cancel.setStyleSheet(u"background-color: rgb(52, 165, 201);\n"
"color : rgb(255, 255, 255);\n"
"border-radius : 10px;")
        self.validated = QPushButton(self.groupBox)
        self.validated.setObjectName(u"validated")
        self.validated.setGeometry(QRect(149, 120, 131, 31))
        self.validated.setFont(font)
        self.validated.setStyleSheet(u"background-color: rgb(52, 165, 201);\n"
"color : rgb(255, 255, 255);\n"
"border-radius : 10px;")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 261, 51))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color : rgb(22, 71, 86);\n"
"border: none;")
        self.input = QTextEdit(self.groupBox)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(10, 70, 271, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.input.setFont(font3)
        self.input.setStyleSheet(u"border-radius : 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(52, 165, 201);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(310, 140, 291, 171))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"color : rgb(22, 71, 86);\n"
"border-radius :10px;\n"
"border: 1px solid rgb(52, 165, 201);")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 241, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color : rgb(22, 71, 86);\n"
"border: none;")
        self.result = QLabel(self.groupBox_2)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(10, 70, 271, 61))
        self.result.setFont(font3)
        self.result.setStyleSheet(u"border: none;")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 320, 591, 181))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"color : rgb(22, 71, 86);\n"
"border-radius :10px;\n"
"border: 1px solid rgb(52, 165, 201);")
        self.lblRoute = QTextEdit(self.groupBox_3)
        self.lblRoute.setObjectName(u"lblRoute")
        self.lblRoute.setEnabled(False)
        self.lblRoute.setGeometry(QRect(10, 30, 571, 131))
        self.lblRoute.setFont(font3)
        self.lblRoute.setStyleSheet(u"border-radius : 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(52, 165, 201);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"203405 Antonio Martinez", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LOTES DE MEDICAMENTO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AUTOMATA VERIFICADOR DE", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de entrada", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.validated.setText(QCoreApplication.translate("MainWindow", u"Validar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese el lote del Medicamento", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Datos de salida", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resultado de la Verificacion:", None))
        self.result.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Ruta del recorrido del automata", None))
        self.lblRoute.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Esperando los datos de salida", None))
    # retranslateUi

