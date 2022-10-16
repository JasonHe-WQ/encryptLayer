# Encrypting with the private key
from web3.auto import w3
from eth_account.messages import encode_defunct


def encryptWithPublicKey(type, privateKey):

    with open('encrypted.bin', 'rb') as f:
        msg = f.read()
        message = encode_defunct(text=str(msg))
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    with open('signed.bin')
