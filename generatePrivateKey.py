from eth_account import Account
import secrets

def generate():


    privateKey = secrets.token_bytes(32)
    privateKeyInHex = '0x' + privateKey.hex()
    print(privateKeyInHex +'Save It And Not Share It')
    acct = Account.from_key(privateKey)
    print("Address:", acct.address)

    with open("private.txt", "w") as f:
        f.write(privateKeyInHex)

    with open("receiver.txt", "w") as f:
        f.write(acct.address)
