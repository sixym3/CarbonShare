# Python program to call the
# smart contract
import json
from web3 import Web3, HTTPProvider
from config import DB_NAME, CONNECTION_URL, PROJECT_ID, MNEMONICS

# truffle development blockchain address
blockchain_address = f"https://sepolia.infura.io/v3/{PROJECT_ID}"

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.account.enable_unaudited_hdwallet_features()
account = web3.eth.account.from_mnemonic(MNEMONICS)
web3.eth.defaultAccount = account.address

# Setting the default account (so we don't need
#to set the "from" for every transaction call)

# Path to the compiled contract JSON file
compiled_contract_path = 'build/contracts/MyToken.json'
deployed_contract_address = "0x6398d65465cb378CAc7cB2922C4F48c1f8dF421F"

# load contract info as JSON
with open(compiled_contract_path) as file:
	contract_json = json.load(file)
	
	# fetch contract's abi - necessary to call its functions
	contract_abi = contract_json['abi']

# Fetching deployed contract reference
contract = web3.eth.contract(address = deployed_contract_address, abi = contract_abi)

# Calling contract function (this is not persisted
# to the blockchain)
# output = contract.functions.rewardTokens("0xD54C89E0f36832E65c9ad7B98F5cf186661101B1", 100).transact()
# output = contract.functions.balanceOf("0x6524E8E57a921aA11c37791d67462363194c74eB").call()



def rewardTokenToDepricated(to_account):
    # from_account = '0xeF8692168D0C165488ae3F0105Fe096f5E81820b'
    # to_account = '0x37d1215743ACf59B85f2DDE7Ab103f2BBC5a568F'
    # web3 = Web3(Web3.HTTPProvider(infura_url))
    nonce = web3.eth.getTransactionCount(account.address)
    tx = {
		'type': '0x2',
		'nonce': nonce,
		'from': account.address,
		'to': to_account,
		'value': web3.toWei(0.01, 'ether'),
		'maxFeePerGas': web3.toWei('250', 'gwei'),
		'maxPriorityFeePerGas': web3.toWei('3', 'gwei'),
		'chainId': 11155111
	}
    gas = web3.eth.estimateGas(tx)
    tx['gas'] = gas
    signed_tx = web3.eth.account.sign_transaction(tx, account.privateKey)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction hash: " + str(web3.toHex(tx_hash)))
    
def rewardTokenTo(from_address, to_address, amount, contract):
	tx = contract.functions.rewardTokens(to_address, amount).buildTransaction({
	    'from': from_address,
	    'nonce': web3.eth.getTransactionCount(from_address),
	    'maxFeePerGas': web3.toWei('250', 'gwei'),
	    'maxPriorityFeePerGas': web3.toWei('3', 'gwei'),
	    'value': 0,
	    'chainId': 11155111
	})
	gas = web3.eth.estimateGas(tx)
	tx['gas'] = gas
	signed_tx = web3.eth.account.signTransaction(tx, account.privateKey)
	tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
	if tx_receipt['status'] == 1:
		print('Tokens transferred successfully! Hash: {}'.format(str(web3.toHex(tx_hash))))
	else:
		print('There was an error transferring the tokens')

rewardTokenTo(account.address, "0x23404C63f6cB5dE59E8b528338658852D6A8E87F", 100, contract)