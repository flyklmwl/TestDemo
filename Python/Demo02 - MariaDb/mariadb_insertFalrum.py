from mysql import connector
import random

src = 'abcdefghijklmnopqrstuvwxyz'


def get_data_list(n):
    res = []
    for i in range(n):
        res.append((get_str(2,4),get_str(8,12)))
    return res


def output():
    cur.execute('select * from flarum_discussions')
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
    con = connector.connect(host='172.16.10.51', user='root',password='12345678',database = 'flarum')
    print('建立游标...')
    cur = con.cursor()
    print('插入一条记录到discussions')
    sql = "insert into `flarum_discussions` (`is_approved`, `title`, `slug`, `created_at`, `user_id`, `is_private`) values (1, 'General', 'general', '2022-06-29 06:43:54', 1, 0)"
    cur.execute(sql)
    # print('获取disid')
    # getidsql = "select last_insert_id()"
    # print(cur.execute(getidsql))
    # output()
    con.commit()
    cur.close()
    con.close()
