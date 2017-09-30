from Crypto.PublicKey import RSA
import random

def generate(path):
    key = RSA.generate(2048)
    secret_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))


    
    with open('{}/public_rsa_key.pem'.format(path),'wb') as f:
        f.write(key.)