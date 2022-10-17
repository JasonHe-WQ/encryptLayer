# Signing with the private key
from web3.auto import w3
from eth_account.messages import encode_defunct


def signWithPrivateKey(privateKey):
    with open('encrypted.txt', 'r') as f:
        msg = f.read()
        message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=privateKey)
    msgHash, r, s, v, sig = signed_message
    with open('msgHash.bin', 'wb') as f:
        f.write(msgHash)
    with open('signature.bin', 'wb') as f:
        f.write(sig)
    with open('rsv.txt', 'w') as f:
        f.write(str(r) + '\n')
        f.write(str(s) + '\n')
        f.write(str(v) + '\n')

