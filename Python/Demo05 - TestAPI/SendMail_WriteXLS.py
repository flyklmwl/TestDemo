# !/usr/bin/python
# -*- coding: UTF-8 -*-

import xlwt
import time
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import xlrd
from datetime import datetime


# 创建附件--表格文件

def alcu():
    filename = '“掌上电力”手机APP日常巡检表' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    fr = open('1.xlsx', 'rb')
    w2 = open(filename, 'wb')  # a代表追加 w代表重写
    for line in fr:
        w2.write(line)
    fr.close()
    w2.close()
    return filename


def encu():
    settime = time.strftime('%Y-%m-%d')
    style0 = xlwt.easyxf('font: height 240')
    tall_style = xlwt.easyxf('font:height 380;')

    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    row0 = [u'序号', u'网省公司', u'用户名/手机号', u'密码', u'登陆所用时长', u'线上基本功能', u'巡检人', u'时间', u'手机型号', u'网络类型']
    for i in range(0, len(row0)):
        sheet.write(0, i, row0[i], style0)

    for i in range(1, 14):
        sheet.write(i, 0, i, style0)
        sheet.write(i, 1, u'公司', style0)
        sheet.write(i, 2, u'用户名/手机号', style0)
        sheet.write(i, 3, u'密码', style0)
        sheet.write(i, 4, str(random.randint(4, 8)) + 's', style0)
        sheet.write(i, 5, u'正常', style0)
        sheet.write(i, 6, u'巡检人', style0)
        sheet.write(i, 7, settime[0:10] + " " + str(i+7) + ":00:00", style0)
        sheet.write(i, 8, u'android', style0)
        sheet.write(i, 9, u'4G', style0)

    col_1 = sheet.col(1)
    col_2 = sheet.col(2)
    col_3 = sheet.col(3)
    col_4 = sheet.col(4)
    col_7 = sheet.col(7)
    col_1.width = 256 * 15
    col_2.width = 256 * 30
    col_3.width = 256 * 30
    col_4.witth = 256 * 25
    col_7.width = 256 * 30

    for i in range(0, 15):
        row_height = sheet.row(i)
        row_height.set_style(tall_style)

    emailfile = settime[0:10] + '.xls'
    wbk.save(emailfile)
    return emailfile


def sent_mail(emailfile):
    _user = "332105775@qq.com"
    _pwd = "optpqwnibnyabiag"
    # _to = #发送到邮箱
    # _to = "发送到邮箱"
    # _to = "发送到邮箱"
    _to = "332105775@qq.com"
    smtpSever='smtp.qq.com'        # 邮箱smtp Sever地址
    smtpPort = '465'                  # 开放的端口
    settime = time.strftime('%Y-%m-%d %H:%M:%S')
    #print(settime[0:10])

    message = MIMEMultipart()
    ##message['From'] = Header("标题" + settime[0:10], 'utf-8')
    #message['To'] = Header("zongbu", 'utf-8')

    message['From'] = formataddr([_user.rsplit("@")[0],_user]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    message['To'] = formataddr([_to.rsplit("@")[0],_to])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    subject = "邮件标题" + settime[0:10]
    message['data'] = Header(settime, 'utf-8')
    message['Subject'] = subject

    content = """   
        你好:</br>
        ... 
        <p>......</p>
        发送时间："""+settime+"""
    """

    #message.attach(MIMEText('附件标题', 'plain', 'utf-8'))
    message.attach(MIMEText(content, 'html', 'utf-8'))

    att1 = MIMEText(open(emailfile, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    #att1["Content-Disposition"] = 'attachment; filename="xunjian.xls"'
    att1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', emailfile))
    message.attach(att1)
    #print (message)

    try:
        s = smtplib.SMTP_SSL(smtpSever, smtpPort)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, message.as_string())
        s.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':   
    # sent_mail(encu())
    sent_mail(alcu())
    # alcu()

    # 手工指定附件
    # emailfile ="2018-08-03.xls"
    # sent_mail(emailfile)
