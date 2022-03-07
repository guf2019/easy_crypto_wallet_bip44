from operations.web3_driver import web3Driver
from config.exceptions import *

def get_blockNumber():
    return web3Driver.web3.eth.blockNumber