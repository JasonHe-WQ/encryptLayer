# Signing with your private key
import ecies

def encryptWithPublicKey(publicKey):
    with open('data.txt','r') as f:
        msg = f.read().encode('utf-8')
    encryptedData = ecies.encrypt(publicKey,bytes(msg))
    with open('encryptedData.bin','wb') as f:
        f.write(encryptedData)
    return encryptedData




