# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\projetoSCO\TELAS.PY\LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(690, 523)
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-20, -10, 711, 541))
        self.background.setStyleSheet("background-color: rgb(170, 197, 255);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Usuario = QtWidgets.QLabel(Dialog)
        self.Usuario.setGeometry(QtCore.QRect(200, 170, 91, 41))
        self.Usuario.setObjectName("Usuario")
        self.Senha = QtWidgets.QLabel(Dialog)
        self.Senha.setGeometry(QtCore.QRect(200, 220, 91, 41))
        self.Senha.setObjectName("Senha")
        self.B_Cadastrar = QtWidgets.QPushButton(Dialog)
        self.B_Cadastrar.setGeometry(QtCore.QRect(170, 300, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.B_Cadastrar.sizePolicy().hasHeightForWidth())
        self.B_Cadastrar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_Cadastrar.setFont(font)
        self.B_Cadastrar.setStyleSheet("background-color: rgb(130, 217, 210);\n"
"color: rgb(255, 255, 255);")
        self.B_Cadastrar.setIconSize(QtCore.QSize(16, 16))
        self.B_Cadastrar.setAutoRepeatDelay(300)
        self.B_Cadastrar.setAutoRepeatInterval(100)
        self.B_Cadastrar.setObjectName("B_Cadastrar")
        self.B_Entrar = QtWidgets.QPushButton(Dialog)
        self.B_Entrar.setGeometry(QtCore.QRect(340, 300, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_Entrar.setFont(font)
        self.B_Entrar.setStyleSheet("background-color: rgb(130, 217, 210);\n"
"color: rgb(255, 255, 255);")
        self.B_Entrar.setObjectName("B_Entrar")
        self.C_usuario = QtWidgets.QLineEdit(Dialog)
        self.C_usuario.setGeometry(QtCore.QRect(310, 180, 141, 21))
        self.C_usuario.setObjectName("C_usuario")
        self.C_senha = QtWidgets.QLineEdit(Dialog)
        self.C_senha.setGeometry(QtCore.QRect(310, 230, 141, 21))
        self.C_senha.setObjectName("C_senha")
        self.img_usuario_T1 = QtWidgets.QLabel(Dialog)
        self.img_usuario_T1.setGeometry(QtCore.QRect(260, 30, 161, 111))
        self.img_usuario_T1.setStyleSheet("image: url(:/img/USUARIO.png);")
        self.img_usuario_T1.setText("")
        self.img_usuario_T1.setObjectName("img_usuario_T1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Usuario.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Usuário:</span></p></body></html>"))
        self.Senha.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Senha:</span></p></body></html>"))
        self.B_Cadastrar.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Cadastrar</span></p></body></html>"))
        self.B_Cadastrar.setText(_translate("Dialog", "Cadastrar"))
        self.B_Entrar.setText(_translate("Dialog", "Entrar"))
import sourcee_rc
