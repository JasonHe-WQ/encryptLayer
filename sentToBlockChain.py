
from web3 import Web3
explorer = {
    '1': 'https://api.etherscan.io',
    '56': 'https://api.bscscan.com/',
    '43114': 'https://api.snowtrace.io',
    '137': 'https://api.polygonscan.com',
    '42161': 'https://api.arbiscan.io',
    '10': 'https://api-optimistic.etherscan.io',
    '1313161554': 'https://api.aurorascan.dev',
    '1284': 'https://api-moonbeam.moonscan.io'

}
myToken = {
    '1': 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9',
    '56': '5QXV3MKW67M4S53WHFDFQ9DUUSSN8RW1GI',
    '43114': 'H13WYPR9C7XV411NK9BGVP8C7KH7V4BPNZ',
    '137': '2KTHMFT4CIZ9WDIQWQIK9ESD7I9T1VCG5Q',
    '42161': '6XIWP1HZR51JEMWPW31CQTPMSVQRRPS26U',
    '10': '7G41Q95JB979VKNDE6B7Z5APEWKK11Y644',
    '1313161554': 'VK1X8E2VN3H7SBDFFZQV4WPSIMWAAF3J49',
    '1284': 'BIV283PS7UZ87FHET11GH9N3PV13IVYBM5'

}
dataHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

def send(chainID, yourAddress, toAddress, privateKeyInBytes):
    chainIDList = ['1', '137', '56', '43114', '10', '42161', '1284']
    for i in chainIDList:
        APIList = {
            '1': 'https://rpc.ankr.com/eth',
            '137': 'https://polygon-rpc.com',
            '56': 'https://polygon-rpc.com',
            '43114': 'https://1rpc.io/avax/c',
            '10': 'https://mainnet.optimism.io',
            '42161': 'https://1rpc.io/arb',
            '1284': 'https://moonbeam.public.blastapi.io'
        }
        with open('encryptedData.bin', 'rb') as f:
            encryptedDataBytes = f.read()
        w3 = Web3(Web3.HTTPProvider(APIList[i]))
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

