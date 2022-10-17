# Decrypting with the private key
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA


def decryptWithPrivateKey(filePath='encryptedData.bin', Type=1):

    with open(filePath, "rb") as f:
        f.read()

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag).decode('utf-8')
    with open('text.txt','w') as f:
        f.write(data)
    print(data)

