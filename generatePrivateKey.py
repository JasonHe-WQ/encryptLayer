from Crypto.PublicKey import RSA

def generate():
    key = RSA.generate(1024)
    privateKey = key.export_key()
    with open("private.pem", "wb") as f:
        f.write(privateKey)

    publicKey = key.publickey().export_key()
    with open("receiver.pem", "wb") as f:
        f.write(publicKey)