import requests
from web3 import Web3

explorer = {
    '1': 'https://api.etherscan.io',
    '137': 'https://api.polygonscan.com',
    '80001': 'https://api-testnet.polygonscan.com/'
}
myToken = {
    '1': 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9',
    '137': '2KTHMFT4CIZ9WDIQWQIK9ESD7I9T1VCG5Q',
    '80001': '2KTHMFT4CIZ9WDIQWQIK9ESD7I9T1VCG5Q'

}
dataHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


def send(chainID, yourAddress, toAddress, privateKeyInBytes):
    APIList = {
        '1': 'https://rpc.ankr.com/eth',
        '137': 'https://polygon-rpc.com',
        '80001': 'https://rpc-mumbai.maticvigil.com'
    }
    print(type(toAddress))
    with open('signedMessage.bin', 'rb') as f:
        signedBytes = f.read()

    with open('encryptedData.bin', 'rb') as f:
        encryptedDataBytes = f.read()
    w3 = Web3(Web3.HTTPProvider(APIList[chainID]))
    gasOracleUrl = '{}/api?module=gastracker&action=gasoracle&apikey={}'.format(explorer[chainID],
                                                                                  myToken[chainID])
    # data = requests.get(gasOracleUrl, headers=dataHeader).json()
    # gasPrice = int(eval(data['result']['ProposeGasPrice'])*1000000000)
    rawHex = w3.eth.account.sign_transaction(dict(
        nonce=w3.eth.get_transaction_count(Web3.toChecksumAddress(hex(yourAddress))),
        maxFeePerGas=2000000000,
        maxPriorityFeePerGas=2000000000,
        gas=400000,
        to=Web3.toChecksumAddress(hex(toAddress)),
        value=0,
        data=signedBytes + bytes('=========='.encode('utf-8')) +encryptedDataBytes,
        type=2,  # (optional) the type is now implicitly set based on appropriate transaction params
        chainId=eval(chainID),
    ),
        privateKeyInBytes,
    )
    url = '{}/api?module=proxy&action=eth_sendRawTransaction&hex={}&apikey={}'\
        .format(explorer[chainID], rawHex['rawTransaction'].hex(), myToken[chainID])
    tx = requests.get(url).json()['result']
    return tx
