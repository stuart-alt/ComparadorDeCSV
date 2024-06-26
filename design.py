# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design_compara_csv.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnEscolherCSV_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherCSV_1.setObjectName("btnEscolherCSV_1")
        self.gridLayout_2.addWidget(self.btnEscolherCSV_1, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 212))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 688, 210))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_file_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_file_2.setObjectName("listWidget_file_2")
        self.gridLayout_3.addWidget(self.listWidget_file_2, 0, 2, 1, 1)
        self.listWidget_file_1 = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_file_1.setObjectName("listWidget_file_1")
        self.gridLayout_3.addWidget(self.listWidget_file_1, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.inserir_campo_chave = QtWidgets.QLineEdit(self.centralwidget)
        self.inserir_campo_chave.setObjectName("inserir_campo_chave")
        self.gridLayout_2.addWidget(self.inserir_campo_chave, 5, 0, 1, 2)
        self.btnEscolherCSV_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnEscolherCSV_2.setObjectName("btnEscolherCSV_2")
        self.gridLayout_2.addWidget(self.btnEscolherCSV_2, 3, 1, 1, 1)
        self.info_campo_chave = QtWidgets.QPushButton(self.centralwidget)
        self.info_campo_chave.setEnabled(False)
        self.info_campo_chave.setObjectName("info_campo_chave")
        self.gridLayout_2.addWidget(self.info_campo_chave, 4, 0, 1, 2)
        self.btn_confirmar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirmar.setObjectName("btn_confirmar")
        self.gridLayout_2.addWidget(self.btn_confirmar, 6, 1, 1, 1)
        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.gridLayout_2.addWidget(self.btn_cancelar, 6, 0, 1, 1)
        self.resultado_comparacao = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultado_comparacao.setObjectName("resultado_comparacao")
        self.gridLayout_2.addWidget(self.resultado_comparacao, 8, 0, 1, 2)
        self.resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.resultado.setEnabled(False)
        self.resultado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resultado.setAlignment(QtCore.Qt.AlignCenter)
        self.resultado.setPlaceholderText("")
        self.resultado.setObjectName("resultado")
        self.gridLayout_2.addWidget(self.resultado, 7, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comparador de CSVs"))
        self.btnEscolherCSV_1.setText(_translate("MainWindow", "Escolher o 1o CSV"))
        self.btnEscolherCSV_2.setText(_translate("MainWindow", "Escolher o 2o CSV"))
        self.info_campo_chave.setText(
            _translate("MainWindow", "Digite o(s) campo(s) usado(s) para relacionar as colunas, separados por vírgula"))
        self.btn_confirmar.setText(_translate("MainWindow", "Confirmar"))
        self.btn_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.resultado.setText(_translate("MainWindow", "Resultado"))

    def show_popup_result(self):
        msg = QMessageBox()
        msg.setWindowTitle("Alerta")
        msg.setText("Verifique se os dois aquivos estão selecionados e se o campo que relaciona as colunas "
                    "está preenchido ")
        msg.setIcon(QMessageBox.Information)

        x = msg.exec_()
