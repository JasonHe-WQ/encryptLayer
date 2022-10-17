from Crypto.Cipher import AES
def ESADecrypt(password):
    with open("encryptedData.bin", "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(password, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data


print(ESADecrypt(b'\x1b\xea>\xdc\x91b\xe8\x05v\xf7\x8b\xe6]\xa4gk'))