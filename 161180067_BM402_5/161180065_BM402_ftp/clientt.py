from PyQt5 import QtWidgets
from ftpclient import Ui_FtpServer
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ftplib import FTP
import ftplib
import os
import shutil


class ApplicationWindow(QMainWindow, Ui_FtpServer):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_FtpServer.setupUi(self, self)
        self.ui = Ui_FtpServer()
        self.connects()
        self.showLocalList()
        self.local_list.itemDoubleClicked.connect(self.localDirs)
        self.server_list.itemDoubleClicked.connect(self.serverDirs)

    def connects(self):
        # connection to functions
        self.login_button.clicked.connect(self.login)
        self.up_level_local.clicked.connect(self.upLevel_Local)
        self.server_nf_button.clicked.connect(self.newFolder_server)
        self.local_nf_button.clicked.connect(self.newFolder_local)
        self.upload.clicked.connect(self.upload_button)
        self.delete_local.clicked.connect(self.deleteLocal)
        self.up_level_server.clicked.connect(self.upLevel_Server)
        self.download.clicked.connect(self.download_button)
        self.delete_server.clicked.connect(self.deleteServer)
        self.server_rename_button.clicked.connect(self.server_rename_but)
        self.local_rename_button.clicked.connect(self.local_rename_but)


    def login(self):
        self.user = self.username.text()
        print("username:",self.user)
        self.passwd_enter = self.password.text()
        print("password",self.passwd_enter)
        self.ftp = FTP('')
        try:
            self.ftp.connect('localhost', 1025)
            if self.user=="admin" and self.passwd_enter=="123456":
                self.ftp.login(self.user, self.passwd_enter)
                print("Başarılı giriş yapılmıştır")
                self.showServerList()
        except ftplib.all_errors as e:
            print(e)

    def serverDirs(self):
        self.showdirServer = self.server_list.currentItem().text()
        if '.' not in self.Value2:
            try:
                self.ftp.cwd(self.showdirServer)
                self.showServerList()
            except:
                pass
        else:
            pass

    def localDirs(self):
        self.showdirLocal = self.local_list.currentItem().text()
        self.Cdir = os.getcwd()
        self.NewDir = self.Cdir + chr(92) + self.showdirLocal
        try:
            os.chdir(self.NewDir)
            self.showLocalList()
        except:
            pass

    def showServerList(self):
        self.server_list.clear()
        self.DirLst = self.ftp.nlst()
        for i in range(len(self.DirLst)):
            self.server_list.insertItem(i, (self.DirLst[i - 1]))

    def showLocalList(self):
        self.local_list.clear()
        self.LocalDirLst = os.listdir()
        for i in range(len(self.LocalDirLst)):
            self.local_list.insertItem(i, self.LocalDirLst[i - 1])

    def upLevel_Local(self):
        os.chdir("..")
        self.showLocalList()

    def upLevel_Server(self):
        self.ftp.cwd("..")
        self.showLocalList()

    def newFolder_server(self):
        self.newfolder_se = self.server_nf_et.text()
        if len(self.newfolder_se) < 1:
            print("Lütfen dosya ismi giriniz")
        else:
            self.ftp.mkd(self.newfolder_se)
            self.showServerList()
            self.server_nf_et.setText("")

    def newFolder_local(self):
        self.newfolder_lc = self.local_nf_et.text()
        if len(self.newfolder_lc) < 1:
            print("Lütfen dosya ismi giriniz")
        else:
            os.makedirs(self.newfolder_lc)
            self.showLocalList()
            self.local_nf_et.setText("")

    def local_rename_but(self):
        self.rn_lc = self.local_rename_et.text()
        self.currentname_local = self.local_list.currentItem().text()
        if len(self.newfolder_se) < 1:
            print("Lütfen dosya ismi giriniz")
        else:
            os.rename(self.currentname_local, self.rn_lc)
            self.showLocalList()
            self.local_rename_et.setText("")

    def server_rename_but(self):
        self.currentname_server = self.server_list.currentItem().text()
        self.rn_se = self.server_rename_et.text()
        if len(self.newfolder_se) < 1:
            print("Lütfen dosya ismi giriniz")
        else:
            self.ftp.rename(self.currentname_server,self.rn_se)
            self.showServerList()
            self.server_rename_et.setText("")

    def deleteLocal(self):
        self.delValue_local = self.local_list.currentItem().text()
        self.Cdir3 = os.getcwd()
        self.NewDir3 = self.Cdir3 + chr(92) + self.delValue_local
        shutil.rmtree(self.NewDir3)
        self.showLocalList()

    def deleteServer(self):
        self.delValue_server = self.server_list.currentItem().text()
        self.ftp.rmd(self.delValue_server)
        self.showServerList()

    def upload_button(self):
        self.uploadValue_local = self.local_list.currentItem().text()
        self.Cdir4 = os.getcwd()
        self.NewDir4 = self.Cdir4 + chr(92) + self.uploadValue_local
        self.ftp.storbinary('STOR ' + self.uploadValue_local, open(self.uploadValue_local, 'rb'))
        self.showServerList()

    def download_button(self):
        self.downloadValue = self.server_list.currentItem().text()
        dosya = open(self.downloadValue, 'wb')
        self.ftp.retrbinary('RETR ' + self.downloadValue, dosya.write, 1024)
        dosya.close()
        self.showLocalList()


def main():
    app = QApplication(sys.argv)
    win = ApplicationWindow()
    win.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())