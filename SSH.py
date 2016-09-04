__author__ = 'Kirill'

import paramiko

host = '192.168.1.41'
user = 'kir'
secret = '853664'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('aptitude install zombi_virus')
data = stdout.read() + b"--------------------------------------\n" + stderr.read()
data2 = data.decode('utf-8')
my_file = open("some.txt", "w")
my_file.write(data2)
my_file.close()
print(data2)
client.close()

