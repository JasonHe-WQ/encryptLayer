from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encryptWithPassword():
    key = get_random_bytes(16)
    with open('ESAPassword.bin','wb') as f:
        f.write(key)
    cipher = AES.new(key, AES.MODE_EAX)
    with open('data.txt','r') as f:
        msg = f.read().encode('utf-8')
    bytesOfMsg = bytes(msg)
    ciphertext, tag = cipher.encrypt_and_digest(pad(data_to_pad=bytesOfMsg,block_size=AES.block_size))
    with open('encryptedData.bin','wb') as f:
        [ f.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    return key, cipher.nonce, tag, ciphertext