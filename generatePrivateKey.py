from eth_account import Account


def generate():
    acct = Account.create()
    privateKey = acct.key
    privateKeyInHex = privateKey.hex()
    print(privateKeyInHex + '   Save It And Not Share It')
    with open('privateKeyInHex.txt','w') as f:
        f.write(privateKeyInHex)
    return privateKey, privateKeyInHex, acct.address, acct
