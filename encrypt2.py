# Encrypting with your public key
import ecies


def encryptWithPublicKey(publicKey):
    with open('data.txt', 'r') as f:
        msg = f.read().encode('utf-8')
    assert len(publicKey) == 130
    encryptedData = ecies.encrypt(publicKey, bytes(msg))
    with open('encryptedData.bin', 'wb') as f:
        f.write(encryptedData)
    print('The encrypted data has been saved as "encryptedData.bin" encrypted by {}'.format(publicKey))
    return encryptedData

