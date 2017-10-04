from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP
import random, string, os, zipfile


private_key = './main/private_rsa_key.pem'
public_key  = './client/public_rsa_key.pem'

def generate_keys():
    print('Bonandos:/# Generating keys                ',end='')
    key = RSA.generate(2048)
    with open(private_key, 'wb') as f:
        f.write(key.exportKey())        
    with open(public_key,'wb') as f:
        f.write(key.publickey().exportKey())
    print('[OK]')

def _zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def package_folder(path,name):
    print('Bonandos:/# Building client app            ',end='')
    zipf = zipfile.ZipFile('{}.zip'.format(name), 'w', zipfile.ZIP_DEFLATED)
    _zipdir(path, zipf)
    zipf.close()
    print('[OK]')

def encrypt(str):
    key = RSA.importKey(open(public_key).read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(str.encode('utf-8'))
    
def decrypt(str):
    key = RSA.importKey(open(private_key).read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(str).decode()

if __name__ == '__main__':
    print('You should not run this file! Run App.py instead.')   