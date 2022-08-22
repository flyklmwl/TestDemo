#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author fifichao
# date 2022/08/18
import os
import rarfile
import random
import shutil
import paramiko
import sqlite3
import configparser

# configfile = configparser.ConfigParser()
# configfile.read("config.ini", encoding="utf-8")
#
# hostname = configfile.get("sys_config", "hostname")
# port = configfile.get("sys_config", "port")
# username = configfile.get("sys_config", "username")
# keyfile = configfile.get("sys_config", "keyfile")

con = sqlite3.connect('webdb.db')
cur = con.cursor()


def get_dir(dirpath):
    # print(len(os.listdir(dirpath)))
    dir_list = os.listdir(dirpath)
    return dir_list


def getmeta(dir_list):
    _count = 0
    shi_count = 0
    moduler_count = 0
    data_list = []
    for file_name in dir_list:
        if "_" in file_name:
            _count += 1
            title, desc = file_name.split("_")[0], file_name.split("_")[1][:-4]
        elif "是" in file_name:
            title, desc = file_name.split("是")[0], file_name.split("是")[1][:-4]
            shi_count += 1
        else:
            title, desc = file_name.split("模板")[0], file_name.split("模板")[1][:-4]
            moduler_count += 1
        # 判断文件名是否合法
        title = title.strip() if title.endswith(" ") else title
        data = {
            "filename": file_name,
            "title": title,
            "link": f"http://moduler.windcs.cn/Bg/{title}/index.html".replace(" ", "%20"),
            "img": "moduler.png",
            "desc": desc,
            "type": "后台管理",
        }
        data_list.append(data)
    return data_list


def unrarfile(basepath, data_list):
    upload_list = []
    z = ""
    for meta in data_list:
        # print(meta)
        full_path = basepath + meta["filename"]
        # print(full_path)
        z = rarfile.RarFile(full_path)
        z.extractall(basepath)
        oldfn = f"{basepath}{meta['filename'][:-4]}"
        newfn = f"{basepath}{meta['title']}"
        # print(f"oldfn： {oldfn}")
        # print(f"newfn: {newfn}")
        try:
            os.rename(oldfn, newfn)
        except FileExistsError:
            newfn = f"{newfn}{round(random.random() * 1000)}"
            os.rename(oldfn, newfn)
        # 查看是否该目录下是一个文件夹
        dircount = len(os.listdir(newfn))
        print(f"{newfn}：有{dircount}个子目录 ")
        if len(os.listdir(newfn)) != 1:
            print("---------------------手动分割-----------------------")
            print(f"该目录不止一个子文件夹: {newfn}")
        else:
            trans_name = os.listdir(newfn)[0]
            newdir = f"{newfn}/{trans_name}"
            shutil.move(newdir, basepath)
            os.rmdir(newfn)
            os.rename(f"{basepath}/{trans_name}", newfn)
            print(newdir)
            upload_list.append(newfn)
    z.close()
    return upload_list


# 有问题，sftp只能传单个文件，传输文件夹方法需要重新封装或者其他办法
def login_upload(upload_list):
    # private_key = paramiko.RSAKey.from_private_key_file(keyfile)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname, int(port), username, pkey=private_key)
    ariticle_count = 0
    sftp = ssh.open_sftp()

    for upload_data in upload_list:
        localpath = upload_data
        remotepath = "/docker-data/nginx/data/App/"
        sftp.put(localpath, remotepath)
        print(f"{upload_data}数据传输完成")
        ariticle_count += 1
    print(f"总共上传文档数： {ariticle_count}")
    ssh.close()


def insertdata(data_list):
    for data in data_list:
        sql = f"INSERT INTO modulerinfo(title, link, img, desc, type) VALUES('{data['title']}', '{data['link']}', '{data['img']}', '{data['desc']}', '{data['type']}')"
        cur.execute(sql)
    con.commit()
    con.close()


def main():
    basepath = 'F:/网页模板/app/'
    # 获取文件夹下的所有文件列表
    dir_list = get_dir(basepath)
    # 拿到文件列表的需要信息
    data_info = getmeta(dir_list)
    # 根据data_list文件列表信息 解压文件
    # upload_list = unrarfile(basepath, data_info)
    # 根据列表上传到目录
    # login_upload(upload_list)
    # 目录信息插入数据库
    print(data_info)
    insertdata(data_info)


if __name__ == '__main__':
    main()
