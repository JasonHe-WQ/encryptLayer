# Signing with the private key
from web3.auto import w3
from eth_account.messages import encode_defunct


def signWithPrivateKey(privateKey):

    with open('encrypted.txt', 'r') as f:
        msg = f.read()
        message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    msgHash, r, s, v, sig  = signed_message
    with open('signed.bin','wb') as f:
        f.write(signed_message)

encryptWithPublicKey(0x93ad253e9f5ce913e36706eb147b99652389686f249554ea3cbf51d022c2ee51)