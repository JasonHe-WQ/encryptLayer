import requests

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


def find(addr):
    chainIDList = ['1', '56', '43114', '137', '42161', '10', '1313161554', '1284']
    tx = int()
    addr = hex(addr)
    for chainID in chainIDList:
        url = '{}/api?module=account' \
              '&action=txlist' \
              '&address={}&startblock=0&' \
              'endblock=99999999' \
              '&page=1' \
              '&offset=1' \
              '&sort=desc&apikey={}'.format(explorer[chainID], str(addr), myToken[chainID])
        print(url)
        print(requests.get(url))
        try:
            data = requests.get(url).json()
            print(data)
            tx = data['result'][0]['hash']
        except IndexError:
            print('No TX yet, please change the address or provide the public key')
            return 0
    return tx


print(find(0x5568BC7EebC605A88e247769c4acA92d95BC9360))
