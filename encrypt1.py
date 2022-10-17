# Signing with the private key
from web3.auto import w3
from eth_account.messages import encode_defunct
import pickle

def signWithPrivateKey(privateKey):
    with open('encrypted.txt', 'r') as f:
        msg = f.read()
        message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    f = open('signed_message.bin', 'wb')
    pickle.dump(signed_message, f)
    f.close()
    print('Signed')
