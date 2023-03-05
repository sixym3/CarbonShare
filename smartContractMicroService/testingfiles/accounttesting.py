from web3 import Web3
from config import PRIVATE_KEY, TESTNET_RPC

web3 = Web3(Web3.HTTPProvider(TESTNET_RPC))
account_1 = '0xD54C89E0f36832E65c9ad7B98F5cf186661101B1'
private_key1 = PRIVATE_KEY
account_2 = '0x6524E8E57a921aA11c37791d67462363194c74eB'

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))