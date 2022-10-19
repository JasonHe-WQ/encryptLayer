import requests
from eth_account import Account
import json
from eth_keys import KeyAPI


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
#     '1': '',
#     '56': '',
#     '43114': '',
#     '137': '',
#     '42161': '',
#     '10': '',
#     '1313161554': '',
#     '1284': ''
#
# }


def find(addr):
    # chainIDList = ['1', '56', '43114', '137', '42161', '10', '1313161554', '1284']
    url = 'https://api-moonbeam.moonscan.io/api?module=account' \
          '&action=txlist' \
          '&address={}' \
          '&startblock=1&endblock=99999999' \
          '&page=1&offset=1&sort=asc' \
          '&apikey=HXWZFA4VR4TKN4BV2GDXPY4NUAQ35SVP7T'.format(addr)
    dataHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    data = requests.get(url, headers=dataHeader).json()
    print(data)
    tx = data['result'][0]['hash']
    url = 'https://moonbeam.api.subscan.io/api/scan/evm/transaction'
    dataHeader = {'Content-Type': 'application/json',
                  'X-API-Key': '5e94a2958fe04ae19a1c1554815a9f4f'}
    dataRaw = {"hash": "{}".format(tx)}
    output = requests.post(url, data=json.dumps(dataRaw), headers=dataHeader)
    try:
        outputDict = output.json()['data']
    except Exception:
        print('No TX yet, please use another address')
        return False
    txHash, r, s, v = (outputDict['hash']), (outputDict['r']), (outputDict['s']), outputDict['v']
    publicKey = Account.recoverHash(txHash, (v, r, s))
    # publicKey = bin(eval(publicKey))
    print(publicKey)
    publicKey = bytes(publicKey, 'utf-8')
    print(len(publicKey))
    return publicKey

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


print(find('0x5568BC7EebC605A88e247769c4acA92d95BC9360'))
