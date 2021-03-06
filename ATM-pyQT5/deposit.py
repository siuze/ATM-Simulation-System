# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deposit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deposit(object):
    def setupUi(self, deposit):
        deposit.setObjectName("deposit")
        deposit.resize(500, 400)
        deposit.setStyleSheet("#deposit{background-color: rgb(52, 80, 164);border-top-left-radius:15px;border-top-right-radius:5px;border-bottom-left-radius:15px;border-bottom-right-radius:5px}\n"
"")
        self.btn500 = QtWidgets.QPushButton(deposit)
        self.btn500.setGeometry(QtCore.QRect(0, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn500.setFont(font)
        self.btn500.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.btn500.setObjectName("btn500")
        self.btn1000 = QtWidgets.QPushButton(deposit)
        self.btn1000.setGeometry(QtCore.QRect(0, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn1000.setFont(font)
        self.btn1000.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.btn1000.setObjectName("btn1000")
        self.return_btn = QtWidgets.QPushButton(deposit)
        self.return_btn.setGeometry(QtCore.QRect(390, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.return_btn.setFont(font)
        self.return_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.return_btn.setObjectName("return_btn")
        self.other_amount_btn = QtWidgets.QPushButton(deposit)
        self.other_amount_btn.setGeometry(QtCore.QRect(390, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.other_amount_btn.setFont(font)
        self.other_amount_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.other_amount_btn.setObjectName("other_amount_btn")
        self.btn2000 = QtWidgets.QPushButton(deposit)
        self.btn2000.setGeometry(QtCore.QRect(390, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn2000.setFont(font)
        self.btn2000.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.btn2000.setObjectName("btn2000")
        self.label1 = QtWidgets.QLabel(deposit)
        self.label1.setGeometry(QtCore.QRect(120, 60, 271, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color:rgb(255, 0, 0)")
        self.label1.setScaledContents(False)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setWordWrap(False)
        self.label1.setOpenExternalLinks(False)
        self.label1.setObjectName("label1")
        self.card_out_btn = QtWidgets.QPushButton(deposit)
        self.card_out_btn.setGeometry(QtCore.QRect(-10, 310, 120, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.card_out_btn.setFont(font)
        self.card_out_btn.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(255, 0, 0);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.card_out_btn.setObjectName("card_out_btn")
        self.btn5000 = QtWidgets.QPushButton(deposit)
        self.btn5000.setGeometry(QtCore.QRect(390, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn5000.setFont(font)
        self.btn5000.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.btn5000.setObjectName("btn5000")
        self.btn100 = QtWidgets.QPushButton(deposit)
        self.btn100.setGeometry(QtCore.QRect(0, 90, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn100.setFont(font)
        self.btn100.setStyleSheet("QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;background-color: rgb(225, 225, 225);}\n"
"QPushButton:hover{background-color: rgb(14, 122, 255);border:none;color:rgb(255, 255, 255);}\n"
"QPushButton:checked{background-color: rgb(20, 62, 134);border:none;color:rgb(255, 255, 255);}")
        self.btn100.setObjectName("btn100")
        self.listView = QtWidgets.QListView(deposit)
        self.listView.setGeometry(QtCore.QRect(0, 0, 501, 401))
        self.listView.setStyleSheet("border-image:url(:/back/back.png)")
        self.listView.setObjectName("listView")
        self.listView.raise_()
        self.btn500.raise_()
        self.btn1000.raise_()
        self.return_btn.raise_()
        self.other_amount_btn.raise_()
        self.btn2000.raise_()
        self.label1.raise_()
        self.card_out_btn.raise_()
        self.btn5000.raise_()
        self.btn100.raise_()

        self.retranslateUi(deposit)
        QtCore.QMetaObject.connectSlotsByName(deposit)

    def retranslateUi(self, deposit):
        _translate = QtCore.QCoreApplication.translate
        deposit.setWindowTitle(_translate("deposit", "deposit"))
        self.btn500.setText(_translate("deposit", "500"))
        self.btn1000.setText(_translate("deposit", "1000"))
        self.return_btn.setText(_translate("deposit", "返 回 ->"))
        self.other_amount_btn.setText(_translate("deposit", "其他金额"))
        self.btn2000.setText(_translate("deposit", "2000"))
        self.label1.setText(_translate("deposit", "请选择存款金额！"))
        self.card_out_btn.setText(_translate("deposit", "<- 退 卡"))
        self.btn5000.setText(_translate("deposit", "5000"))
        self.btn100.setText(_translate("deposit", "100"))
