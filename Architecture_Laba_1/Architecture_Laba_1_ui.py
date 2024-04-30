# Form implementation generated from reading ui file 'Architecture_Laba_1_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
        MainWindow.setStyleSheet("QWidget {\n"
"background-color: rgb(0, 0, 0); \n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.textEditAnswer = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEditAnswer.setGeometry(QtCore.QRect(10, 230, 271, 151))
        self.textEditAnswer.setMinimumSize(QtCore.QSize(0, 0))
        self.textEditAnswer.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.textEditAnswer.setObjectName("textEditAnswer")
        self.labelGif = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelGif.setGeometry(QtCore.QRect(10, 60, 480, 91))
        self.labelGif.setMinimumSize(QtCore.QSize(480, 70))
        self.labelGif.setObjectName("labelGif")
        self.labelTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(100, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 481, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditIp = QtWidgets.QLineEdit(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditIp.setFont(font)
        self.lineEditIp.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.lineEditIp.setObjectName("lineEditIp")
        self.horizontalLayout.addWidget(self.lineEditIp)
        self.pushButtonGenerateAnswer = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonGenerateAnswer.setFont(font)
        self.pushButtonGenerateAnswer.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButtonGenerateAnswer.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"")
        self.pushButtonGenerateAnswer.setObjectName("pushButtonGenerateAnswer")
        self.horizontalLayout.addWidget(self.pushButtonGenerateAnswer)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 230, 191, 131))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget.raise_()
        self.textEditAnswer.raise_()
        self.labelTitle.raise_()
        self.labelGif.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelGif.setText(_translate("MainWindow", "TextLabel"))
        self.labelTitle.setText(_translate("MainWindow", "Хочу узнать параметры сети!"))
        self.pushButtonGenerateAnswer.setText(_translate("MainWindow", "Показать параметры сети"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
