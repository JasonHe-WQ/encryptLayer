import decrypt1
import encrypt1
import encrypt2
import decrypt2
import generatePrivateKey

generatePrivateKey.generate()
encrypt1.encryptWithPublicKey('data.txt')
encrypt2.sigWithPublicKey()
if decrypt2.verify():
    decrypt1.decryptWithPrivateKey()
else:
    raise "ERROR"