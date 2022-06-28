import paramiko
import os

hostname = '192.168.0.151'
port = '22'
username = 'root'
password = '123456'


if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #
    ssh.connect(hostname, port, username, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command('iostat')
    print(stdout.read())
