from web3 import Web3
from config.constants import NodeRPC
from config.exceptions import Web3ConnectException

class Web3Driver:
    def __init__(self, net):
        self.web3 = Web3(Web3.HTTPProvider(net))
        if not self.web3.isConnected():
            raise Web3ConnectException(net)

web3Driver = Web3Driver(NodeRPC.ETHEREUM_MAINNET)