from pyzabbix import ZabbixAPI
import sys

ZABBIX_SERVER = 'http://172.16.10.74:8081'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin', 'zabbix')

def hostItemAllInfo(user, host_name, item):
    '''根据主机名和监控key，返回该监控项的数据'''
    item =  user.item.get(host=host_name, search={"key_": item}, output="extend")
    if len(item) != 0:
      return item
    else:
      return None

def getItems(zapi, key, hostid, hostname):
    items = zapi.item.get(search={"key_":key}, hostids=hostid , output="extend")
    if(len(items)==0):
        print ("item key: %s not found in hostname: %s" % (key,hostname))
        # sys.exit()
    else:
        return items

if '__main__' == __name__:
    # 获取主机
    host_list = zapi.host.get(
        output="extend",
    )
    all_total_mem = 0
    all_total_disk = 0
    for host in host_list:
        # print(host)
        cpu_num = 0
        total_disk = 0
        host = {
          key:value for key, value in host.items()
          if key in ["hostid", "name"]
        }
        if host['name'] in ["www.windcs.cn","crawl.windcs.cn"]:
            pass
        elif host['name'] in ["app36", "172.16.20.13", "proxy"]:
            cpu_num = getItems(zapi, 'wmi.get[root/cimv2,"Select NumberOfLogicalProcessors from Win32_ComputerSystem"]', host['hostid'], host['name'])[0]['lastvalue']
            total_mem = round(float(getItems(zapi, 'vm.memory.size[total]', host['hostid'], host['name'])[0]['lastvalue'])/1024/1024/1024)
            total_disk = round(int(getItems(zapi, 'vfs.fs.size[C:,total]', host['hostid'], host['name'])[0]['lastvalue'])/1024/1024/1024, 2)
        else:
            cpu_num = getItems(zapi, 'system.cpu.num', host['hostid'], host['name'])[0]['lastvalue']
            total_mem = round(float(getItems(zapi, 'vm.memory.size[total]', host['hostid'], host['name'])[0]['lastvalue'])/1024/1024/1024)
            try:
                total_disk = round(int(getItems(zapi, 'vfs.fs.size[/,total]', host['hostid'], host['name'])[0]['lastvalue'])/1024/1024/1024, 2)
            except:
                print("没有该监控项目")
        if host['name'] not in ["www.windcs.cn","crawl.windcs.cn"]:
            # pass
            print(host['name'] + f" cpu 核数为: {cpu_num}个")
            print(host['name'] + f" 内存为: {total_mem}GB")
            print(host['name'] + f" 磁盘总量为: {total_disk}GB")
        all_total_mem += total_mem
        all_total_disk += total_disk
        
    
    print(f"主机总数为: " + str(len(host_list)) + "台")
    print(f"总内存数为: " + str(all_total_mem) + "GB")
    print(f"总磁盘数为: " + str(round(all_total_disk, 2)) + "GB")


