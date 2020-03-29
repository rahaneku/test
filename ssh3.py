import paramiko, time, threading

ip = "192.168.1.12"
user = "root"
passwd = "rudeboy2121"




def term():

    def execute(cmd):

        while True:
            chan.send(cmd + '\n')
            output = chan.recv(6000)
            print(output.decode())
            time.sleep(1)

    def fcall(cmd):

        t = threading.Thread(target=execute, args=(cmd,))
        t.start()


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 2121, username=user, password=passwd, timeout=200)
    chan = ssh.invoke_shell()

    #fcall("ping 127.0.0.1")
    fcall("df -h")
    fcall("ls -l")




term()
