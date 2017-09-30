def windows_logs():
    return 0

def generate_statistic():
    data = {}
    data['cpu'] = psutil.cpu_percent(interval=1)
    data['memory_usage'] = psutil.virtual_memory().used
    data['up_time'] = int(time.time()-psutil.boot_time())
    data['windows_logs'] = windows_logs()
    return data 

if __name__ == '__main__':
    import psutil, time, socket, socket, sys, json
    HOST, PORT = sys.argv[1], 9999 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    print('Capturing data...')
    info = generate_statistic()
    print('Connection to server...')
    try:
        sock.connect((HOST, PORT))
        print('Sending captured info...')
        sock.sendall(json.dumps(info),'utf-8'))
    finally:
        print('Exiting...')
        sock.close()
       
