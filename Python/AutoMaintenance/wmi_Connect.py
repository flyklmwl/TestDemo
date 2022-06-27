# -*- coding:utf-8 -*-
import wmi

def sys_version(ipaddress, user, password):
    conn = wmi.WMI(computer=ipaddress, user=user, password=password)
    for sys in conn.Win32_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber)  # 系统信息
        print(sys.OSArchitecture.encode("UTF8"))                                                 # 系统的位数
        print(sys.NumberOfProcesses)                                                    # 系统的进程数


if __name__ == '__main__':
    sys_version(ipaddress="172.16.10.36", user="administrator", password="hnwjs@168")
