# Encrypting with your public key
import ecies


def encryptWithPublicKey(publicKey):
    with open('data.txt', 'r') as f:
        msg = f.read().encode('utf-8')
    publicKey = hex(publicKey)
    encryptedData = ecies.encrypt(publicKey, bytes(msg))
    with open('encryptedData.bin', 'wb') as f:
        f.write(encryptedData)
    print('The encrypted data has been saved as "encryptedData.bin"')
    return encryptedData
encryptWithPublicKey(0x017547c5eaae082fba7276c537a073d010d4000b7fa46e897f7b6849f3083f0a2456034a03631cc34392ef8d4c38f62aebcca32b08dc6202b47ead07b0a25b6b)
