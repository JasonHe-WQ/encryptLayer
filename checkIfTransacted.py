import web3
from web3 import Web3

httpNodeDictionary = {'Ethereum': ['https://eth-mainnet.public.blastapi.io',
                                   'https://api.securerpc.com/v1',
                                   'https://rpc.ankr.com/eth',
                                   'https://eth-mainnet.gateway.pokt.network/v1/5f3453978e354ab992c4da79',
                                   'https://eth-mainnet-public.unifra.io'],
                      'BNB': [],
                      'Polygon': [],
                      'Avalanche-C': [],
                      'Arbitrum': [],
                      'Optimism': []}


def check(addr):
    ans = False
    isConnected = False
    hasValue = False
    while not hasValue:
        for key in httpNodeDictionary.keys():
            httpList = list(httpNodeDictionary[key])
            for i in range(len(httpList)):
                sigleHTTP = httpList[i]
                w3 = Web3(Web3.HTTPProvider(sigleHTTP))
                if w3.isConnected():
                    break
            hasValue = bool(Web3.eth.get_balance(addr))
            if hasValue:
                return True, key
        return False
