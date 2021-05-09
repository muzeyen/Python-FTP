# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ftpclient_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FtpServer(object):
    def setupUi(self, FtpServer):
        FtpServer.setObjectName("FtpServer")
        FtpServer.resize(800, 646)
        self.centralwidget = QtWidgets.QWidget(FtpServer)
        self.centralwidget.setObjectName("centralwidget")
        self.up_level_local = QtWidgets.QPushButton(self.centralwidget)
        self.up_level_local.setGeometry(QtCore.QRect(300, 390, 41, 31))
        self.up_level_local.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_level_local.setIcon(icon)
        self.up_level_local.setObjectName("up_level_local")
        self.local_nf_button = QtWidgets.QPushButton(self.centralwidget)
        self.local_nf_button.setGeometry(QtCore.QRect(450, 440, 41, 31))
        self.local_nf_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/new_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.local_nf_button.setIcon(icon1)
        self.local_nf_button.setObjectName("local_nf_button")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(450, 390, 41, 31))
        self.upload.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload.setIcon(icon2)
        self.upload.setObjectName("upload")
        self.delete_local = QtWidgets.QPushButton(self.centralwidget)
        self.delete_local.setGeometry(QtCore.QRect(370, 390, 41, 31))
        self.delete_local.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_local.setIcon(icon3)
        self.delete_local.setObjectName("delete_local")
        self.up_level_server = QtWidgets.QPushButton(self.centralwidget)
        self.up_level_server.setGeometry(QtCore.QRect(560, 390, 41, 31))
        self.up_level_server.setText("")
        self.up_level_server.setIcon(icon)
        self.up_level_server.setObjectName("up_level_server")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(720, 390, 41, 31))
        self.download.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download.setIcon(icon4)
        self.download.setObjectName("download")
        self.delete_server = QtWidgets.QPushButton(self.centralwidget)
        self.delete_server.setGeometry(QtCore.QRect(640, 390, 41, 31))
        self.delete_server.setText("")
        self.delete_server.setIcon(icon3)
        self.delete_server.setObjectName("delete_server")
        self.local_rename_button = QtWidgets.QPushButton(self.centralwidget)
        self.local_rename_button.setGeometry(QtCore.QRect(450, 480, 41, 31))
        self.local_rename_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/rename.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.local_rename_button.setIcon(icon5)
        self.local_rename_button.setObjectName("local_rename_button")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 231, 221))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        self.login_button.setGeometry(QtCore.QRect(30, 170, 151, 28))
        self.login_button.setObjectName("login_button")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(20, 130, 191, 22))
        self.password.setObjectName("password")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(20, 60, 191, 22))
        self.username.setObjectName("username")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 20, 241, 371))
        self.groupBox_2.setObjectName("groupBox_2")
        self.local_list = QtWidgets.QListWidget(self.groupBox_2)
        self.local_list.setGeometry(QtCore.QRect(10, 30, 211, 321))
        self.local_list.setObjectName("local_list")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(540, 20, 241, 371))
        self.groupBox_3.setObjectName("groupBox_3")
        self.server_list = QtWidgets.QListWidget(self.groupBox_3)
        self.server_list.setGeometry(QtCore.QRect(10, 30, 211, 321))
        self.server_list.setObjectName("server_list")
        self.local_nf_et = QtWidgets.QLineEdit(self.centralwidget)
        self.local_nf_et.setGeometry(QtCore.QRect(300, 440, 131, 31))
        self.local_nf_et.setObjectName("local_nf_et")
        self.local_rename_et = QtWidgets.QLineEdit(self.centralwidget)
        self.local_rename_et.setGeometry(QtCore.QRect(300, 480, 131, 31))
        self.local_rename_et.setObjectName("local_rename_et")
        self.server_nf_et = QtWidgets.QLineEdit(self.centralwidget)
        self.server_nf_et.setGeometry(QtCore.QRect(560, 440, 131, 31))
        self.server_nf_et.setObjectName("server_nf_et")
        self.server_nf_button = QtWidgets.QPushButton(self.centralwidget)
        self.server_nf_button.setGeometry(QtCore.QRect(720, 440, 41, 31))
        self.server_nf_button.setText("")
        self.server_nf_button.setIcon(icon1)
        self.server_nf_button.setObjectName("server_nf_button")
        self.server_rename_button = QtWidgets.QPushButton(self.centralwidget)
        self.server_rename_button.setGeometry(QtCore.QRect(720, 480, 41, 31))
        self.server_rename_button.setText("")
        self.server_rename_button.setIcon(icon5)
        self.server_rename_button.setObjectName("server_rename_button")
        self.server_rename_et = QtWidgets.QLineEdit(self.centralwidget)
        self.server_rename_et.setGeometry(QtCore.QRect(560, 480, 131, 31))
        self.server_rename_et.setObjectName("server_rename_et")
        FtpServer.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FtpServer)
        self.statusbar.setObjectName("statusbar")
        FtpServer.setStatusBar(self.statusbar)

        self.retranslateUi(FtpServer)
        QtCore.QMetaObject.connectSlotsByName(FtpServer)

    def retranslateUi(self, FtpServer):
        _translate = QtCore.QCoreApplication.translate
        FtpServer.setWindowTitle(_translate("FtpServer", "FTP SERVER"))
        self.groupBox.setTitle(_translate("FtpServer", "Login"))
        self.label.setText(_translate("FtpServer", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("FtpServer", "Parola: "))
        self.login_button.setText(_translate("FtpServer", "GİRİŞ"))
        self.groupBox_2.setTitle(_translate("FtpServer", "Local"))
        self.groupBox_3.setTitle(_translate("FtpServer", "Server"))