# Decrypting with the private key
import ecies

def decryptWithPrivateKey(privateKey):
    with open('encryptedData.bin', "rb") as f:
        encryptedData = f.read()
    # print(type(privateKey))
    # privateKey1 = hex(privateKey)
    # print(type(privateKey1))
    data = ecies.decrypt(privateKey, encryptedData)
    with open('text.bin', 'wb') as f:
        f.write(data)
    print(data)

# print(len(hex(0xcadd2665703540a989fbcf6c935509aa14a6e481c9670a6e4a1b4c33a68941ff)))
# print('type,len,hex',type(len(hex(0xcadd2665703540a989fbcf6c935509aa14a6e481c9670a6e4a1b4c33a68941ff))))
# print(decryptWithPrivateKey(0xcadd2665703540a989fbcf6c935509aa14a6e481c9670a6e4a1b4c33a68941ff))
