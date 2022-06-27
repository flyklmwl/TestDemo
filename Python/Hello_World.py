#!/usr/bin/env python
# -*- coding: utf-8 -*-
'a test module'
__author__ = 'Michael Liao'
import sys
import os


def test():
	# 这里是测试路径
	print("这个是执行路径：" + os.getcwd())
	print("这个是文件所在的路径：" + os.path.abspath(os.path.dirname(__file__)))
	help(sys)
	sys.__file__
	# 这里是测试输入参数
	args = sys.argv
	if len(args) == 1:
		print("Hello,world!")
	elif len(args) == 2:
		print("Hello,%s!" % args[1])
	else:
		print("Too many arguments")


if __name__ == '__main__':
	test()
