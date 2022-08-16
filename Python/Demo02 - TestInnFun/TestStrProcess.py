#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def teststrip():
    cstring = "http://moduler.windcs.cn/clean%20Blog极简个人博客主页模板_极简%20简洁%20个人%20博客%20blog主页%20blog/index.html"
    print(cstring)
    sstring = cstring.lstrip("http://moduleran.windcs.cn/")
    # .replace("%20", " ").rstrip("/index.html")
    print(sstring)

    tstr = "http://www.baidu.com/du0.ab"
    fstr = "http://www.baidu.com/"
    ffstr = tstr.lstrip(fstr)
    print(ffstr)
    # 截取25个字符以后的字符串
    fffstr = cstring[25:]
    print(fffstr)

    ss = 'hello, world!!!'
    print(ss.strip('hello, '))
    # 仅从左侧开始匹配
    print(ss.lstrip('hello, '))  
    print(ss.lstrip('whello, '))


def testrep():
    ss = "hello, world!!"
    print(re.match("hello", ss).span())
    print(re.match("hello", ss))
    print(re.match("hello", ss).group())

def main():
    teststrip()
    # testrep()


if __name__ == '__main__':
    main()
