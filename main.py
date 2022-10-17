# import decrypt1
import encrypt1
import encrypt2
import decrypt2
import generatePrivateKey
from eth_account import Account
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


class mailbox():
    def __init__(self, ifHadAccount=False):
        self.__privateKey = 0x0
        self.address = 0x0
        self.signature = bytes()
        self.ifOnline = False
        self.encryptType = 'RSA'
        self.encryptedMsg = str()
        self.password = bytes()
        """
        Initialize and Generate a EVM account.The Private Key Will Be stored As A Parameter
        :param ifHadAccount:
        """
        if ifHadAccount == False:
            self.__privateKey, self.address = generatePrivateKey.generate()

        else:
            privateKeyInHex = input('Please Import Your Private Key In Hex')
            acct = Account.privateKeyToAccount(privateKeyInHex)
            self.__privateKey = privateKeyInHex
            self.address = acct.address

    def sign(self):
        """
        This method will read the encrypted file and generate a signed file name 'signedMessage.bin'
        :return:None
        """
        self.signature = encrypt1.signWithPrivateKey(self.__privateKey)
        print('The Signature has been saved as "signedMessage.bin"')

    def encrypt(self, fromAddr = None, Type = 'RSA'):
        """
        This method will read the text file named 'data.txt' and generate an encrypted text file named
        'encryptedData.txt' with the receiver's address
        :param fromAddr:When the parameter 'Type' is set as RSA, please provide the address of receiver
        :param Type:'RSA' for default Ethereum encrypt function, 'ESA' for using same password both sides knew
        :return:
        """

        if self.encryptType=='RSA':
            if fromAddr is None:
                fromAddr = self.address
            self.senderAddr = fromAddr
            self.encrptedBytes = encrypt2.encryptWithPublicKey(self.senderAddr)

        elif self.encryptType=='ESA':
            pass

        else:
            raise 'Error, Not supported encrypt type'


    def dycrypt(self, fromAddr = None):
        if self.encryptType=='RSA':
            if fromAddr is None:
                fromAddr = self.address
            self.senderAddr = fromAddr
            ans, addr = decrypt2.verify(senderAddr=self.senderAddr)
            if ans:
                print('Address matched')
                # decrypt1.decryptWithPrivateKey()
            else:
                print(addr)
                print("Addresses don't match")
        else:
            input('Please input your password')


    def sendOnline(self):
        """
        Not Completed Yet
        :return:
        """
        pass


msg = mailbox()
msg.sign()
msg.dycrypt()
