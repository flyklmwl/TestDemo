from mysql import connector
import random

src = 'abcdefghijklmnopqrstuvwxyz'


def get_data_list(n):
    res = []
    for i in range(n):
        res.append((get_str(2,4),get_str(8,12)))
    return res


def output():
    cur.execute('select * from mytab')
    for sid,name,ps in cur:
        print(sid,' ',name,' ',ps)


def output_all():
    cur.execute('select * from mytab')
    for item in cur.fetchall():
        print(item)

def get_str(param, param1):
    str_num = random.randint(param,param1)
    astr = ''
    for i in range(str_num):
        astr += random.choice(src)
    return astr






if __name__ == '__main__':
    print('建立连接...')
    con = connector.connect(host='172.16.10.51', user='root',password='12345678',database = 'test')
    print('建立游标...')
    cur = con.cursor()
    print('创建一张表mytab...')
    cur.execute('create table mytab(id int primary key auto_increment not null,name text,passwd text)')
    print('插入一条记录...')
    cur.execute('insert into mytab (name,passwd) values(%s,%s)',(get_str(2,4),get_str(8,12),))
    print('显示所有记录...')
    output()
    print('批量插入多条记录')
    cur.executemany('insert into mytab (name,passwd) values(%s,%s)',get_data_list(3))
    print('显示所有记录...')
    output_all()
    print('更新一条记录...')
    cur.execute('update mytab set name=%s where id = %s',('aaa',1))
    print('显示所有记录....')
    output()
    print('删除一条记录...')
    cur.execute('delete from mytab where id=%s',(3,))
    print('显示所有记录：')
    output()
    con.commit()
    cur.close()
    con.close()
