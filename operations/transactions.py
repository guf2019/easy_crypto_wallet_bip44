from operations.web3_driver import web3Driver

def transferETH(from_address, to_address, value, gasPriceInGwei, private_key):
    from_address = web3Driver.web3.toChecksumAddress(from_address)
    to_address = web3Driver.web3.toChecksumAddress(to_address)
    nonce = web3Driver.web3.eth.getTransactionCount(from_address)
    gasPrice = web3Driver.web3.toWei(str(gasPriceInGwei), 'gwei')
    value = web3Driver.web3.toWei(value, 'ether')

    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': value,
        'gas': 21000,
        'gasPrice': gasPrice
    }

    # sign the transaction
    signed_tx = web3Driver.web3.eth.account.sign_transaction(tx, private_key)

    # send transaction
    tx_hash = web3Driver.web3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return str(web3Driver.web3.toHex(tx_hash))
