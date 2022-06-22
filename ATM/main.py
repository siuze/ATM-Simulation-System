import sys
import func
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
# import pics_rc
from atm import Ui_atm
from cash import Ui_cash
from cash1 import Ui_cash1
from login import Ui_login
from cashAccount import Ui_cashAccount
from signup import Ui_signup
from inquiry import Ui_inquiry
from record import Ui_record
from manager import Ui_manager
from deposit import Ui_deposit
from deposit1 import Ui_deposit1
from transfer import Ui_transfer
from card_out import Ui_card_out
from pwchange import Ui_pwchange
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from datetime import date
from datetime import datetime
account_type='活期'

# 管理员界面
class manager(QMainWindow, Ui_manager):
    def __init__(self):
        super(manager, self).__init__()
        self.setupUi(self)


# 输入身份信息界面
class signup(QMainWindow, Ui_signup):
    def __init__(self):
        super(signup, self).__init__()
        self.setupUi(self)


# 登陆界面
class login(QMainWindow, Ui_login):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
        self.count = 3
        self.account.setValidator(QtGui.QIntValidator())  #########
        self.pwd.setValidator(QtGui.QIntValidator())  #########

# 账户选择
class cashAccount(QMainWindow, Ui_cashAccount):
    def __init__(self):
        super(cashAccount, self).__init__()
        self.setupUi(self)


# ATM机界面
class atm(QMainWindow, Ui_atm):
    def __init__(self):
        super(atm, self).__init__()
        self.setupUi(self)


# 取款界面1
class cash(QMainWindow, Ui_cash):
    def __init__(self):
        super(cash, self).__init__()
        self.setupUi(self)


# 其他金额取款
class cash1(QMainWindow, Ui_cash1):
    def __init__(self):
        super(cash1, self).__init__()
        self.setupUi(self)
        self.amount.setValidator(QtGui.QIntValidator())  #########


# 存款界面1
class deposit(QMainWindow, Ui_deposit):
    def __init__(self):
        super(deposit, self).__init__()
        self.setupUi(self)


# 其他金额存款
class deposit1(QMainWindow, Ui_deposit1):
    def __init__(self):
        super(deposit1, self).__init__()
        self.setupUi(self)
        self.amount.setValidator(QtGui.QIntValidator())  #########


# 转账界面
class transfer(QMainWindow, Ui_transfer):
    def __init__(self):
        super(transfer, self).__init__()
        self.setupUi(self)


# 查询界面
class inquiry(QMainWindow, Ui_inquiry):
    def __init__(self):
        super(inquiry, self).__init__()
        self.setupUi(self)


#查询记录界面
class record(QMainWindow,Ui_record):
    def __init__(self):
        super(record,self).__init__()
        self.setupUi(self)


# 修改密码
class pwchange(QMainWindow, Ui_pwchange):
    def __init__(self):
        super(pwchange, self).__init__()
        self.setupUi(self)

