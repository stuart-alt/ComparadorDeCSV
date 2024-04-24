

import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from os.path import expanduser
import datacompy
from pandas import read_csv


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherCSV_1.clicked.connect(self.abrir_csv_1)
        self.btnEscolherCSV_2.clicked.connect(self.abrir_csv_2)
        self.btn_cancelar.clicked.connect(qt.closeAllWindows)
        self.btn_confirmar.clicked.connect(self.confirmar)
        self.file_1 = None
        self.file_2 = None
        self.home = expanduser('~')

    def exec_comp(self, df1, df2, campos):
        df_1 = read_csv(df1[0])
        df_2 = read_csv(df2[0])

        try:
            compare = datacompy.Compare(df_1, df_2, join_columns=campos)
            result = compare.report()
            return result
        except Exception as e:
            return str(e)

    def abrir_csv_1(self):
        self.listWidget_file_1.clear()
        self.file_1 = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Selecionar 1o arquivo',
            self.home,
            'CSV (*.csv)'
        )[0]
        for file in self.file_1:
            self.listWidget_file_1.addItem(file)

    def abrir_csv_2(self):
        self.listWidget_file_2.clear()
        self.file_2 = QFileDialog.getOpenFileNames(
            self.centralwidget,
            'Selecionar 2o arquivo',
            self.home,
            'CSV (*.csv)'
        )[0]
        for file in self.file_2:
            self.listWidget_file_2.addItem(file)

    def confirmar(self):
        campos = self.inserir_campo_chave.text().split(',')
        if self.file_1 is not None and self.file_2 is not None and len(campos) > 0:
            result = self.exec_comp(self.file_1, self.file_2, campos)
            self.resultado_comparacao.clear()
            self.resultado_comparacao.insertPlainText(result)
        else:
            self.show_popup_result()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
