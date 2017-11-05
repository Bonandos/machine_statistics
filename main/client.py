import paramiko

def _connect(host,port,username,password):
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(host, port=port, username=username, password=password)
        # stdin, stdout, stderr = client.exec_command('cd /home/videos | ls')
        # print(stdout.read().decode())
    finally:
        return client

def _create_temp_location(client):
    client.exec_command('cd ~')
    client.exec_command('mkdir bonandos_temp')
    client.exec_command('ls / > teste.txt')
    return client

def main():
    client = _connect('host',22,'user','pwd')    
    client = _create_temp_location(client)
    stdin, stdout, stderr = client.exec_command('ls')
    print(stdout.read().decode())

if __name__ == '__main__':
    main()