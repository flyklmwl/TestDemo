# !/usr/bin/python
# -*- coding: UTF-8 -*-

import xlwt
import time

style0 = xlwt.easyxf('font: height 240')
tall_style = xlwt.easyxf('font:height 380;')

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')
row0 = [u'序号', u'网省公司', u'用户名/手机号', u'密码', u'登陆所用时长', u'线上基本功能', u'巡检人', u'时间', u'手机型号', u'网络类型']
for i in range(0, len(row0)):
    sheet.write(0, i, row0[i], style0)

for i in range(1, 14):
    sheet.write(i, 0, i, style0)
    sheet.write(i, 1, u'湖南公司', style0)
    sheet.write(i, 2, u'wind1314/15116432193', style0)
    sheet.write(i, 3, u'Flykl3321', style0)
    sheet.write(i, 4, u'4s', style0)
    sheet.write(i, 5, u'正常', style0)
    sheet.write(i, 6, u'傅超', style0)
    sheet.write(i, 7, time.strftime("%Y-%m-%d", time.localtime()) + " " + str(i+7) + ":00:00", style0)
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
# sheet.Cells(1, 1).Font.Size = 20

for i in range(0, 15):
    row_height = sheet.row(i)
    row_height.set_style(tall_style)

# sheet.write(0,0,'序号')
wbk.save(time.strftime("%Y-%m-%d", time.localtime()) + '.xls')