import decrypt1
import encrypt1
import encrypt2
import decrypt2
import generatePrivateKey
from eth_account import Account
import ESAEncrypt
import ESADecrypt
from eth_keys import keys
from eth_keys import KeyAPI

class mailbox():
    def __init__(self, ifHadAccount=False):
        self.senderAddr = 0x0
        self.encryptedBytes = bytes()
        self.__privateKey = 0x0
        self.address = 0x0
        self.publicKey = 0x0
        self.signature = bytes()
        self.ifOnline = False
        self.encryptType = 'RSA'
        self.encryptedMsg = str()
        self.password = bytes()
        self.acct = object()
        self.senderPublicKey = 0x0
        """
        Initialize and Generate a EVM account.The Private Key Will Be stored As A Parameter.
        When using again, please import your private key in HEX to continue your conversation.
        :param ifHadAccount:
        """
        if ifHadAccount is False:
            self.__privateKey,privateKeyInHex, self.address, self.acct = generatePrivateKey.generate()

        else:
            privateKeyInHex = input('Please Import Your Private Key In Hex')
            acct = Account.privateKeyToAccount(privateKeyInHex)
            self.__privateKey = acct.Key
            self.address = acct.address
        Keys = keys.PrivateKey(self.__privateKey)
        self.publicKey = Keys.public_key
        self.address = eval(KeyAPI.PublicKey.to_address(self.publicKey))


    def sign(self):
        """
        This method will read the encrypted file and generate a signed file name 'signedMessage.bin'
        :return:None
        """
        self.signature = encrypt1.signWithPrivateKey(self.__privateKey)
        print('The Signature has been saved as "signedMessage.bin"')

    def encrypt(self, senderPublicKey=None, Type='RSA'):
        """
        This method will read the text file named 'data.txt' and generate an encrypted text file named
        'encryptedData.txt' with the receiver's address
        :param fromAddr:When the parameter 'Type' is set as RSA, please provide the address of receiver
        :param Type:'RSA' for default Ethereum encrypt function, 'ESA' for using same password both sides knew
        :return:
        """
        self.encryptType = Type
        if self.encryptType == 'RSA':
            if senderPublicKey is None:
                self.senderPublicKey = self.publicKey
            self.encryptedBytes = encrypt2.encryptWithPublicKey(self.senderPublicKey)

        elif self.encryptType == 'ESA':
            self.password, nonce, tag, self.encryptedBytes = ESAEncrypt.encryptWithPassword()

        else:
            raise 'Error, Not supported encrypt type'

    def decrypt(self, fromAddr=None, password=None):
        """
        This method will decrypt and print the data
        :param fromAddr: When self.encryptType == 'RSA', please use this parameter
        :param password: When self.encryptType == 'ESA', please use this parameter
        :return:
        """
        if fromAddr is None:
            fromAddr = self.address
        self.senderAddr = fromAddr
        addr = eval(decrypt2.verify(senderAddr=self.senderAddr))
        ans = bool(addr==self.senderAddr)
        if ans:
            print('Address matched')
            flag = True
        else:
            print(addr)
            print("Addresses don't match")
            raise ValueError
        if self.encryptType == 'RSA':
            decrypt1.decryptWithPrivateKey()
        else:
            print("Please make sure your password is encoded as bytes and saved in 'ESAPassword.bin'")
            if password is None:
                with open('ESAPassword.bin', 'rb') as f:
                    password = f.read()
            while flag:
                """
                Note that the code generates a ValueError exception when tampering is detected 
                or the password doesn't match.
                """
                try:
                    text = ESADecrypt.ESADecrypt(password)
                    print(text)
                    break
                except ValueError:
                    print('Password Wrong or Tampering Detected')
                    print('Please Check Again')
                    ifAgain = input('Another Try?')
                    if ifAgain is None or False:
                        flag = False

    def sendOnline(self):
        """
        Not Completed Yet
        :return:
        """
        pass


msg = mailbox()
msg.encryptType = 'RSA'
msg.sign()
msg.decrypt()
