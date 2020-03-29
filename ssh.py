import paramiko, time, threading

#ip = "192.168.1.12"
user = "root"
passwd = "rudeboy2121"

def terminal(ip,name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 2121, username=user, password=passwd, timeout=200)
    while True:
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        print(stdout.read().decode())
        print(name)
        time.sleep(2)

def reggie(host,name):
    t = threading.Thread(target=terminal, args=(host,name))
    t.start()



reggie("192.168.1.12","first")

reggie("192.168.1.12","second")


