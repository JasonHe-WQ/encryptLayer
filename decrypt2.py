import pickle
from web3.auto import w3
from eth_account.messages import encode_defunct


def verify(senderAddr):
    f = open('signedMessage.bin', 'rb')
    signedMessage = pickle.load(f)
    f.close()
    with open('encrypted.txt', 'r') as f:
        encryptedMsg = f.read()
        Msg = encode_defunct(text=encryptedMsg)
    decryptedAddr = w3.eth.account.recover_message(Msg, signature=signedMessage.signature)
    if type(senderAddr) == str():
        senderAddr = eval(senderAddr)
    print('The assumed sender is {}'.format(hex(senderAddr)))
    print('The actual sender is {}'.format(eval(decryptedAddr)))
    return senderAddr == eval(decryptedAddr), decryptedAddr