# 取卡后界面
class card_out(QMainWindow, Ui_card_out):
    def __init__(self):
        super(card_out, self).__init__()
        self.setupUi(self)
        self.count = 10
        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer1 = QTimer(self)  # 初始化一个定时器
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.Refresh)

    def Refresh(self):
        if self.count > 0:
            self.label_time.setText(str(self.count))
            self.count -= 1
        else:
            self.timer.stop()
            self.count = 10


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    # 各种界面示例创建
    manager = manager()
    signup = signup()
    login = login()
    cashAccount = cashAccount()
    atm = atm()
    cash = cash()
    cash1 = cash1()
    deposit = deposit()
    deposit1 = deposit1()
    inquiry = inquiry()
    record = record()
    transfer = transfer()
    card_out = card_out()
    pwchange = pwchange()
    # 显示管理员界面
    manager.show()


    # 显示注册界面
    def show_signup():
        manager.close()
        signup.show()


    # 显示登录界面
    def show_login():
        manager.close()
        login.show()





    """
    输入身份信息，点确定开户，验证身份信息，并显示填写密码阶段
    判断用户填写的信息是否正确
    正确
    跳转到输密码界面
    姓名为空
    电话号码为空
    提示：电话号码不为空请重新输入
    提示：身份证号输入错误，请重新输入
    全部正确，显示密码确认界面，显示注册账号
    """




    # 从输入用户信息界面返回管理员界面
    def signup_return_manager():
        reply = QMessageBox.question(signup, '询问', '您正在进行开户操作，确认退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            signup.name.setText("")
            signup.tel.setText("")
            #signup.id.setText("")
            signup.close()
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass


    def signup_confirm():
        if len(signup.name.text()) == 0:
            QMessageBox.warning(signup, '警告', '姓名不为空，请重新输入！')
        elif len(signup.tel.text()) == 0:
            QMessageBox.warning(signup, '警告', '电话不为空，请重新输入！')
        elif len(signup.tel.text()) > 12:
            QMessageBox.warning(signup, '警告', '电话号码不规范，请重新输入！')
        if len(signup.pwd.text()) == 0:
            QMessageBox.warning(signup, '警告', '密码不为空，请重新输入！')
        elif signup.pwd.text() != signup.pwd1.text():
            QMessageBox.warning(signup, '警告', '密码不一致，请重新输入！')
        elif len(signup.pwd.text()) != 6:
            QMessageBox.warning(signup, '警告', '密码长度为六位，请重新输入！')
        else:

            name = signup.name.text()
            pwd = signup.pwd.text()
            tel = signup.tel.text()
            id,info=func.signup(name,pwd,tel)
            QMessageBox.information(signup, '通知', f'{info}，您的卡号为：{str(id)}\n请妥善保存您的卡号和密码！')
            signup.close()
            signup.name.setText("")
            signup.pwd.setText("")
            signup.pwd1.setText("")
            # signup.account.setText("")
            manager.show()  # show()方法显示窗口

    def pwchange_return_manager():
        reply = QMessageBox.question(pwchange, '询问', '确认退出更改？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pwchange.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    def pwchange_confirm():
        if pwchange.newpw.text() != pwchange.confirmpw.text():
            QMessageBox.warning(pwchange, '警告', '密码不一致，请重新输入！')
        else:
            state,info=func.changepwd(pwchange.oldpw.text(), pwchange.newpw.text())
            QMessageBox.information(pwchange, '通知', info)
            if state==1:
                pwchange.close()
                atm.show()


    # 登陆界面返回管理员界面
    def login_return_manager():
        reply = QMessageBox.question(login, '询问', '确认退出登录？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            login.account.setText("")
            login.pwd.setText("")
            login.close()
            login.count = 3
            manager.show()  # show()方法显示窗口
        elif reply == QMessageBox.No:
            pass

    def try_login():
        if len(login.account.text()) == 0:
            QMessageBox.warning(login, '警告', '账号不为空，请重新输入！')
        elif len(login.pwd.text()) == 0:
            QMessageBox.warning(login, '警告', '密码为空，请重新输入！')
        elif len(login.pwd.text()) != 6:
            QMessageBox.warning(login, '警告', '密码不规范，请重新输入！')
        if func.login(login.account.text(), login.pwd.text()):
            QMessageBox.information(signup, '通知', f'登录成功')
            login.close()
            login.pwd.setText("")
            cashAccount.show()
        else:
            QMessageBox.warning(login, '警告', '登陆失败，请重新输入！')


    def choose_type(type):
        global account_type
        account_type=type
        cashAccount.close()
        atm.show()

    # 显示取款界面1
    def show_cash():
        atm.close()
        cash.show()


    # 显示取款界面2
    def show_cash1():
        cash.close()
        cash1.show()


    # 显示存款界面1
    def show_deposit():
        atm.close()
        deposit.show()


    # 显示存款界面2
    def show_deposit1():
        deposit.close()
        deposit1.show()


    # 显示转账界面
    def show_transfer():
        atm.close()
        transfer.show()


    def show_pwchange():
        atm.close()
        pwchange.show()

    # 显示查询界面
    def show_inquiry():
        name, balance, fbalance=func.inquiry(account_type)
        inquiry.balance.setText(str(balance))
        inquiry.balance1.setText(str(fbalance))
        inquiry.balance_2.setText(str(account_type))
        atm.close()
        inquiry.show()

    #显示记录界面
    def show_record():
        atm.close()
        record.show()

    #从记录界面返回ATM界面
    def record_return_atm():
        QMessageBox.information(record, '提示', '正在退出查询记录界面，请保管好您的财物！')
        record.close()
        atm.show()
  
    # 从取款界面1返回ATM界面
    def cash_return_atm():
        QMessageBox.information(cash, '提示', '正在退出取款界面，请保管好您的财物！')
        cash.close()
        atm.show()


    # 从取款界面2返回ATM界面
    def cash1_return_atm():
        reply = QMessageBox.question(transfer, '询问', '您正在进行取款操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash1.amount.setText("")
            cash1.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 从存款界面1返回ATM界面
    def deposit_return_atm():
        QMessageBox.information(deposit, '提示', '正在退出存款界面！')
        deposit.close()
        atm.show()


    # 从存款界面2返回ATM界面
    def deposit1_return_atm():
        reply = QMessageBox.question(deposit1, '询问', '您正在进行存款操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit1.amount.setText("")
            deposit1.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 转账界面返回ATM界面
    def transfer_return_atm():
        reply = QMessageBox.question(transfer, '询问', '您正在进行转账操作，确认退出？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            transfer.amount.setText("")
            transfer.close()
            atm.show()
        elif reply == QMessageBox.No:
            pass


    # 查询界面返回ATM界面
    def inquiry_return_atm():
        QMessageBox.question(inquiry, '提示', '正在退出查询界面')
        inquiry.balance.setText("")
        inquiry.balance1.setText("")
        inquiry.close()
        atm.show()


    # 以下是各种退卡操作
    def record_show_card_out():
        reply = QMessageBox.question(atm, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            record.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def atm_show_card_out():
        reply = QMessageBox.question(atm, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            atm.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def cash_show_card_out():
        reply = QMessageBox.question(cash, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def cash1_show_card_out():
        reply = QMessageBox.question(cash1, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            cash1.amount.setText("")
            cash1.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def deposit_show_card_out():
        reply = QMessageBox.question(deposit, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def deposit1_show_card_out():
        reply = QMessageBox.question(deposit1, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            deposit1.amount.setText("")
            deposit1.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def transfer_show_card_out():
        reply = QMessageBox.question(transfer, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            transfer.amount.setText("")
            transfer.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    def inquiry_show_card_out():
        reply = QMessageBox.question(inquiry, '询问', '确认退出服务？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            inquiry.balance.setText("")
            inquiry.balance1.setText("")
            inquiry.close()
            login.account.setText("")
            card_out.timer.start()
            card_out.timer1.start(12000)
            card_out.show()
        elif reply == QMessageBox.No:
            pass


    # 各种取款操作
    def cash_out(money):
        reply = QMessageBox.question(cash, '询问', f'确认取款{str(money)}元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            state,info,balance=func.cash_out(account_type,money)
            if state>0:
                    QMessageBox.question(cash, '提示', info)
            else:
                QMessageBox.warning(cash, '警告', info)
        elif reply == QMessageBox.No:
            pass
    
    #记录操作
    def record_out(begin_day,end_time,select_method):
        reply = QMessageBox.question(cash, '询问', '确认查询？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            row = record.tableWidget.rowCount()
            for i in range(row):
                record.tableWidget.removeRow(0)
            ans=func.checkrecords(account_type,begin_day,end_time,select_method,1)
            #show records
            # begin
            for i in range(len(ans)):
                item = ans[i]
                row = record.tableWidget.rowCount()
                record.tableWidget.insertRow(row)
                for j in range(len(item)):
                    fill = QTableWidgetItem(str(item[j]))
                    record.tableWidget.setItem(row, j, fill)
            # end
        elif reply == QMessageBox.No:
            pass

    # 跳转其他金额取款界面
    def cash_other():
        cash.close()
        cash1.show()


    # 其他金额取款
    def cash_confirm():
        if cash1.amount.text() == 0:
            QMessageBox.warning(cash1, '警告', '取款金额不为0！')
        elif int(cash1.amount.text()) % 100 != 0:
            QMessageBox.warning(cash1, '警告', '取款金额必须为100整数倍！')
        else:
            reply = QMessageBox.question(cash1, '询问', f'确认取款{cash1.amount.text()}元？', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)
            if reply == QMessageBox.Yes:
                state, info, balance = func.cash_out(account_type, cash1.amount.text())
                if state > 0:
                    QMessageBox.question(cash, '提示', info)
                else:
                    QMessageBox.warning(cash, '警告', info)
                cash1.amount.setText("")
            elif reply == QMessageBox.No:
                pass


    # 存款操作
    def deposit_in(money):
        reply = QMessageBox.question(deposit, '询问', f'确认存款{money}元？', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            state,info,balance=func.deposit(account_type,money)
            QMessageBox.question(deposit, '提示', info)
        elif reply == QMessageBox.No:
            pass


    # 跳转其他金额存款界面
    def deposit_other():
        deposit.close()
        deposit1.show()


    # 其他金额存款
    def deposit_confirm():
        if deposit1.amount.text() == 0:
            QMessageBox.warning(deposit1, '警告', '存款金额不为0！')
        elif int(deposit1.amount.text()) % 100 != 0:
            QMessageBox.warning(deposit1, '警告', '存款金额必须为100整数倍！')
        else:
            reply = QMessageBox.question(deposit1, '询问', f'确认存款 {deposit1.amount.text()} 元？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                state, info, balance = func.deposit(account_type, deposit1.amount.text())
                QMessageBox.question(deposit, '提示', info)
                deposit1.amount.setText("")
            elif reply == QMessageBox.No:
                pass


    # 确认转账操作
    def transfer_confirm():
            to_type=''
            if transfer.to_cb.currentText()=='定期账户':
                to_type='定期'
            elif transfer.to_cb.currentText()=='活期账户':
                to_type='活期'
            elif transfer.to_cb.currentText() == '信用卡账户':
                to_type = '信用'
            state,info,balance=func.transfer(transfer.amount_2.text(),account_type,to_type,float(transfer.amount.text()) )
            QMessageBox.warning(transfer, '提示', info)


    # 退卡界面10秒后返回管理员界面
    def card_out_manager():
        card_out.close()
        card_out.timer1.stop()
        manager.show()

    #时间
    tod = date.today()
    today = str(datetime(tod.year, tod.month, tod.day + 1)).split(' ')[0]
    month = str(datetime(tod.year, tod.month - 1, tod.day)).split(' ')[0]
    year = str(datetime(tod.year - 1, tod.month, tod.day)).split(' ')[0]

    # 各种按键与函数连接
    manager.signup_btn.clicked.connect(show_signup)#主页面注册按钮
    manager.login_btn.clicked.connect(show_login)#主页面登录按钮

    signup.return_manager_btn.clicked.connect(signup_return_manager)#注册界面返回按钮
    signup.confirm_btn.clicked.connect(signup_confirm)#注册界面提交按钮


    login.login_btn.clicked.connect(try_login)
    login.return_manager_btn.clicked.connect(login_return_manager)
    cashAccount.livetime_btn.clicked.connect(lambda:choose_type('活期'))
    cashAccount.settime_btn.clicked.connect(lambda:choose_type('定期'))
    cashAccount.credit_btn.clicked.connect(lambda:choose_type('信用'))
    atm.cash_btn.clicked.connect(show_cash)
    atm.deposit_btn.clicked.connect(show_deposit)
    atm.transfer_btn.clicked.connect(show_transfer)
    atm.inquiry_btn.clicked.connect(show_inquiry)
    atm.record_btn.clicked.connect(show_record)
    atm.card_out_btn.clicked.connect(atm_show_card_out)
    atm.pwchange_btn.clicked.connect(show_pwchange)
    pwchange.login_btn.clicked.connect(pwchange_confirm)
    pwchange.back_btn.clicked.connect(pwchange_return_manager)

    record.one_btn.clicked.connect(lambda:record_out(today,today,1))
    record.month_btn.clicked.connect(lambda:record_out(month,today,0))
    record.year_btn.clicked.connect(lambda:record_out(year,today,0))
    record.return_btn.clicked.connect(record_return_atm)
    record.card_out_btn.clicked.connect(record_show_card_out)

    cash.btn100.clicked.connect(lambda:cash_out(100))
    cash.btn500.clicked.connect(lambda:cash_out(500))
    cash.btn1000.clicked.connect(lambda:cash_out(1000))
    cash.btn2000.clicked.connect(lambda:cash_out(2000))
    cash.other_amount_btn.clicked.connect(cash_other)
    cash.return_btn.clicked.connect(cash_return_atm)
    cash.card_out_btn.clicked.connect(cash_show_card_out)

    cash1.cash_btn.clicked.connect(cash_confirm)
    cash1.return_btn.clicked.connect(cash1_return_atm)
    cash1.card_out_btn.clicked.connect(cash1_show_card_out)

    deposit.btn100.clicked.connect(lambda:deposit_in(100))
    deposit.btn500.clicked.connect(lambda:deposit_in(500))
    deposit.btn1000.clicked.connect(lambda:deposit_in(1000))
    deposit.btn2000.clicked.connect(lambda:deposit_in(2000))
    deposit.btn5000.clicked.connect(lambda:deposit_in(5000))
    deposit.other_amount_btn.clicked.connect(deposit_other)
    deposit.return_btn.clicked.connect(deposit_return_atm)
    deposit.card_out_btn.clicked.connect(deposit_show_card_out)

    deposit1.deposit_btn.clicked.connect(deposit_confirm)
    deposit1.return_btn.clicked.connect(deposit1_return_atm)
    deposit1.card_out_btn.clicked.connect(deposit1_show_card_out)

    transfer.transfer_btn.clicked.connect(transfer_confirm)
    transfer.return_btn.clicked.connect(transfer_return_atm)
    transfer.card_out_btn.clicked.connect(transfer_show_card_out)

    inquiry.return_btn.clicked.connect(inquiry_return_atm)
    inquiry.card_out_btn.clicked.connect(inquiry_show_card_out)

    card_out.timer1.timeout.connect(card_out_manager)

    sys.exit(app.exec_())
