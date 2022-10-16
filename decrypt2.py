# Verifying signature with your private key
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


def verify(filepath='sig.bin', fileBeforeSign='encrypted_data.bin'):
    with open("receiver.pem", 'r') as pubFile:
        pubKey = pubFile.read()
    with open(filepath, 'rb') as f:
        signature = f.read()
    with open(fileBeforeSign, 'rb') as f:
        toEncyrpt = f.read()
    publicKey = RSA.import_key(pubKey)
    hashObj = SHA256.new(toEncyrpt)
    verified = PKCS1_v1_5.new(publicKey)
    return verified.verify(hashObj, signature)
print(verify())