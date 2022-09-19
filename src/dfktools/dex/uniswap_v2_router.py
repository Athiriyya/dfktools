"""
https://docs.uniswap.org/protocol/V2/reference/smart-contracts/router-02
"""

from web3 import Web3


SERENDALE_CONTRACT_ADDRESS = '0x24ad62502d1C652Cc7684081169D04896aC20f30'
CRYSTALVALE_CONTRACT_ADDRESS = '0x3C351E1afdd1b1BC44e931E12D4E05D6125eaeCa'

ABI = """
    [
        {"name": "WETH", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "pure"},
        {"name": "addLiquidity", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "amountADesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountBDesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "addLiquidityETH", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "amountTokenDesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}], "stateMutability": "payable"},
        {"name": "factory", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "pure"},
        {"name": "getAmountIn", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "reserveIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveOut", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
        {"name": "getAmountOut", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveOut", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
        {"name": "getAmountsIn", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
        {"name": "getAmountsOut", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
        {"name": "quote", "type": "function", "inputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "reserveA", "type": "uint256", "internalType": "uint256"}, {"name": "reserveB", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
        {"name": "removeLiquidity", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "removeLiquidityETH", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "removeLiquidityETHSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "removeLiquidityETHWithPermit", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "removeLiquidityWithPermit", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
        {"name": "swapETHForExactTokens", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "payable"},
        {"name": "swapExactETHForTokens", "type": "function", "inputs": [{"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "payable"},
        {"name": "swapExactETHForTokensSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
        {"name": "swapExactTokensForETH", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
        {"name": "swapExactTokensForETHSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "swapExactTokensForTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
        {"name": "swapExactTokensForTokensSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
        {"name": "swapTokensForExactETH", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "amountInMax", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
        {"name": "swapTokensForExactTokens", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "amountInMax", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"}
    ]
    """


def block_explorer_link(txid):
    return 'https://explorer.harmony.one/tx/' + str(txid)


def weth(contract_address, rpc_address):
    '''
    Return the wrapped address of the native token of the blockchain
    :param rpc_address:
    :return:
    '''

    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.WETH().call()


def factory(contract_address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.factory().call()


def quote(contract_address, amount_a, reserve_a, reserve_b, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.quote(amount_a, reserve_a, reserve_b).call()


def get_amount_in(contract_address, amount_out, reserve_in, reserve_out, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getAmountIn(amount_out, reserve_in, reserve_out).call()


def get_amount_out(contract_address, amount_in, reserve_in, reserve_out, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getAmountOut(amount_in, reserve_in, reserve_out).call()


def swap_exact_tokens_for_tokens(contract_address, amount_in, amount_out_min, path, to, deadline, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    '''
    Swaps an exact amount of input tokens for as many output tokens as possible, along the route determined by the
    path. The first element of path is the input token, the last is the output token, and any intermediate elements
    represent intermediate pairs to trade through (if, for example, a direct pair does not exist).
    :param amount_in:
    :param amount_out_min:
    :param path:
    :param to:
    :param deadline:
    :param private_key:
    :param nonce:
    :param gas_price_gwei:
    :param tx_timeout_seconds:
    :param rpc_address:
    :param logger:
    :return:
    '''

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    tx = contract.functions.swapExactTokensForTokens(amount_in, amount_out_min, path, to, deadline)

    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:   # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def swap_exact_tokens_for_eth(contract_address, amount_in, amount_out_min, path, to, deadline, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    '''
    Swaps an exact amount of tokens for as much ETH as possible, along the route determined by the path.
    The first element of path is the input token, the last must be WETH, and any intermediate elements represent
     intermediate pairs to trade through (if, for example, a direct pair does not exist).
    :param amount_in:
    :param amount_out_min:
    :param path:
    :param to:
    :param deadline:
    :param private_key:
    :param nonce:
    :param gas_price_gwei:
    :param tx_timeout_seconds:
    :param rpc_address:
    :param logger:
    :return:
    '''
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.privateKeyToAccount(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.swapExactTokensForETH(amount_in, amount_out_min, path, to, deadline)
    
    if isinstance(gas_price_gwei, dict):   # dynamic fee
        tx = tx.buildTransaction(
            {'maxFeePerGas': w3.toWei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.toWei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:   # legacy
        tx = tx.buildTransaction({'gasPrice': w3.toWei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info(
        "Waiting for transaction " + block_explorer_link(signed_tx.hash.hex()) + " to be mined")

    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt