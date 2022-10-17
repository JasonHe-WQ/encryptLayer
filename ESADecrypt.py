from Crypto.Cipher import AES
def ESADecrypt(password):
    with open("encryptedData.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(password, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data, True
