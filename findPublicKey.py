import requests
from eth_account import Account
import json



#
# explorer = {
#     '1': 'https://api.etherscan.io',
#     '56': 'https://api.bscscan.com/',
#     '43114': 'https://api.snowtrace.io',
#     '137': 'https://api.polygonscan.com',
#     '42161': 'https://api.arbiscan.io',
#     '10': 'https://api-optimistic.etherscan.io',
#     '1313161554': 'https://api.aurorascan.dev',
#     '1284': 'https://api-moonbeam.moonscan.io'
#
# }

# myToken = {
#     '1': 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9',
#     '56': '5QXV3MKW67M4S53WHFDFQ9DUUSSN8RW1GI',
#     '43114': 'H13WYPR9C7XV411NK9BGVP8C7KH7V4BPNZ',
#     '137': '2KTHMFT4CIZ9WDIQWQIK9ESD7I9T1VCG5Q',
#     '42161': '6XIWP1HZR51JEMWPW31CQTPMSVQRRPS26U',
#     '10': '7G41Q95JB979VKNDE6B7Z5APEWKK11Y644',
#     '1313161554': 'VK1X8E2VN3H7SBDFFZQV4WPSIMWAAF3J49',
#     '1284': 'BIV283PS7UZ87FHET11GH9N3PV13IVYBM5'
#
# }


def find(addr):
    # chainIDList = ['1', '56', '43114', '137', '42161', '10', '1313161554', '1284']
    tx = str()
    addr = hex(addr)
    url = 'https://api-moonbeam.moonscan.io/api?module=account' \
          '&action=txlist' \
          '&address={}' \
          '&startblock=1&endblock=99999999' \
          '&page=1&offset=1&sort=asc' \
          '&apikey=BIV283PS7UZ87FHET11GH9N3PV13IVYBM5'.format(addr)
    print(requests.get(url))
    print(url)
    tx = hex(0x507d269ad2022ffdb0dff875a5a4c78aaf98c13a25b3cc6028033731e000ddd3)
    url = 'https://moonbeam.api.subscan.io/api/scan/evm/transaction'
    dataHeader = {'Content-Type': 'application/json',
                  'X-API-Key': 'e41dbb7261e9468aa4cd0d1b9824eeea'}
    dataRaw = {"hash": "{}".format(tx)}
    output = requests.post(url, data=json.dumps(dataRaw), headers=dataHeader)
    print(output.json())
    outputDict = output.json()['data']
    txHash, r, s, v = (outputDict['hash']), (outputDict['r']), (outputDict['s']), outputDict['v']
    publicKey = Account.recoverHash(txHash, (v, r, s))
    print(publicKey)
    print(len(publicKey))

    # for chainID in chainIDList:
    #     url = '{}/api?module=account' \
    #           '&action=txlist' \
    #           '&address={}&startblock=0&' \
    #           'endblock=99999999' \
    #           '&page=1' \
    #           '&offset=1' \
    #           '&sort=desc&apikey={}'.format(explorer[chainID], str(addr), myToken[chainID])
    #     print(url)
    #     print(requests.get(url))
    #     try:
    #         data = requests.get(url).json()
    #         tx = data['result'][0]['hash']
    #     except Exception as e:
    #         if type(e) == IndexError and chainID == chainIDList[-1]:
    #             print('No TX yet, please change another address')
    #         elif type(e) == IndexError:
    #             pass
    #         else:
    #             print('Please make sure you are online, you are disconnected from {}'.format(chainID))
    #     if tx == 0 and chainID == chainIDList[-1]:
    #         return 0
    #     elif tx == 0:
    #         continue
    #     else:
    #         publicKey = Account.recover_message(tx)
    #         return publicKey

print(find(0x5568BC7EebC605A88e247769c4acA92d95BC9360))
