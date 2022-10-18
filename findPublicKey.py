import requests


def find(chainID, addr):
    addr = hex(addr)
    url = 'https://www.covalenthq.com/docs/api/#get-/v1/{0}/address/{1}/transfers_v2/'.format(chainID, str(addr))
    return url

print(find(1,0x5568BC7EebC605A88e247769c4acA92d95BC9360))