from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import random, string, os, zipfile

secret_code=''
private_key='./'
public_key='./'

def generate_keys(server_path,client_path):
    print('Bonandos:/# Generating keys                ',end='')
    key = RSA.generate(2048)
    secret_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8)    
    private_key = '{}/private_rsa_key.pem'.format(server_path)
    public_key  = '{}/public_rsa_key.pem'.format(client_path)
    with open(private_key, 'wb') as f:
        f.write(encrypted_key)        
    with open(public_key,'wb') as f:
        f.write(key.publickey().exportKey())
    print('[OK]')
    # print(encrypt('bonando'))
    

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
    recipient_key = RSA.import_key(open(public_key).read())
    session_key = get_random_bytes(16)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(str)
    return '{}{}{}{}'.format(cipher_rsa.encrypt(session_key),cipher_aes.nonce,tag,ciphertext)
    
def decrypt(str):
    rsa_private_key = RSA.import_key(open(private_key).read(),passphrase=secret_code)
    enc_session_key, nonce, tag, ciphertext = [fobj.read(x) for x in (rsa_private_key.size_in_bytes(), 16, 16, -1)]
    cipher_rsa = PKCS1_OAEP.new(rsa_private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    return cipher_aes.decrypt_and_verify(ciphertext, tag)

if __name__ == '__main__':
    print('You should not run this file! Run App.py instead.')   