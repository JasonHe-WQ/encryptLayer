import decrypt1
import encrypt1
import encrypt2
import decrypt2
import generatePrivateKey


class mailbox():
    def __init__(self):
        generatePrivateKey.generate()

    def encrypt(self):
        encrypt1.encryptWithPublicKey('data.txt')

    def sign(self):
        encrypt2.signWithPrivateKey()

    def dycrypt(self):
        if decrypt2.verify():
            decrypt1.decryptWithPrivateKey()
        else:
            raise "ERROR"

msg = mailbox()
msg.encrypt()
msg.sign()
msg.dycrypt()