# Decrypting with the private key
import ecies


def decryptWithPrivateKey(filePath='encryptedData.bin'):

    with open(filePath, "rb") as f:
        encryptedData = f.read()
    data = ecies.decrypt(9,encryptedData)
    with open('text.txt','w') as f:
        f.write(data)
    print(data)

