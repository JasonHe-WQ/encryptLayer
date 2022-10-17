# Verifying signature with your private key
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


def verify(filepath='sig.bin', fileBeforeSign='encrypted_data.bin'):
    f = open('signed_message.bin','rb')
    signed_message
    publicKey = RSA.import_key(pubKey)
    hashObj = SHA256.new(toEncyrpt)
    verified = PKCS1_v1_5.new(publicKey)
    return verified.verify(hashObj, signature)