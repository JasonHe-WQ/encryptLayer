# Decrypting with the private key
import ecies


def decryptWithPrivateKey(privateKey):
    if type(privateKey) == int:
        privateKey = hex(privateKey)
    with open('encryptedData.bin', "rb") as f:
        encryptedData = f.read()
    data = ecies.decrypt(privateKey, encryptedData)
    with open('text.bin', 'wb') as f:
        f.write(data)
    print(data)

