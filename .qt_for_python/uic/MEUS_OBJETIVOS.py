# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\projetoSCO\TELAS.PY\MEUS_OBJETIVOS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(737, 578)
        self.Back_Lista = QtWidgets.QLabel(Dialog)
        self.Back_Lista.setGeometry(QtCore.QRect(0, 0, 221, 581))
        self.Back_Lista.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.Back_Lista.setText("")
        self.Back_Lista.setObjectName("Back_Lista")
        self.Back = QtWidgets.QLabel(Dialog)
        self.Back.setGeometry(QtCore.QRect(0, 0, 871, 611))
        self.Back.setStyleSheet("background-color: rgb(170, 197, 255);")
        self.Back.setText("")
        self.Back.setObjectName("Back")
        self.Img_User = QtWidgets.QLabel(Dialog)
        self.Img_User.setGeometry(QtCore.QRect(50, 10, 81, 91))
        self.Img_User.setStyleSheet("image: url(:/img/USUARIO.png);")
        self.Img_User.setText("")
        self.Img_User.setObjectName("Img_User")
        self.B_Sair = QtWidgets.QPushButton(Dialog)
        self.B_Sair.setGeometry(QtCore.QRect(0, 540, 41, 23))
        self.B_Sair.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Sair.setObjectName("B_Sair")
        self.L_CAD_OBJ = QtWidgets.QLabel(Dialog)
        self.L_CAD_OBJ.setGeometry(QtCore.QRect(400, 10, 221, 41))
        self.L_CAD_OBJ.setObjectName("L_CAD_OBJ")
        self.B_MeusObjetivos = QtWidgets.QPushButton(Dialog)
        self.B_MeusObjetivos.setEnabled(True)
        self.B_MeusObjetivos.setGeometry(QtCore.QRect(0, 150, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_MeusObjetivos.setFont(font)
        self.B_MeusObjetivos.setToolTipDuration(-1)
        self.B_MeusObjetivos.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_MeusObjetivos.setObjectName("B_MeusObjetivos")
        self.B_Conf_Conta = QtWidgets.QPushButton(Dialog)
        self.B_Conf_Conta.setGeometry(QtCore.QRect(-10, 510, 161, 23))
        self.B_Conf_Conta.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.B_Conf_Conta.setObjectName("B_Conf_Conta")
        self.B_NovoObjetivo = QtWidgets.QPushButton(Dialog)
        self.B_NovoObjetivo.setEnabled(True)
        self.B_NovoObjetivo.setGeometry(QtCore.QRect(0, 190, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_NovoObjetivo.setFont(font)
        self.B_NovoObjetivo.setToolTipDuration(-1)
        self.B_NovoObjetivo.setStyleSheet("background-color: rgb(198, 255, 253);")
        self.B_NovoObjetivo.setObjectName("B_NovoObjetivo")
        self.NomeUsuario = QtWidgets.QLabel(Dialog)
        self.NomeUsuario.setGeometry(QtCore.QRect(40, 100, 111, 21))
        self.NomeUsuario.setObjectName("NomeUsuario")
        self.T_materia = QtWidgets.QTableWidget(Dialog)
        self.T_materia.setGeometry(QtCore.QRect(270, 90, 261, 51))
        self.T_materia.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_materia.setObjectName("T_materia")
        self.T_materia.setColumnCount(1)
        self.T_materia.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.T_materia.setHorizontalHeaderItem(0, item)
        self.T_materia.horizontalHeader().setCascadingSectionResizes(False)
        self.T_materia.horizontalHeader().setSortIndicatorShown(False)
        self.T_materia.horizontalHeader().setStretchLastSection(True)
        self.T_assunto = QtWidgets.QTableWidget(Dialog)
        self.T_assunto.setGeometry(QtCore.QRect(270, 140, 261, 51))
        self.T_assunto.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_assunto.setObjectName("T_assunto")
        self.T_assunto.setColumnCount(1)
        self.T_assunto.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.T_assunto.setHorizontalHeaderItem(0, item)
        self.T_assunto.horizontalHeader().setCascadingSectionResizes(False)
        self.T_assunto.horizontalHeader().setSortIndicatorShown(False)
        self.T_assunto.horizontalHeader().setStretchLastSection(True)
        self.T_objetivo1 = QtWidgets.QTableWidget(Dialog)
        self.T_objetivo1.setGeometry(QtCore.QRect(270, 190, 261, 31))
        self.T_objetivo1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_objetivo1.setObjectName("T_objetivo1")
        self.T_objetivo1.setColumnCount(0)
        self.T_objetivo1.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_objetivo1.setVerticalHeaderItem(0, item)
        self.T_objetivo1.horizontalHeader().setCascadingSectionResizes(False)
        self.T_objetivo1.horizontalHeader().setSortIndicatorShown(False)
        self.T_objetivo1.horizontalHeader().setStretchLastSection(True)
        self.T_RC_A1 = QtWidgets.QTableWidget(Dialog)
        self.T_RC_A1.setGeometry(QtCore.QRect(270, 220, 261, 31))
        self.T_RC_A1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_RC_A1.setObjectName("T_RC_A1")
        self.T_RC_A1.setColumnCount(0)
        self.T_RC_A1.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_RC_A1.setVerticalHeaderItem(0, item)
        self.T_RC_A1.horizontalHeader().setCascadingSectionResizes(False)
        self.T_RC_A1.horizontalHeader().setSortIndicatorShown(False)
        self.T_RC_A1.horizontalHeader().setStretchLastSection(True)
        self.T_RC_B1 = QtWidgets.QTableWidget(Dialog)
        self.T_RC_B1.setGeometry(QtCore.QRect(270, 250, 261, 31))
        self.T_RC_B1.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_RC_B1.setObjectName("T_RC_B1")
        self.T_RC_B1.setColumnCount(0)
        self.T_RC_B1.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_RC_B1.setVerticalHeaderItem(0, item)
        self.T_RC_B1.horizontalHeader().setCascadingSectionResizes(False)
        self.T_RC_B1.horizontalHeader().setSortIndicatorShown(False)
        self.T_RC_B1.horizontalHeader().setStretchLastSection(True)
        self.T_objetivo2 = QtWidgets.QTableWidget(Dialog)
        self.T_objetivo2.setGeometry(QtCore.QRect(270, 290, 261, 31))
        self.T_objetivo2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_objetivo2.setObjectName("T_objetivo2")
        self.T_objetivo2.setColumnCount(0)
        self.T_objetivo2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_objetivo2.setVerticalHeaderItem(0, item)
        self.T_objetivo2.horizontalHeader().setCascadingSectionResizes(False)
        self.T_objetivo2.horizontalHeader().setSortIndicatorShown(False)
        self.T_objetivo2.horizontalHeader().setStretchLastSection(True)
        self.T_RC_A2 = QtWidgets.QTableWidget(Dialog)
        self.T_RC_A2.setGeometry(QtCore.QRect(270, 320, 261, 31))
        self.T_RC_A2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_RC_A2.setObjectName("T_RC_A2")
        self.T_RC_A2.setColumnCount(0)
        self.T_RC_A2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_RC_A2.setVerticalHeaderItem(0, item)
        self.T_RC_A2.horizontalHeader().setCascadingSectionResizes(False)
        self.T_RC_A2.horizontalHeader().setSortIndicatorShown(False)
        self.T_RC_A2.horizontalHeader().setStretchLastSection(True)
        self.T_RC_B2 = QtWidgets.QTableWidget(Dialog)
        self.T_RC_B2.setGeometry(QtCore.QRect(270, 350, 261, 31))
        self.T_RC_B2.setStyleSheet("background-color: rgb(113, 229, 231);")
        self.T_RC_B2.setObjectName("T_RC_B2")
        self.T_RC_B2.setColumnCount(0)
        self.T_RC_B2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.T_RC_B2.setVerticalHeaderItem(0, item)
        self.T_RC_B2.horizontalHeader().setCascadingSectionResizes(False)
        self.T_RC_B2.horizontalHeader().setSortIndicatorShown(False)
        self.T_RC_B2.horizontalHeader().setStretchLastSection(True)
        self.Back.raise_()
        self.Back_Lista.raise_()
        self.NomeUsuario.raise_()
        self.B_Sair.raise_()
        self.L_CAD_OBJ.raise_()
        self.B_MeusObjetivos.raise_()
        self.B_Conf_Conta.raise_()
        self.B_NovoObjetivo.raise_()
        self.Img_User.raise_()
        self.T_materia.raise_()
        self.T_assunto.raise_()
        self.T_objetivo1.raise_()
        self.T_RC_A1.raise_()
        self.T_RC_B1.raise_()
        self.T_objetivo2.raise_()
        self.T_RC_A2.raise_()
        self.T_RC_B2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.B_Sair.setText(_translate("Dialog", "Sair"))
        self.L_CAD_OBJ.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">MEUS OBJETIVOS</span></p></body></html>"))
        self.B_MeusObjetivos.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_MeusObjetivos.setText(_translate("Dialog", "Meus Objetivos"))
        self.B_Conf_Conta.setText(_translate("Dialog", "Configurações de conta"))
        self.B_NovoObjetivo.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ffffff;\">Meus Objetivos</span></p></body></html>"))
        self.B_NovoObjetivo.setText(_translate("Dialog", "Novo Objetivo"))
        self.NomeUsuario.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Nome_Usuario</span></p></body></html>"))
        item = self.T_materia.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Matéria"))
        item = self.T_assunto.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Assunto"))
        item = self.T_objetivo1.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Objetivo1"))
        item = self.T_RC_A1.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Resultado-Chave a"))
        item = self.T_RC_B1.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Resultado-Chave b"))
        item = self.T_objetivo2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Objetivo2"))
        item = self.T_RC_A2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Resultado-Chave a"))
        item = self.T_RC_B2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Resultado-Chave b"))
import sourcee_rc
