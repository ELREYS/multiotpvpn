import paramiko
import sys
from paramiko import AuthenticationException


#Functions
def generateBC():
    command = "python /opt/scripts_lukas/generateBC.py "
    username = input("Please add a valid ldap username\n").replace(" ","")
    command += username
    command += " "
    mail = input("Please add a valid mail address\n").replace(" ","")
    command += mail
    print(command)
    return command

def unlockVPN():
    command = "/opt/multiotp-master/multiotp.php -unlock "
    username = input("Please add a valid vpn username\n").replace(" ","")
    command += username
    print(command)
    return command

def connect_and_execute(_command):

    server = "192.168.10.2"
    user = "gdilisa"

    command = _command
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, username=user, password='Magnolia2020')

    stdin, stdout, stderr = client.exec_command("{}".format(command))
    for line in stdout:
        try:
            print(line.strip('\n'))
        except Exception as e :
            print(e)
            client.close()

def execute_command(session,_command):

    stdin, stdout, stderr = session.exec_command("{}".format(_command))
    for line in stdout:
        try:
            print(line.strip('\n'))
        except Exception as e :
            print(e)
            session.close()


def connect_and_login(_username,_password) -> paramiko :

    server = "192.168.10.2"
    user = _username

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server, username=_username, password=_password)
        
    
    except AuthenticationException :
            print("Authentication failed")
            print(client.connect)
            return client
    
    return client

            

connect_and_login("gdilisa","Magnolia2020")
connect_and_execute("last | head")
