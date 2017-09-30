from Crypto.PublicKey import RSA
import random

def generate(server_path,client_path):
    key = RSA.generate(2048)
    secret_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
    with open('{}/private_rsa_key.bin'.format(server_path), 'wb') as f:
        f.write(encrypted_key)        
    with open('{}/public_rsa_key.pem'.format(client_path),'wb') as f:
        f.write(key.publickey().exportKey())

if __name__ == '__main__':
    print('You should not run this file! Run App.py instead.')   