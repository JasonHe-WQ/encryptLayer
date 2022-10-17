# Signing with your private key
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


def encryptWithPublicKey(address):
    with open("private.pem", 'r') as priFile:
        priKey = priFile.read()
    privateKey = RSA.import_key(priKey)
    with open(filepath, 'rb') as f:
        toEncyrpt = f.read()
    signer = PKCS1_v1_5.new(privateKey)
    hashObj = SHA256.new(toEncyrpt)
    signature = signer.sign(hashObj)
    with open('sig.bin', 'wb') as f:
        f.write(signature)



