import paramiko, time, threading

ip = "192.168.1.12"
user = "root"
passwd = "rudeboy2121"




def term():

    def execute(cmd):

        while True:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode())
            time.sleep(2)

    def fcall(cmd):

        t = threading.Thread(target=execute, args=(cmd,))
        t.start()


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 2121, username=user, password=passwd, timeout=200)

    fcall("ps -aux")
    fcall("df -h")
    fcall("ls -l")




term()
