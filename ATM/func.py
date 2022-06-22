import random
from turtle import begin_fill
import pymysql
import base64
from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Util.py3compat import *

def toAES_base64(data):
        mode=AES.MODE_ECB
        style='pkcs7'
        key="HNUdatabase"
        _data = Padding.pad(data.encode('utf-8'), block_size=16, style=style)#填充
        amount_to_pad = 16 - (len(key) % 16)
        pad = bchr(0)
        _key=key.encode("utf-8") + pad * amount_to_pad
        cipher = AES.new(_key, mode=mode)
        return base64.b64encode(cipher.encrypt(_data)).decode("utf-8")

# 连接
parmas = {
    'host': '139.9.191.1',
    'port': 3306,
    'user': 'atm',
    'passwd': 'HNUdb',
    'db': 'atm',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor
}
mydb = pymysql.connections.Connection(**parmas)  # 连接数据库

#登录
def login(id,pwd):
    mycursor = mydb.cursor()
    cookie_tmp=0
    pwd1=toAES_base64(pwd)
    mycursor.callproc(procname='login',args=[id,pwd1,0,0])
    mycursor.execute(query='select @_login_0, @_login_1, @_login_2, @_login_3')
    res=mycursor.fetchall()
    print(res)
    state=res[0]["@_login_2"]
    cookie_tmp=res[0]["@_login_3"]
    mydb.commit()
    mycursor.close()
    if state==1:
        global cookie
        cookie=cookie_tmp
        return True
    return False

#开户
def signup(name,pwd,tel):
    mycursor=mydb.cursor()
    pwd1=toAES_base64(pwd)
    mycursor.callproc(procname='signup',args=[name,pwd1,tel,0,0])
    mycursor.execute(query='select @_signup_0, @_signup_1, @_signup_2, @_signup_3, @_signup_4')
    res=mycursor.fetchall()
    print(res)
    id=res[0]["@_signup_3"]
    info=res[0]["@_signup_4"]
    mydb.commit()
    mycursor.close()
    return id,info

# 取款
def cash_out(account_type,num):
    mycursor = mydb.cursor()  # 获取游标
    mycursor.callproc(procname='withdraw',args=[cookie,account_type,num,0,0,0])
    mycursor.execute(query='select @_withdraw_0, @_withdraw_1, @_witdraw_2, @_withdraw_3, @_withdraw_4, @_withdraw_5')
    res=mycursor.fetchall()
    state=res[0]["@_withdraw_3"]
    info=res[0]["@_withdraw_4"]
    balance=res[0]["@_withdraw_5"]
    mydb.commit()
    mycursor.close()
    print(info)
    return state, info,balance

# 存款
def deposit(account_type,num):
    mycursor = mydb.cursor()  # 获取游标
    mycursor.callproc(procname='save',args=[cookie,account_type,num,0,0,0])
    mycursor.execute(query='select @_save_0, @_save_1, @_save_2, @_save_3, @_save_4, @_save_5')
    res=mycursor.fetchall()
    state=res[0]["@_save_3"]
    info=res[0]["@_save_4"]
    balance=res[0]["@_save_5"]
    mydb.commit()
    mycursor.close()
    print(info)
    return state,info,balance
   
# 查询余额，返回余额值
def inquiry(account_type):
    mycursor = mydb.cursor()  # 获取游标
    mycursor.callproc(procname='inquiry',args=[cookie,account_type,0,0,0])
    mycursor.execute(query='select @_inquiry_0, @_inquiry_1, @_inquiry_2, @_inquiry_3, @_inquiry_4')
    res=mycursor.fetchall()
    name=res[0]["@_inquiry_2"]
    balance=res[0]["@_inquiry_3"]
    fbalance=res[0]["@_inquiry_4"]
    mydb.commit()
    mycursor.close()
    return name,balance,fbalance

# 转账
def transfer(your_account,my_account_type,your_account_type,num):
    mycursor=mydb.cursor()
    mycursor.callproc(procname='transfer',args=[cookie,your_account,my_account_type,your_account_type,num,0,0,0])
    mycursor.execute(query='select @_transfer_0, @_transfer_1, @_transfer_2, @_transfer_3, @_transfer_4, @_transfer_5,@_transfer_6, @_transfer_7')
    res=mycursor.fetchall()
    state=res[0]["@_transfer_5"]
    info=res[0]["@_transfer_6"]
    balance=res[0]["@_transfer_7"]
    mydb.commit()
    mycursor.close()
    print(info)
    return state,info,balance

#修改密码
def changepwd(oldpwd,newpwd):
    mycursor=mydb.cursor()
    pwd1=toAES_base64(oldpwd)
    pwd2=toAES_base64(newpwd)
    mycursor.callproc(procname='modify',args=[cookie,pwd1,pwd2,0,0])
    mycursor.execute(query='select @_modify_0, @_modify_1, @_modify_2, @_modify_3, @_modify_4')
    res=mycursor.fetchall()
    state=res[0]["@_modify_3"]
    info=res[0]["@_modify_4"]
    mydb.commit()
    mycursor.close()
    print(info)
    return state,info

#历史记录查询
def checkrecords(account_type,begin_day,end_day,select_method,sort_method):
    mycursor=mydb.cursor()
    mycursor.callproc(procname='history',args=[cookie,account_type,begin_day,end_day,select_method,sort_method])
    res1=mycursor.fetchall()
    ret=[]
    for res in res1:
        ans=[]
        ans.append(res["交易时间"])
        ans.append(res["交易类型"])
        ans.append(res["发起人或接收方"])
        ans.append(res["发起人或接收方类型"])
        ans.append(res["变动金额"])
        ans.append(res["余额"])
        ans.append(res["交易备注"])
        ret.append(ans)
    print(ret)
    mydb.commit()
    mycursor.close()
    return ret
