import decrypt1
import encrypt1
import encrypt2
import decrypt2
import generatePrivateKey
import findPublicKey
from eth_account import Account
import ESAEncrypt
import ESADecrypt
from eth_keys import keys
from eth_keys import KeyAPI
import sentToBlockChain


class mailbox():
    def __init__(self, ifHadAccount=False):
        self.senderAddr = 0x0
        self.encryptedBytes = bytes()
        self.__privateKey = bytes()
        self.__privateKeyInHex = str()
        self.address = 0x0
        self.publicKey = str()
        self.signature = bytes()
        self.ifOnline = False
        self.encryptType = 'RSA'
        self.encryptedMsg = str()
        self.password = bytes()
        self.acct = object()
        self.senderPublicKey = 0x0
        self.ifGenerate = bool()
        """
        Initialize and Generate a EVM account.The Private Key Will Be stored As A Parameter and A str in file.
        When using again, please import your private key in HEX to continue your conversation.
        :param ifHadAccount:
        """
        if ifHadAccount is False:
            self.__privateKey, self.__privateKeyInHex, self.address, self.acct = generatePrivateKey.generate()
            self.ifGenerate = False

        else:
            privateKeyInHex = input('Please Import Your Private Key In Hex')
            acct = Account.privateKeyToAccount(privateKeyInHex)
            self.__privateKey = acct.key
            self.address = acct.address
            self.__privateKeyInHex = privateKeyInHex
            self.ifGenerate = True
        Keys = keys.PrivateKey(self.__privateKey)
        self.publicKey = Keys.public_key
        self.address = eval(KeyAPI.PublicKey.to_address(self.publicKey))
        self.publicKey = hex(self.publicKey).zfill(130)
        print('Your public key is {}:', self.publicKey)
        print(len(self.publicKey))
        print('Your address is   {}'.format(hex(self.address)))
        # publicKey and privateKey are stored as '0x' and will be use as str hex and stored in 'privateKeyInHex.txt'.


    def sign(self):
        """
        This method will read the encrypted file and generate a signed file name 'signedMessage.bin'
        :return:None
        """
        self.signature = encrypt1.signWithPrivateKey(self.__privateKeyInHex)
        print('The Signature by address:  {} has been saved as "signedMessage.bin"'.format(hex(self.address)))

    def encrypt(self, senderPublicKey=None, senderAddr=None, Type='RSA'):
        """
        This method will read the text file named 'data.txt' and generate an encrypted text file named
        'encryptedData.txt' with the receiver's address
        :param senderPublicKey:When the parameter 'Type' is set as RSA and transactions hash can't be found on chain,
         please provide the senderPublicKey of receiver in Hex
        :param senderAddr:When the parameter 'Type' is set as RSA, please provide the address of receiver in Hex
        :param Type:'RSA' for default Ethereum encrypt function, 'ESA' for using same password both sides knew
        :return:
        """
        senderPublicKey = '0x' + hex(senderPublicKey)[2:].zfill(128)
        self.encryptType = Type
        if self.encryptType == 'RSA':
            if senderAddr is None:
                if eval(senderPublicKey) == 0:
                    self.senderPublicKey = self.publicKey
                else:
                    self.senderPublicKey = senderPublicKey
            else:
                """
                If the sender has made any tx, you can get the public key. Else, you can only send message to
                who revealed the public key.
                Network support: ETH,BNB,Polygon
                """
                self.senderAddr = hex(senderAddr)
                # self.senderPublicKey = findPublicKey.find(self.senderAddr)
                """
                IT DOES NOT WORK RIGHT NOW
                """
                self.senderPublicKey = self.publicKey
            if self.senderPublicKey is not None:
                self.encryptedBytes = encrypt2.encryptWithPublicKey(self.senderPublicKey)
            else:
                return

        elif self.encryptType == 'ESA':
            self.password, nonce, tag, self.encryptedBytes = ESAEncrypt.encryptWithPassword()

        else:
            raise 'Error, Not supported encrypt type'

    def decrypt(self, senderAddr=None,  password=None):
        """
        This method will decrypt and print the data
        :param senderAddr: When self.encryptType == 'RSA', please use this parameter with Hex
        :param password: When self.encryptType == 'ESA', please use this parameter with BytesSrting
        :return:
        """
        if senderAddr is not None:
            self.senderAddr = senderAddr
        ans = decrypt2.verify(senderAddr=self.senderAddr)
        if ans:
            print('Address matched')
            flag = True
        else:
            print("Addresses don't match, it should be the message sender's address")
            return
        if self.encryptType == 'RSA':
            decrypt1.decryptWithPrivateKey(self.__privateKey)
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

    def sendOnline(self, permanent=False):
        if permanent is True:
            if self.ifGenerate is False:
                raise "No token to spend gas fee"
            chainID = input('Please choose the chain you would like to use\n1: Ethereum, 137: Polygon')
            """
            1: Ethereum, 137: Polygon
            """
            tx = sentToBlockChain.send(chainID, self.address, self.senderAddr, self.__privateKey)
            print('Your encrypted data has been sent with tx=\n{}'.format(tx))
        else:
            print("This message will be stored on a centralize server for 7 days.")
            pass
        """
        Not Completed Yet
        :return:
        """


msg = mailbox(ifHadAccount=False)
msg.encryptType = 'ESA'
msg.encrypt(
    senderPublicKey=0x017547c5eaae082fba7276c537a073d010d4000b7fa46e897f7b6849f3083f0a2456034a03631cc34392ef8d4c38f62aebcca32b08dc6202b47ead07b0a25b6b,
    senderAddr=None)
msg.sign()
msg.decrypt(senderAddr=0x5568BC7EebC605A88e247769c4acA92d95BC9360,password=None)
msg.sendOnline(True)
