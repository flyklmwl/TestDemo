# coding:utf-8
import paramiko

# test address
test_address = ['ip']
# hncae
hn_address = ['ip']
win_address = ['ip']
# fubaosc
fubao_address = ['ip']
fubao_win_address = ['ip']
port = '22'
username = 'username'
password = 'passwd'
# cmd = "df -hP|awk '{print $5,$6}'|column -t"  # diskusage

# 上传shell来检测系统信息，并把检测的结果下载下载过来
if __name__ == '__main__':
    for ip in hn_address:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, username, password, timeout=5)

        sftp = ssh.open_sftp()
        sftp.put('Sys_Check.sh', '/username/Sys_Check.sh')
        print('上传脚本')
        stdin, stdout, stderr = ssh.exec_command("/bin/bash /username/Sys_Check.sh")
        print('执行脚本中......')
        stdout.readlines()  # 据说读完才继续往下执行
        stderr.readlines()  # 当我们去读取结果的时候程序就会等待命令执行完，这样就能判断出命令是完整的执行了！
        stdin, stdout, stderr = ssh.exec_command("ip a show dev eth0|grep -w inet|awk '"
                                                 "{print $2}'|awk -F '/' '{print $1}'")
        hostip = stdout.read().strip('\n')
        stdin, stdout, stderr = ssh.exec_command("date +%Y%m%d")
        hostdate = stdout.read().strip('\n')

        logfile = hostip + '-' + hostdate + '.txt'
        pathfile = '/username/logs/' + logfile
        destfile = hostip + '.txt'

        sftp.get(pathfile, destfile)
        ssh.close()

