import requests

explorer = {
    '1': 'https://api.etherscan.io',
    '56':'https://bscscan.com',
    '43114':'https://snowtrace.io',
    '137':'https://polygonscan.com',
    '42161':'https://arbiscan.io'

}


def find(chainID, addr):
    addr = hex(addr)
    myToken = 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9'
    url = '{}/api?module=account&action=txlist&address={}&startblock=0&' \
          'endblock=99999999&page=1&offset=1&sort=asc&apikey={}'.format(explorer[chainID],str(addr), myToken)
    data = requests.get(url).json()
    tx = data['result'][0]['hash']
    print(tx)
    # with open('get.json', 'w') as f:
    #     f.write(data)
    return url


print(find('1', 0x5568BC7EebC605A88e247769c4acA92d95BC9360))
