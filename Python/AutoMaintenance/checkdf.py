import paramiko
import sys

address = [37, 245]
outer_address = [18, 19, 20, 21]
outer_address1 = [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cmd="df"
cmd += " -h / |sed -n "  
cmd += "'3p'"
cmd += "| awk '"
cmd += "{printf $4 "
cmd += '"\\n"'
cmd += "}'"
    
for ip in outer_address:
    ssh.connect('172.31.193.' + str(ip), 10022, username='weblogic', password='Yxsjgl.w.' + str(ip))
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print('172.31.193.' + str(ip) + ': '  + stdout.readlines()[0])

for ip in outer_address1:
    ssh.connect('172.31.193.' + str(ip), 10022, username='weblogic', password='Yxsjgl.w.2016')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(str(ip) + ': '  + stdout.readlines()[0])


# for x in address:
    # print(typeof(x))
#    if x==37:
#        ssh.connect('10.223.57.' + str(x), 22, username='web', password='hpdl580.2016')
#        stdin, stdout, stderr = ssh.exec_command(cmd)
#        print('10.223.57.37: ' + stdout.readlines()[0])
        
#    if x==245:
#        ssh.connect('10.223.57.' + str(x), 10022, username='weblogic', password='hpdl580.2016')
#        stdin, stdout, stderr = ssh.exec_command(cmd)
#        print(stdout.readlines()[0])
    


# fout = open('file.txt', 'tw')
# sys.stdout = fout
# fout.close()


