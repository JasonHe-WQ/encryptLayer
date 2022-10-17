# Decrypting with the private key
import ecies

def decryptWithPrivateKey(privateKey):
    with open('encryptedData.bin', "rb") as f:
        encryptedData = f.read()
    print(type(privateKey))
    privateKey = str(hex(privateKey))
    data = ecies.decrypt(privateKey, encryptedData)
    with open('text.bin', 'wb') as f:
        f.write(data)
    print(data)
decryptWithPrivateKey(0x6749a15e1dc36310a36d30791557f9b93e13b262f20a982fd859ba800581f215)