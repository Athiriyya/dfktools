from web3 import Web3

ITEMS = [

	("0x909EF175d58d0e17d3Ceb005EeCF24C1E5C6F390", "DFKETRNLSTY", "Pages of the Eternal Story")

 ]

ABI = """
[
    {"name": "ApprovalForAll", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "operator", "type": "address", "internalType": "address", "indexed": true}, {"name": "approved", "type": "bool", "internalType": "bool", "indexed": false}], "anonymous": false},
    {"name": "TransferBatch", "type": "event", "inputs": [{"name": "operator", "type": "address", "internalType": "address", "indexed": true}, {"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "ids", "type": "uint256[]", "internalType": "uint256[]", "indexed": false}, {"name": "values", "type": "uint256[]", "internalType": "uint256[]", "indexed": false}], "anonymous": false},
    {"name": "TransferSingle", "type": "event", "inputs": [{"name": "operator", "type": "address", "internalType": "address", "indexed": true}, {"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "id", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "value", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "URI", "type": "event", "inputs": [{"name": "value", "type": "string", "internalType": "string", "indexed": false}, {"name": "id", "type": "uint256", "internalType": "uint256", "indexed": true}], "anonymous": false},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}, {"name": "id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "balanceOfBatch", "type": "function", "inputs": [{"name": "accounts", "type": "address[]", "internalType": "address[]"}, {"name": "ids", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "isApprovedForAll", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}, {"name": "operator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "safeBatchTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "ids", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}, {"name": "data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setApprovalForAll", "type": "function", "inputs": [{"name": "operator", "type": "address", "internalType": "address"}, {"name": "approved", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "uri", "type": "function", "inputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"}
]
        """

'''
def symbol2item(symbol):
    symbol = symbol.upper().strip()
    for item in ITEMS:
        if item[1] == symbol:
            return item
    return None


def symbol2address(symbol):
    symbol = symbol.upper().strip()
    for item in ITEMS:
        if item[1] == symbol:
            return item[0]
    return None
'''


def address2item(address):
    address = address.upper().strip()
    for item in ITEMS:
        if item[0].upper() == address:
            return item
    return None


def address2symbol(address):
    address = address.upper().strip()
    for item in ITEMS:
        if item[0].upper() == address:
            return item[1]
    return None


def all_items():
    return ITEMS.copy()


def balance_of(token_address, account_address, id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.balanceOf(account_address, id).call()

    return result


def uri(token_address, id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    contract_address = Web3.toChecksumAddress(token_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    result = contract.functions.uri(id).call()

    return result
