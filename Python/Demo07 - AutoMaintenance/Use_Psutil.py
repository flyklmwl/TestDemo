# coding:utf-8
import paramiko
import psutil
import time
import datetime



hostname = '172.16.20.33'
port = '22'
username = 'root'
password = 'Flykl3321*'


if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password, timeout=5)

    # CPU
    print('CPU逻辑数量: ' + str(psutil.cpu_count()))
    print('CPU核心数量: ' + str(psutil.cpu_count(logical=False)))
    print('CPU利用率: ' + str(psutil.cpu_percent()) + '%')
    print('内存利用率: ' + str(psutil.virtual_memory().percent) + '%')
    print('磁盘利用率: ' + str(psutil.disk_usage('/')))


#  这里看的是本机的信息了
# 当前时间
now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
print(now_time)

# 查看cpu物理个数的信息
print(u"物理CPU个数: %s" % psutil.cpu_count(logical=False))

#CPU的使用率
cpu = (str(psutil.cpu_percent(1))) + '%'
print(u"cup使用率: %s" % cpu)

#查看内存信息,剩余内存.free  总共.total
#round()函数方法为返回浮点数x的四舍五入值。

free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))
total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))
memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)
print(u"物理内存： %s G" % total)
print(u"剩余物理内存： %s G" % free)
print(u"物理内存使用率： %s %%" % int(memory * 100))
# 系统启动时间
print(u"系统启动时间: %s" % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

# 系统用户
users_count = len(psutil.users())
#
# >>> for u in psutil.users():
# ...   print(u)
# ...
# suser(name='root', terminal='pts/0', host='61.135.18.162', started=1505483904.0)
# suser(name='root', terminal='pts/5', host='61.135.18.162', started=1505469056.0)
# >>> u.name
# 'root'
# >>> u.terminal
# 'pts/5'
# >>> u.host
# '61.135.18.162'
# >>> u.started
# 1505469056.0
# >>>

users_list = ",".join([u.name for u in psutil.users()])
print(u"当前有%s个用户，分别是 %s" % (users_count, users_list))

#网卡，可以得到网卡属性，连接数，当前流量等信息
net = psutil.net_io_counters()
bytes_sent = '{0:.2f} Mb'.format(net.bytes_recv / 1024 / 1024)
bytes_rcvd = '{0:.2f} Mb'.format(net.bytes_sent / 1024 / 1024)
print(u"网卡接收流量 %s 网卡发送流量 %s" % (bytes_rcvd, bytes_sent))

io = psutil.disk_partitions()
# print(io)
# print("io[-1]为",io[-1])
#del io[-1]

print('-----------------------------磁盘信息---------------------------------------')

print("系统磁盘信息：" + str(io))

for i in io:
    o = psutil.disk_usage(i.device)
    print("总容量：" + str(int(o.total / (1024.0 * 1024.0 * 1024.0))) + "G")
    print("已用容量：" + str(int(o.used / (1024.0 * 1024.0 * 1024.0))) + "G")
    print("可用容量：" + str(int(o.free / (1024.0 * 1024.0 * 1024.0))) + "G")

print('-----------------------------进程信息-------------------------------------')
# 查看系统全部进程
for pnum in psutil.pids():
    p = psutil.Process(pnum)
    print(u"进程名 %-20s  内存利用率 %-18s 进程状态 %-10s 创建时间 %-10s " \
    % (p.name(), p.memory_percent(), p.status(), p.create_time()))

