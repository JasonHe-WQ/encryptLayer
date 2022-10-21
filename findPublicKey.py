import requests
from eth_keys import KeyAPI
explorer = {'1': 'https://api.etherscan.io'}
myToken = {'1': 'VYDCJ3TMWJKTS1FRXVHEWQRSZE6D8HRWI9'}
from eth_utils import to_checksum_address
from eth_account import Account
from eth_account._utils.legacy_transactions import serializable_unsigned_transaction_from_dict
from hexbytes import HexBytes
from eth_utils.curried import (
    combomethod,
    hexstr_if_str,
    is_dict,
    keccak,
    text_if_str,
    to_bytes,
    to_int,
)

def find(addr):
    chainID = '1'
    dataHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
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
        if type(e) == IndexError:
            print('No TX yet, please change another address')
            return
        else:
            print('Please make sure you are online, you are disconnected from {}'.format(chainID))
            return
    else:
        url = '{}/' \
              'api?module=proxy&action=eth_getTransactionByHash' \
              '&txhash={}' \
              '&apikey={}'.format(explorer[chainID], tx, myToken[chainID])
        data = requests.get(url, headers=dataHeader).json()
        v, r, s = data['result']['v'], data['result']['r'], data['result']['s']
        v, r, s = eval(v), eval(r), eval(s)
        legacy_transaction = data['result']
        gasPrice = data['result']['gasPrice']
        legacy_transaction.update({'data': data['result']['input'], 'to': to_checksum_address(data['result']['to'])})
        keys = ['from', 'blockHash', 'blockNumber', 'hash', 'input', 'transactionIndex', 'gasPrice', 'v', 'r', 's']
        for key in keys:
            del legacy_transaction[key]
        try:
            unsigned_transaction = serializable_unsigned_transaction_from_dict(legacy_transaction)
            transaction_hash = unsigned_transaction.hash()
            tx = transaction_hash.hex()
        except Exception as e:
            print(e)
            del legacy_transaction['type']
            legacy_transaction.update({"gasPrice": gasPrice, 'chainId': int(chainID)})
            unsigned_transaction = serializable_unsigned_transaction_from_dict(legacy_transaction)
            transaction_hash = unsigned_transaction.hash()
            tx = transaction_hash.hex()

        hash_bytes = HexBytes(tx)
        v, r, s = map(hexstr_if_str(to_int), (v, r, s))

        v = 0
        vaddr = Account.recoverHash(tx, (v, r, s))
        print(vaddr)
        if vaddr == addr:
            signature_obj = KeyAPI.Signature(vrs=(v, r, s))
            pubkey = signature_obj.recover_public_key_from_msg_hash(hash_bytes)
        else:
            v = 1
            vaddr = Account.recoverHash(tx, (v, r, s))
            signature_obj = KeyAPI.Signature(vrs=(v, r, s))
            pubkey = signature_obj.recover_public_key_from_msg_hash(hash_bytes)

        publicKey = str(pubkey)
        return publicKey

# publicKey=find("0x5568BC7EebC605A88e247769c4acA92d95BC9360")
# print(publicKey)