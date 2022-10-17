from eth_account import Account

def generate():


    acct = Account.create()
    privateKey = acct.key
    privateKeyInHex = privateKey.hex()
    print(privateKeyInHex +'   Save It And Not Share It')
    acct = Account.from_key(privateKey)
    print("Address:", acct.address)
    return privateKeyInHex, acct.address, acct