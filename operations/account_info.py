from operations.web3_driver import web3Driver

def get_eth_balance(account_address):
    address = web3Driver.web3.toChecksumAddress(account_address)
    balance = web3Driver.web3.eth.getBalance(address)
    return web3Driver.web3.fromWei(balance, "ether")
