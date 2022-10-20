from eth_account import Account


def generate():
    acct = Account.create()
    privateKey = acct.key
    privateKeyInHex = privateKey.hex()
    print(privateKeyInHex + '     This is your private key. Save It And Not Share It')
    with open('privateKeyInHex.txt','w') as f:
        f.write(privateKeyInHex)
    return privateKey, privateKeyInHex.zfill(64), acct.address, acct
