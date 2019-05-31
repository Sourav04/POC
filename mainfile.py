import telnetlib
import socket
import os
def check_ping(fqdn):
    response = os.system("ping -c 1 " + fqdn)
    return response
def check_dns_entry(fqdn):
    response = os.system("nslookup " + fqdn)
    return response
def check_telent_connection(fqdn,port):
    response=1
    try:
        tn=telnetlib.Telnet(fqdn,port)
    except socket.error as e:
        response=0
    return response
def check_ad_entry(fqdn):
    response=1
    retvalue = os.popen("host -l ds.dtveng.net |grep {} |awk {}".format(fqdn,"awk '{print $1}'")).readlines())
    if len(retvalue) == 0:
        response=0