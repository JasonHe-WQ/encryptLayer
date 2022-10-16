# Encrypting with the public key
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def encryptWithPublicKey(filepath):

    with open(filepath,'r') as f:

        toEncyrpt = f.read()
        toEncyrpt = toEncyrpt.encode('utf-8')
    data = toEncyrpt
    fileOut = open("encrypted_data.bin", "wb")

    recipientKey = RSA.import_key(open("receiver.pem").read())
    sessionKey = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipherRsa = PKCS1_OAEP.new(recipientKey)
    encSessionKey = cipherRsa.encrypt(sessionKey)

    # Encrypt the data with the AES session key
    cipherAes = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipherAes.encrypt_and_digest(data)
    [fileOut.write(x) for x in (encSessionKey, cipherAes.nonce, tag, ciphertext)]
    fileOut.close()
    return fileOut.name