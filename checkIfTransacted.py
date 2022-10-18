import web3
from web3 import Web3

httpNodeDictionary = {'Ethereum': ['https://eth-mainnet.public.blastapi.io',
                                   'https://api.securerpc.com/v1',
                                   'https://rpc.ankr.com/eth',
                                   'https://eth-rpc.gateway.pokt.network',
                                   'https://eth-mainnet-public.unifra.io'],
                      'BNB': ['https://bsc-dataseed3.defibit.io',
                              'https://bsc-dataseed2.defibit.io',
                              'https://bsc-dataseed1.defibit.io',
                              'https://bsc-dataseed1.ninicoin.io',
                              'https://bsc.mytokenpocket.vip'],
                      'Avalanche-C': ['https://rpc.ankr.com/avalanche',
                                      'https://1rpc.io/avax/c',
                                      'https://api.avax.network/ext/bc/C/rpc',
                                      'https://avaIancheapi.terminet.io/ext/bc/C/rpc'],
                      'Polygon': ['https://polygon-bor.publicnod.com',
                                  'https://polygon-mainnet-public.unifra.io',
                                  'https://rpc.ank.com/polygon',
                                  'https://polygon-mainnet.public.blastapi.io',
                                  'https://polygon-rp.com'],
                      'Arbitrum': ['https://1rpc.io/arb',
                                   'https://arb1.arbitrum.io/rpc',
                                   'https://rpc.ankr.com/arbitrum'],
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
            # if hasValue:
            #     return True, key
        return False
