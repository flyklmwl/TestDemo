import paramiko
import os
import time

jres_ar_hostname = ['172.16.10.64', '172.16.10.65']
uc_hostname = ['172.16.10.67', '172.16.10.68']
admin_hostname = ['172.16.10.66']

port = '22'
username = 'root'
password = 'Hnwjs@123'
# jres_ar_cmd1 = 'su - cprs'
jres_ar_cmd = 'su -c "/home/cprs/tomcats/tomcat-jres-ar-8050/bin/startup.sh" cprs'
eclp_cmd = 'su -c "/home/cprs/tomcats/tomcat-eclp-8075/bin/startup.sh" cprs'

chengdudao_cmd = 'su -c "/home/cprs/tomcats/tomcat-chengdudao-8082/bin/startup.sh" cprs'
munandao_cmd = 'su -c "/home/cprs/tomcats/tomcat-munandao-8086/bin/startup.sh" cprs'
uc_as_cmd = 'su -c "/home/cprs/tomcats/tomcat-uc-as-8074/bin/startup.sh" cprs'
hps_as_cmd = 'su -c "/home/cprs/tomcats/tomcat-hps-as-8064/bin/startup.sh" cprs'

dalidao_cmd = 'su -c "/home/cprs/tomcats/tomcat-dalidao-8085/bin/startup.sh" cprs'
hq_cmd = 'su -c "/home/cprs/tomcats/tomcat-hq-8081/bin/startup.sh" cprs'

chongqidao_cmd = 'su -c "/home/cprs/tomcats/tomcat-chongqingdao-8084/bin/startup.sh" cprs'
hps_admin_cmd = 'su -c "/home/cprs/tomcats/tomcat-hps-admin-8063/bin/startup.sh" cprs'
uc_admin_cmd = 'su -c "/home/cprs/tomcats/tomcat-uc-admin-8073/bin/startup.sh" cprs'
bankgate_cmd = 'su -c "/home/cprs/tomcats/tomcat-hps-bankgate-web/bin/startup.sh" cprs'

alps_cmd = 'su -c "/home/cprs/tomcats/tomcat-alps-8083/bin/startup.sh" cprs'
uc_web_cmd = 'su -c "/home/cprs/tomcats/tomcat-uc-webapp-8072/bin/startup.sh" cprs'
hps_web_cmd = 'su -c "/home/cprs/tomcats/tomcat-hps-webapp-8062/bin/startup.sh" cprs'


def start(ip, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    #
    ssh.connect(ip, port, username, password, timeout=5)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    status = stdout.channel.recv_exit_status()
    if status == 0:
        print(cmd + "服务正常启动")
        time.sleep(20)
    else:
        print(cmd + "服务启动失败")
        exit(-1)
    ssh.close()


if __name__ == '__main__':
    # start jres_ar
    start(jres_ar_hostname[0], jres_ar_cmd)
    start(jres_ar_hostname[1], jres_ar_cmd)
    # start eclp
    start(jres_ar_hostname[1], eclp_cmd)
    # chengdudao\munandao\uc-as\hps-as
    start(jres_ar_hostname[0], chengdudao_cmd)
    start(jres_ar_hostname[1], chengdudao_cmd)

    start(jres_ar_hostname[0], munandao_cmd)
    start(jres_ar_hostname[1], munandao_cmd)

    start(uc_hostname[0], uc_as_cmd)
    start(uc_hostname[1], uc_as_cmd)

    start(uc_hostname[0], hps_as_cmd)
    start(uc_hostname[1], hps_as_cmd)

    # dalidao\hq
    start(jres_ar_hostname[0], dalidao_cmd)
    start(jres_ar_hostname[1], dalidao_cmd)

    start(jres_ar_hostname[0], hq_cmd)

    # chongqingdao\hps-admin\uc-admin\bankgate\alps\uc-web\hps-web
    start(jres_ar_hostname[0], chongqidao_cmd)
    start(jres_ar_hostname[1], chongqidao_cmd)

    start(admin_hostname[0], hps_admin_cmd)
    start(admin_hostname[0], uc_admin_cmd)
    start(admin_hostname[0], bankgate_cmd)

    start(uc_hostname[0], alps_cmd)
    start(uc_hostname[1], alps_cmd)

    start(uc_hostname[0], uc_web_cmd)
    start(uc_hostname[1], uc_web_cmd)

    start(uc_hostname[0], hps_web_cmd)
    start(uc_hostname[1], hps_web_cmd)











