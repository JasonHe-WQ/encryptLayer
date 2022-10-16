# import decrypt1
# import encrypt1
# import encrypt2
# import decrypt2
import generatePrivateKey
from eth_account import Account


class mailbox():
    def __init__(self, ifHadAccount=False):
        """
        Initialize and Generate a EVM account
        :param ifHadAccount:
        """
        if ifHadAccount == False:
            generatePrivateKey.generate()
        else:
            privateKeyInHex = input('Please Import Your Private Key In Hex')
            with open("private.txt", "w") as f:
                f.write(privateKeyInHex)

            acct = Account.privateKeyToAccount(privateKeyInHex)
            with open("receiver.txt", "w") as f:
                f.write(acct.address)

    # def encrypt(self):
    #     encrypt1.encryptWithPublicKey('data.txt')
    #
    # def sign(self):
    #     encrypt2.signWithPrivateKey()
    #
    # def dycrypt(self):
    #     if decrypt2.verify():
    #         decrypt1.decryptWithPrivateKey()
    #     else:
    #         raise "ERROR"


msg = mailbox()

