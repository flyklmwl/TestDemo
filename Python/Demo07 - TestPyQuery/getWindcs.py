from pyquery import PyQuery as pq
import requests
import sqlite3

webinfo = []
webclass = []

url = "http://nav.windcs.cn/cn/index.html#"
html = requests.get(url)
html.encoding = "utf-8"

doc = pq(html.text)    
# print(doc)            

# 获取分类信息
items = doc(".text-gray").items()
for item in items:
    webclass.append(item.text())


# 获取索引详细信息
items = doc(".col-sm-3").items()
for item in items:
    # print(item)
    data = {
      "link": item('.xe-widget.xe-conversations.box2.label-info').attr('data-original-title'),
      "img": item('.lozad.img-circle').attr('data-src'),
      "title": item('.xe-user-name.overflowClip_1').text(),
      "desc": item('.overflowClip_2').text(),
    }
    webinfo.append(data)
  
# print(webinfo)
# print(webclass)

# 导入数据

con = sqlite3.connect('webdb.db')
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

for webcls in webclass:
    sql = f"INSERT INTO webclass VALUES ('{webcls}')"
    cur.execute(sql)
  
for webhost in webinfo:
    if "'" in webhost['title']:
        webhost['title'] = webhost['title'].replace("'", "''")
        print(webhost['title'])
    if "'" in webhost['desc']:
        webhost['desc'] = webhost['desc'].replace("'", "''")
    sql = f"INSERT INTO t_webinfo VALUES('{webhost['title']}', '{webhost['link']}', '{webhost['img']}', '{webhost['desc']}', '')"
    print(sql)
    cur.execute(sql)

con.commit()
con.close()
