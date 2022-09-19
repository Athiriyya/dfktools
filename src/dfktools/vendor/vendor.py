from web3 import Web3

SERENDALE_CONTRACT_ADDRESS = "0x5BDa5c3258c72c4890E6c1EA16f4F9E394FF3fB4"
CRYSTALVALE_CONTRACT_ADDRESS = "0x0f85fdf6c561C42d6b46d0E27ea6Aa9Bf9476B3f"

ABI = '''
[
	{"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
	{"name": "ItemAdded", "type": "event", "inputs": [{"name": "item", "type": "address", "indexed": true, "internalType": "address"}, {"name": "startingPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
	{"name": "ItemTraded", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "boughtItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "boughtQty", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "soldItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "soldQty", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
	{"name": "ItemUpdated", "type": "event", "inputs": [{"name": "item", "type": "address", "indexed": true, "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "indexed": false, "internalType": "uint64"}, {"name": "status", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
	{"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
	{"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
	{"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
	{"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
	{"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
	{"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
	{"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
	{"name": "addTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_startingPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "_decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "_priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "addressToTradeItemId", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
	{"name": "buyItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}, {"name": "_maxPrice", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "getNextPrice", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
	{"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
	{"name": "getTradeItem", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem"}], "stateMutability": "view"},
	{"name": "getTradeItemByAddress", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem"}], "stateMutability": "view"},
	{"name": "getTradeItems", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem[]"}], "stateMutability": "view"},
	{"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
	{"name": "initialize", "type": "function", "inputs": [{"name": "_dfkGoldAddress", "type": "address", "internalType": "address"}, {"name": "_itemMinter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
	{"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "sellItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
	{"name": "togglePause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
	{"name": "tradeItems", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
	{"name": "updateTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "_decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "_priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "_status", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
'''


def block_explorer_link(txid):
	return 'https://explorer.harmony.one/tx/' + str(txid)


def buy_item(contract_address, item_address, quantity, maxPrice, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	tx = contract.functions.buyItem(item_address, quantity, maxPrice).buildTransaction(
		{'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

	logger.debug("Signing transaction")
	signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
	logger.debug("Sending transaction " + str(tx))
	ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	logger.debug("Transaction successfully sent !")
	logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
	tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
													 poll_latency=2)
	logger.info("Transaction mined !")

	return tx_receipt

def sell_item(contract_address, item_address, quantity, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

	w3 = Web3(Web3.HTTPProvider(rpc_address))
	account = w3.eth.account.privateKeyToAccount(private_key)
	w3.eth.default_account = account.address

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	tx = contract.functions.sellItem(item_address, quantity)
	
	if isinstance(gas_price_gwei, dict):  # dynamic fee
		tx = tx.buildTransaction(
			{'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
			 'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
	else:  # legacy
		tx = tx.buildTransaction(
			{'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})
			
	logger.debug("Signing transaction")
	signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
	logger.debug("Sending transaction " + str(tx))
	ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
	logger.debug("Transaction successfully sent !")
	logger.info("Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")
	tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
													 poll_latency=2)
	logger.info("Transaction mined !")

	return tx_receipt

def paused(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	result = contract.functions.paused().call()

	return result

def address_to_trade_item_id(contract_address, trade_item_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	return contract.functions.addressToTradeItemId(trade_item_address).call()

def get_trade_items(contract_address, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	raw = contract.functions.getTradeItems().call()
	trade_items = []
	for r in raw:
		trade_items.append({'id': r[0], 'tokenAddress': r[1], 'currentPrice': r[2], 'playerSellPrice': r[3]})

	return trade_items

def trade_items(contract_address, item_id, rpc_address):
	w3 = Web3(Web3.HTTPProvider(rpc_address))

	contract_address = Web3.toChecksumAddress(contract_address)
	contract = w3.eth.contract(contract_address, abi=ABI)

	raw = contract.functions.tradeItems(item_id).call()
	trade_items = {'id': raw[0], 'tokenAddress': raw[1], 'currentPrice': raw[2], 'playerSellPrice': raw[3]}

	return trade_items 