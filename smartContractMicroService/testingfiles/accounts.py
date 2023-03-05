from web3 import Web3, EthereumTesterProvider
from config import PRIVATE_KEY, TESTNET_RPC
from eth_account.messages import encode_defunct

# web3 = Web3(Web3.HTTPProvider(TESTNET_RPC))

w3 = Web3(EthereumTesterProvider)
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account
acct = Account.create(PRIVATE_KEY)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct))
w3.eth.default_account = acct.address

# msg = 'hello world'
# message = encode_defunct(text=msg)
# signed_message = web3.eth.account.sign_message(message, private_key=PRIVATE_KEY)

# print(signed_message)

# def to_32byte_hex(val):
#    return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

# ec_recover_args = (msghash, v, r, s) = (
#   Web3.toHex(signed_message.messageHash),
#   signed_message.v,
#   to_32byte_hex(signed_message.r),
#   to_32byte_hex(signed_message.s),
# )

# print(signed_message)
# print('-' * 50)
# print(ec_recover_args)
# print('-' * 50)
# print(web3.eth.account.recover_message(message, signature=signed_message.signature))
# account = web3.eth.account.from_key(PRIVATE_KEY)
# print(account.address)

# to_address = '0x6524E8E57a921aA11c37791d67462363194c74eB'
# value = 0
# gas = 21000
# gas_price = web3.toWei('1', 'gwei')
# nonce = web3.eth.getTransactionCount(account.address)

# transaction = {
#     'to': to_address,
#     'value': value,
#     'gas': gas,
#     'maxFeePerGas': gas_price,
#     'maxPriorityFeePerGas': 0,
#     'nonce': nonce,
#     'chainId': 1,
#     'type': '0x2', 
#     'accessList': ( 
#         {
#             'address': '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae',
#             'storageKeys': (
#                 '0x0000000000000000000000000000000000000000000000000000000000000003',
#                 '0x0000000000000000000000000000000000000000000000000000000000000007',
#             )
#         },
#         {
#             'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
#             'storageKeys': ()
#         },
#     )
# }

transaction = {
    'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
    'value': 1000000000,
    'gas': 2000000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
    'nonce': 0,
    'chainId': 1,
    'type': '0x2',  # the type is optional and, if omitted, will be interpreted based on the provided transaction parameters
    'accessList': (  # accessList is optional for dynamic fee transactions
        {
            'address': '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae',
            'storageKeys': (
                '0x0000000000000000000000000000000000000000000000000000000000000003',
                '0x0000000000000000000000000000000000000000000000000000000000000007',
            )
        },
        {
            'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
            'storageKeys': ()
        },
    )
}

receiving_account_address = acct.address

dynamic_fee_transaction = {
    'type': '0x2',  # optional - defaults to '0x2' when dynamic fee transaction params are present
    'from': acct.address,  # optional if w3.eth.default_account was set with acct.address
    'to': receiving_account_address,
    'value': 22,
    'maxFeePerGas': 2000000000,  # required for dynamic fee transactions
    'maxPriorityFeePerGas': 1000000000,  # required for dynamic fee transactions
}
w3.eth.send_transaction(dynamic_fee_transaction)
# key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
# signed = web3.eth.account.sign_transaction(transaction, key)

# tx_hash = web3.eth.send_raw_transaction(signed.rawTransaction)

# print(f'Transaction sent: {tx_hash.hex()}')
# signed = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

# print(web3.eth.send_raw_transaction(signed.rawTransaction))