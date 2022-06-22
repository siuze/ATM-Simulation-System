# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(506, 400)
        login.setStyleSheet("#login{background-color: rgb(52, 80, 164);border-top-left-radius:15px;border-top-right-radius:5px;border-bottom-left-radius:15px;border-bottom-right-radius:5px}\n"
"")
        self.return_manager_btn = QtWidgets.QPushButton(login)
        self.return_manager_btn.setGeometry(QtCore.QRect(10, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.return_manager_btn.setFont(font)
        self.return_manager_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.return_manager_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:20px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(255, 0, 0);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.return_manager_btn.setObjectName("return_manager_btn")
        self.label1 = QtWidgets.QLabel(login)
        self.label1.setGeometry(QtCore.QRect(80, 100, 321, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:rgb(255, 0, 0)")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setOpenExternalLinks(False)
        self.label1.setObjectName("label1")
        self.login_btn = QtWidgets.QPushButton(login)
        self.login_btn.setGeometry(QtCore.QRect(360, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:20px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color:rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.login_btn.setObjectName("login_btn")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(110, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 0, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(110, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(login)
        self.pwd.setGeometry(QtCore.QRect(190, 230, 161, 31))
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.account = QtWidgets.QLineEdit(login)
        self.account.setGeometry(QtCore.QRect(190, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.account.setFont(font)
        self.account.setStyleSheet("")
        self.account.setObjectName("account")
        self.listView = QtWidgets.QListView(login)
        self.listView.setGeometry(QtCore.QRect(0, 0, 511, 421))
        self.listView.setStyleSheet("border-image:url(:/back/back.png)")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.return_manager_btn.raise_()
        self.label1.raise_()
        self.login_btn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pwd.raise_()
        self.account.raise_()

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.return_manager_btn.setText(_translate("login", "退出 Exit"))
        self.label1.setText(_translate("login", "请输入您的卡号和密码！"))
        self.login_btn.setText(_translate("login", "登录 Login"))
        self.label.setText(_translate("login", "卡号："))
        self.label_2.setText(_translate("login", "密码："))
import hnu_rc
