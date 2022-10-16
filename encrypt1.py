# Encrypting with the public key
from web3.auto import w3
from eth_account.messages import encode_defunct

def encryptWithPublicKey(data):

    msg = data
    with open('prvate')
    private_key =
    message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=private_key)