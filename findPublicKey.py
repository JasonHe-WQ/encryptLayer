import requests
import json


def find(chainID, addr):
    addr = hex(addr)
    myToken = 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9'
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address={}&startblock=0&' \
          'endblock=99999999&page=1&offset=1&sort=asc&apikey={}'.format(str(addr),myToken)
    data = requests.get(url).json()
    print(data)
    # with open('get.json', 'w') as f:
    #     f.write(data)
    return url


print(find(1, 0x5568BC7EebC605A88e247769c4acA92d95BC9360))
