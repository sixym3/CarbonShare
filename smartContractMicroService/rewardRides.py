import time
from pymongo import MongoClient
import json
from web3 import Web3, HTTPProvider
from config import DB_NAME, CONNECTION_URL, PROJECT_ID, MNEMONICS

# Connect to MongoDB
client = MongoClient(CONNECTION_URL)

# Connect to blockchain
blockchain_address = f"https://sepolia.infura.io/v3/{PROJECT_ID}"

# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.account.enable_unaudited_hdwallet_features()
account = web3.eth.account.from_mnemonic(MNEMONICS)
web3.eth.defaultAccount = account.address

# Load contract files
compiled_contract_path = 'build/contracts/MyToken.json'
deployed_contract_address = "0x6398d65465cb378CAc7cB2922C4F48c1f8dF421F"
with open(compiled_contract_path) as file:
	contract_json = json.load(file)
	contract_abi = contract_json['abi']
 
# Initialize contract
contract = web3.eth.contract(address = deployed_contract_address, abi = contract_abi)

# Function to reward token 
def rewardTokenTo(from_address, to_address, amount, contract):
    try:
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
        return tx_receipt['status'] == 1
    except ValueError as e:
        return rewardTokenTo(from_address, to_address, amount, contract)

# rewardTokenTo(account.address, "0x23404C63f6cB5dE59E8b528338658852D6A8E87F", 100, contract)

# Microservice to check for unrewarded rides
def service():
    time.sleep(1)
    print("Checking for unrewarded rides...")
    
    # Reload data from database
    db = client[DB_NAME]
    rides_collection = db['rides']
    
    # Reward rides
    for ride in rides_collection.find({'rewarded': False}):
        print("Rewarding: ", ride['_id'])
        particpants = []
        particpants.append(ride['driver'])
        tokens_to_reward = int(ride['distance'])
        reward_status = True
        for rider in ride['riders']:
            particpants.append(rider)
        for rideraccount in particpants:
            address = rideraccount['publicKey']
            reward_status = rewardTokenTo(account.address, address, tokens_to_reward, contract) and reward_status
                
        # Update rewarded field in MongoDB
        if reward_status:
            rides_collection.update_one({'rideId': ride['rideId']}, {'$set': {'rewarded': True}})
            print("Success")
            print("-" * 50)

if __name__ == '__main__':
    while True:
        service()