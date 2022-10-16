# Decrypting with the private key
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA


def decryptWithPrivateKey(filePath='encrypted_data.bin', data=None, Type=1):
    with open("private.pem") as pkFile:
        pk = pkFile.read()
    private_key = RSA.import_key(pk)
    if Type == 1:
        file_in = open(filePath, "rb")
    else:
        file_in = data

    enc_session_key, nonce, tag, ciphertext = \
        [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    file_in.close()

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag).decode('utf-8')
    with open('text.txt','w') as f:
        f.write(data)
    print(data)

