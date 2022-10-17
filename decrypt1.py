# Decrypting with the private key
import ecies


def decryptWithPrivateKey(filePath='encryptedData.bin'):

    with open(filePath, "rb") as f:
        encryptedData = f.read()
    with open('text.txt','w') as f:
        f.write(data)
    print(data)

