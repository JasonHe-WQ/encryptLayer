# Decrypting with the private key
import ecies

def decryptWithPrivateKey(privateKey):
    with open('encryptedData.bin', "rb") as f:
        encryptedData = f.read()
    print(encryptedData)
    print(type(privateKey))
    privateKey = str(hex(eval(privateKey)))
    print(type(privateKey))
    print(len(privateKey))
    data = ecies.decrypt(privateKey, encryptedData)
    with open('text.bin', 'wb') as f:
        f.write(data)
    print(data)