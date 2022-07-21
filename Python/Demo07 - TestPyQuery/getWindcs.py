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
  
print(webinfo)
print(webclass)

# 导入数据

con = sqlite3.connect('webdb.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS webclass 
               (type text)''')
for webcls in webclass:
  cur.execute("INSERT INTO webclass VALUES (f'{webcls}')")
  
con.commit()
con.close()