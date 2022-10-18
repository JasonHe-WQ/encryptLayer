import web3
from web3 import Web3

httpNodeDictionary = {
                      'Ethereum': ['https://eth-mainnet.public.blastapi.io',
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
                                      'https://api.avax.network/ext/bc/C/rpc'],
                      'Polygon': ['https://poly-rpc.gateway.pokt.network',
                                  'https://1rpc.io/matic',
                                  'https://polygonapi.terminet.io/rpc',
                                  'https://rpc-mainnet.matic.quiknode.pro',
                                  'https://polygon-mainnet-public.unifra.io'],
                      'Arbitrum': ['https://1rpc.io/arb',
                                   'https://arb1.arbitrum.io/rpc',
                                   'https://rpc.ankr.com/arbitrum'],
                      'Optimism': ['https://1rpc.io/op',
                                   'https://mainnet.optimism.io',
                                   'https://rpc.ankr.com/optimism']}


def check(addr):
    isConnected = False
    hasValue = False
    w3 = object()
    sigleHTTP = str()
    addr = str(hex(addr))
    checksum_address = Web3.toChecksumAddress(addr)
    print(addr)
    while not hasValue:
        for key in httpNodeDictionary.keys():
            httpList = list(httpNodeDictionary[key])
            for i in range(len(httpList)):
                sigleHTTP = httpList[i]
                w3 = Web3(Web3.HTTPProvider(sigleHTTP))
                isConnected = w3.isConnected()
                if isConnected:
                    break
            hasValue = bool(w3.eth.get_balance(checksum_address))
            print(key,sigleHTTP,hasValue)
            if hasValue:
                return True, key
        return False, None