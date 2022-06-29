# -*- coding:utf-8 -*-
import wmi
import time


def sys_version(ipaddress, user, password):
    conn = wmi.WMI(computer=ipaddress, user=user, password=password)
    for sys in conn.Win32_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF8"), "Vernum:%s" % sys.BuildNumber)  # 系统信息
        print(sys.OSArchitecture.encode("UTF8"))                                                 # 系统的位数
        print(sys.NumberOfProcesses)                                                    # 系统的进程数
    # get_cpu_mem
    # getcpu(conn)
    # get_disk(conn)
    network(conn)


def network(conn):                      # 获取MAC和IP地址
    for interface in conn.Win32_NetworkAdapterConfiguration (IPEnabled=1):
        print("MAC: %s" % interface.MACAddress)
    for ip_address in interface.IPAddress:
        print("ip_add: %s" % ip_address)
    print

# 获取自启动程序的位置
    for s in conn.Win32_StartupCommand():
        print("[%s] %s <%s>" % (s.Location.encode("UTF8"), s.Caption.encode("UTF8"), s.Command.encode("UTF8")))
# 获取当前运行的进程
    for process in conn.Win32_Process():
        print(process.ProcessId, process.Name)


def get_disk(conn):
    for physical_disk in conn.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                print(physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption)
    for disk in conn.Win32_LogicalDisk(DriveType=3):
        print(disk.Caption, "%0.2f%% free" % (100.0 * float(disk.FreeSpace) / float(disk.Size)))


def get_cpu_mem(conn):
    for processor in conn.Win32_Processor():   # print "Processor ID: %s" % processor.DeviceID
        print("Process Name: %s" % processor.Name.strip())
    for Memory in conn.Win32_PhysicalMemory():
        print("Memory Capacity: %.fMB" % (int(Memory.Capacity)/1048576))


def getcpu(conn):
    while True:
        for cpu in conn.Win32_Processor():
            timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
            print('%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage))
            time.sleep(5)


if __name__ == '__main__':
    sys_version(ipaddress="172.16.10.36", user="administrator", password="hnwjs@168")

