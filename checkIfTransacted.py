from web3 import Web3

httpNodeDictionary = {
                      '1': ['https://eth-mainnet.public.blastapi.io',
                                   'https://rpc.ankr.com/eth',
                                   'https://eth-rpc.gateway.pokt.network',
                                   'https://eth-mainnet-public.unifra.io'],
                      '56': ['https://bsc-dataseed3.defibit.io',
                              'https://bsc-dataseed2.defibit.io',
                              'https://bsc-dataseed1.defibit.io',
                              'https://bsc-dataseed1.ninicoin.io',
                              'https://bsc.mytokenpocket.vip'],
                      '43114': ['https://rpc.ankr.com/avalanche',
                                      'https://1rpc.io/avax/c',
                                      'https://api.avax.network/ext/bc/C/rpc'],
                      '137': ['https://poly-rpc.gateway.pokt.network',
                                  'https://1rpc.io/matic',
                                  'https://polygonapi.terminet.io/rpc',
                                  'https://rpc-mainnet.matic.quiknode.pro',
                                  'https://polygon-mainnet-public.unifra.io'],
                      '42161': ['https://1rpc.io/arb',
                                   'https://arb1.arbitrum.io/rpc',
                                   'https://rpc.ankr.com/arbitrum']}


def check(addr):
    isConnected = False
    hasValue = False
    w3 = object()
    singleHTTP = str()
    addr = str(hex(addr))
    checksum_address = Web3.toChecksumAddress(addr)
    print(addr)
    while not hasValue:
        for key in httpNodeDictionary.keys():
            httpList = list(httpNodeDictionary[key])
            for i in range(len(httpList)):
                singleHTTP = httpList[i]
                w3 = Web3(Web3.HTTPProvider(singleHTTP))
                isConnected = w3.isConnected()
                if isConnected:
                    break
            hasValue = bool(w3.eth.get_balance(checksum_address))
            print(key,singleHTTP,hasValue)
            if hasValue:
                return True, key
        return False, None
check(0x5568BC7EebC605A88e247769c4acA92d95BC9360)