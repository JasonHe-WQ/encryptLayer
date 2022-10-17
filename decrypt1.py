# Decrypting with the private key
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA


def decryptWithPrivateKey(filePath='encryptedData.bin', Type=1):

    with open(filePath, "rb") as f:
        f.read()
    with open('text.txt','w') as f:
        f.write(data)
    print(data)

