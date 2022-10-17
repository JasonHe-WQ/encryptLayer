from eth_account import Account

def generate():


    acct = Account.create()
    privateKey = acct.key
    privateKeyInHex = privateKey.hex()
    print(privateKeyInHex +'   Save It And Not Share It')
    return privateKey, privateKeyInHex, acct.address, acct