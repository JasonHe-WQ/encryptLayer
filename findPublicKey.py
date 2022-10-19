import requests
from eth_account import Account
import json
from eth_keys import KeyAPI

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
    # url = 'https://api-moonbeam.moonscan.io/api?module=account' \
    #       '&action=txlist' \
    #       '&address={}' \
    #       '&startblock=1&endblock=99999999' \
    #       '&page=1&offset=1&sort=asc' \
    #       '&apikey=HXWZFA4VR4TKN4BV2GDXPY4NUAQ35SVP7T'.format(addr)
    dataHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    # data = requests.get(url, headers=dataHeader).json()
    # print(data)
    # tx = data['result'][0]['hash']
    # url = 'https://moonbeam.api.subscan.io/api/scan/evm/transaction'
    # dataHeader = {'Content-Type': 'application/json',
    #               'X-API-Key': '5e94a2958fe04ae19a1c1554815a9f4f'}
    # dataRaw = {"hash": "{}".format(tx)}
    # output = requests.post(url, data=json.dumps(dataRaw), headers=dataHeader)
    # try:
    #     outputDict = output.json()['data']
    # except Exception:
    #     print('No TX yet, please use another address')
    #     return False
    # txHash, r, s, v = (outputDict['hash']), (outputDict['r']), (outputDict['s']), outputDict['v']
    # publicKey = Account.recoverHash(txHash, (v, r, s))
    # print(publicKey)
    # publicKey = bin(eval(publicKey))
    # print(publicKey[2:])
    # print(len(publicKey))
    # return publicKey

    for chainID in chainIDList:
        url = '{}/api?module=account' \
              '&action=txlist' \
              '&address={}&startblock=0&' \
              'endblock=99999999' \
              '&page=1' \
              '&offset=1' \
              '&sort=desc&apikey={}'.format(explorer[chainID], str(addr), myToken[chainID])
        try:
            data = requests.get(url, headers=dataHeader).json()
            tx = data['result'][0]['hash']
        except Exception as e:
            if type(e) == IndexError and chainID == chainIDList[-1]:
                print('No TX yet, please change another address')
            elif type(e) == IndexError:
                pass
            else:
                print('Please make sure you are online, you are disconnected from {}'.format(chainID))
        if tx == str(0) and chainID == chainIDList[-1]:
            return 0
        elif tx == str(0):
            continue
        else:
            url = '{}/' \
                  'api?module=proxy&action=eth_getTransactionByHash' \
                  '&txhash={}' \
                  '&apikey={}'.format(explorer[chainID], tx, myToken[chainID])
            data = requests.get(url, headers=dataHeader).json()
            v, r, s = data['result']['v'], data['result']['r'], data['result']['s']
            publicKey = Account.recoverHash(tx, (v, r, s))
            print(publicKey)
            publicKey.lower()
            publicKey = bytes.fromhex(publicKey[2:])
            print(KeyAPI.PublicKey.from_compressed_bytes(publicKey))
            return publicKey

# print(find('0x5568BC7EebC605A88e247769c4acA92d95BC9360'))
