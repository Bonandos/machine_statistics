from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP
import psutil, time, socket, socket, sys, json

def windows_logs():
    return 0

def generate_statistic():
    data = {}
    data['cpu'] = psutil.cpu_percent(interval=1)
    data['memory_usage'] = psutil.virtual_memory().used
    data['up_time'] = int(time.time()-psutil.boot_time())
    data['windows_logs'] = windows_logs()
    return data 

def encrypt(str):
    public_key  = './public_rsa_key.pem'
    key = RSA.importKey(open(public_key).read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(str.encode('utf-8'))

if __name__ == '__main__':
    HOST, PORT = sys.argv[1], 9999 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    print('Capturing data...')
    info = generate_statistic()
    print('Connection to server...')
    try:
        sock.connect((HOST, PORT))
        print('Sending captured info...')
        sock.sendall(encrypt(json.dumps(info)))
    finally:
        print('Exiting...')
        sock.close()
       
