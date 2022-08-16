import sqlite3

con = sqlite3.connect('webdb.db')
cur = con.cursor()

global txt_line


def gettxt():
    global txt_line
    txt_line = 0
    with open('e:/filename.txt', encoding='utf-8') as f:
      for line in f.readlines():##readlines(),函数把所有的行都读取进来；
        txt = line.strip()##删除行后的换行符，img_file 就是每行的内容啦
        txt_line += 1
        sql = f"select count(1) from check_file where filename = '{txt}'"
        for count in cur.execute(sql):
          num = count[0]
          # print(num, txt_line)
          if num == 0:
            print(f"没有找到的目录为: {txt}")
        
    print(f"总行数为: {txt_line}")
        # print(txt)


def getdb():
    data_list = []
    sql = "select link from modulerinfo"
    for link in cur.execute(sql):
      link = link[0][25:].replace("%20", " ")[:-11]
      data_list.append(link)
    return data_list

def insertdb(data_list_ex):
    for data in data_list_ex:
        sql = f"insert into check_file values ('{data}')"
        cur.execute(sql)
    con.commit()
    print("插入成功")
    

if __name__ == '__main__':
    gettxt()
    # data_list1 = getdb()
    # insertdb(data_list1)
    
