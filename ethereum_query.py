from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
#     This line will mess with our autograders, but might be useful when debugging
    # print( "Connected to Ethereum node" )
# else:
#     print( "Failed to connect to Ethereum node!" )

def get_transaction(tx):
    txObj = w3.eth.getTransaction(tx)   #YOUR CODE HERE
    # print(type(tx))
    return txObj

# # Return the gas price used by a particular transaction,
# #   tx is the transaction
def get_gas_price(tx):
    txObj = w3.eth.getTransaction(tx)
    gas_price = txObj['gasPrice']
    # gas_price = tx['gasPrice']
    return gas_price

def get_gas(tx):
    # txObj = w3.eth.getTransaction(tx)
    txObj = w3.eth.get_transaction_receipt(tx)
    # gas = tx['gas']
    gas = txObj['gasUsed']
    return gas

def get_transaction_cost(tx):
    # tx_cost = get_gas(tx) * get_gas_price(tx) / 1000000000000000000
    tx_cost = get_gas(tx) * get_gas_price(tx)
    return tx_cost

def get_block_cost(block_num):
    block = w3.eth.get_block(block_num)
    transactions = block['transactions']
    block_cost = 0
    for tx in transactions:
        cost = get_transaction_cost(tx)
        block_cost = block_cost + cost
   
    return block_cost

# # Return the hash of the most expensive transaction
def get_most_expensive_transaction(block_num):
    block = w3.eth.get_block(block_num)
    transactions = block['transactions']
    mostExpensive = 0
    max_tx = None
    for tx in transactions:
        cost = get_transaction_cost(tx)
        if cost > mostExpensive:
            max_tx = tx['hash']

    max_tx = HexBytes(max_tx)
    return max_tx


# print(get_block_cost(2000000))
# txCost = get_transaction_cost('0x0dda1142828634746a8e49e707fddebd487355a172bfa94b906a151062299578')
# print(txCost)
# print('\n')
# print('cost in USD: ')
# print(txCost * 1385.02)


