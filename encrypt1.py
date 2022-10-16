# Encrypting with the private key
from web3.auto import w3
from eth_account.messages import encode_defunct


def encryptWithPublicKey(type, privateKey):

    with open('encrypted.bin', 'r') as f:
        msg = f.readline()
        message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    with open('signed.bin')
