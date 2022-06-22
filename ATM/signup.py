# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup(object):
    def setupUi(self, signup):
        signup.setObjectName("signup")
        signup.resize(500, 400)
        signup.setFocusPolicy(QtCore.Qt.NoFocus)
        signup.setStyleSheet("#signup{background-color: rgb(52, 80, 164);border-top-left-radius:15px;border-top-right-radius:5px;border-bottom-left-radius:15px;border-bottom-right-radius:5px}\n"
"")
        self.return_manager_btn = QtWidgets.QPushButton(signup)
        self.return_manager_btn.setGeometry(QtCore.QRect(10, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.return_manager_btn.setFont(font)
        self.return_manager_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:20px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.return_manager_btn.setObjectName("return_manager_btn")
        self.label1 = QtWidgets.QLabel(signup)
        self.label1.setGeometry(QtCore.QRect(-20, 50, 331, 51))
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
        self.name = QtWidgets.QLineEdit(signup)
        self.name.setGeometry(QtCore.QRect(200, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setStyleSheet("")
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(signup)
        self.label.setGeometry(QtCore.QRect(120, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 0, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.confirm_btn = QtWidgets.QPushButton(signup)
        self.confirm_btn.setGeometry(QtCore.QRect(360, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:20px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.confirm_btn.setObjectName("confirm_btn")
        self.label_3 = QtWidgets.QLabel(signup)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tel = QtWidgets.QLineEdit(signup)
        self.tel.setGeometry(QtCore.QRect(200, 150, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.tel.setFont(font)
        self.tel.setStyleSheet("")
        self.tel.setObjectName("tel")
        self.label_2 = QtWidgets.QLabel(signup)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pwd = QtWidgets.QLineEdit(signup)
        self.pwd.setGeometry(QtCore.QRect(200, 200, 161, 31))
        self.pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd.setObjectName("pwd")
        self.label_4 = QtWidgets.QLabel(signup)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pwd1 = QtWidgets.QLineEdit(signup)
        self.pwd1.setGeometry(QtCore.QRect(200, 250, 161, 31))
        self.pwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd1.setObjectName("pwd1")
        self.listView = QtWidgets.QListView(signup)
        self.listView.setGeometry(QtCore.QRect(-10, -10, 511, 421))
        self.listView.setStyleSheet("border-image:url(:/back/back.png)")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.return_manager_btn.raise_()
        self.label1.raise_()
        self.name.raise_()
        self.label.raise_()
        self.confirm_btn.raise_()
        self.label_3.raise_()
        self.tel.raise_()
        self.label_2.raise_()
        self.pwd.raise_()
        self.label_4.raise_()
        self.pwd1.raise_()

        self.retranslateUi(signup)
        QtCore.QMetaObject.connectSlotsByName(signup)

    def retranslateUi(self, signup):
        _translate = QtCore.QCoreApplication.translate
        signup.setWindowTitle(_translate("signup", "signup"))
        self.return_manager_btn.setText(_translate("signup", "返回"))
        self.label1.setText(_translate("signup", "请填写您的身份信息！"))
        self.label.setText(_translate("signup", "姓名："))
        self.confirm_btn.setText(_translate("signup", "注册"))
        self.label_3.setText(_translate("signup", "身份证号："))
        self.label_2.setText(_translate("signup", "请输入密码："))
        self.label_4.setText(_translate("signup", "确认密码："))
