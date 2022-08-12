import sqlite3
import os

con = sqlite3.connect('example.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS webclass')
cur.execute('DROP TABLE IF EXISTS t_webinfo')
cur.execute('CREATE TABLE webclass(type text)')
cur.execute('''CREATE TABLE t_webinfo(
            title text,
            link text,
            img text,
            desc text,
            type text
            )''')

path = "E:\网页模板\博客个人"
file_name_list = os.listdir(path)


for i, file_name in enumerate(file_name_list):
    if "_" in file_name:
        title, desc = file_name.split("_")[0], file_name.split("_")[1][:-4]
    elif "是" in file_name:
        title, desc = file_name.split("是")[0], file_name.split("是")[1][:-4]
    else:
        title, desc = file_name.split("模板")[0], file_name.split("模板")[1][:-4]
    file_name = file_name[:-4].replace(" ", "%20")
    link = f"http://moduler.windcs.cn/{file_name}/index.html"
    img = "moduler.png"
    # 写入数据
    sql = f"INSERT INTO t_webinfo VALUES('{title}', '{link}', '{img}', '{desc}', '')"
    cur.execute(sql)

con.commit()
con.close()
