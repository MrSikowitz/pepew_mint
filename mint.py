from web3 import Web3
from eth_account import Account
import config
import json

rpc_url = "https://rpc.ankr.com/polygon_mumbai"

web3 = Web3(Web3.HTTPProvider(rpc_url))
print(web3.is_connected())

private_key = config.Private_Key
wallet_address = Account.from_key(private_key).address
address = ''

abi = json.loads('[{"type": "function","name": "mint","inputs": []}]')

nonce = web3.eth.get_transaction_count(wallet_address)
contract = web3.eth.contract(address, abi=abi)

tx = contract.functions.mint().build_transaction({
    "value": web3.to_wei(0.1, 'ether'),
    "from": wallet_address,
    "gas": 4000000,
    "gasPrice": web3.eth.gas_price,
    "nonce": nonce,
    "chainId": 80001
})

signed_txn = web3.eth.account.sign_transaction(tx, private_key)

tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(web3.to_hex(tx_hash))