import web3
import json
from abi import abi
import time
import os
from dotenv import load_dotenv

load_dotenv()
provider = os.getenv('PROVIDER')
w3 = web3.Web3(web3.HTTPProvider(provider))
print(w3.clientVersion)
print ("Latest Ethereum block number" , w3.eth.blockNumber)
abi = abi
contract_address = w3.toChecksumAddress('0xDE3278e65D8cdB66A70e8E5B89a31445e98dfc6d')
counter = w3.eth.contract(address=contract_address, abi=abi)
private_key = os.getenv('PRIVATE_KEY')
me = w3.eth.account.privateKeyToAccount(private_key)
print(me.address)


def add_contact(name, email, contactAddress):
    nonce = w3.eth.getTransactionCount(me.address)
    user_addr = w3.toChecksumAddress(contactAddress)
    txn = counter.functions.addContact(contactAddress=user_addr,
                    name=name, email=email).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )
    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(tx_receipt)
    print(w3.toHex(tx_receipt['transactionHash']))

    return tx_receipt['status']

def create_group(name, description, member_addresses):

    current_ts = int(time.time())
    nonce = w3.eth.getTransactionCount(me.address)
    formatted_addresses = []
    for addr in member_addresses:
        formatted_addresses.append(w3.toChecksumAddress(addr))
    txn = counter.functions.createGroup(name=name, description=description,
                        createdAtTimestamp=current_ts,
                        memberAddresses=formatted_addresses).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )
    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

    # print(tx_receipt['status'])
    # print(w3.toHex(tx_receipt['transactionHash']))
    # print(tx_receipt['logs'][0]['topics'][1])
    # print(tx_receipt)
    return w3.toHex(tx_receipt['logs'][0]['topics'][1]), current_ts, tx_receipt['status'], me.address
# print(counter)
def add_group_membership(group_id, member_address):

    nonce = w3.eth.getTransactionCount(me.address)
    group_id_bytes = w3.toBytes(hexstr=group_id)
    # group_id_bytes = group_id.encode('utf-8')
    # print(type(group_id_bytes))
    # print(group_id_bytes)
    # print(type(member_address))
    txn = counter.functions.addGroupMembership(group_id_bytes,
                        member_address).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )

    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    # print(tx_receipt['transactionHash'])
    return tx_receipt['status']

def create_expense(group_id, amount, description, member_addresses):
    nonce = w3.eth.getTransactionCount(me.address)
    group_id_bytes = w3.toBytes(hexstr=group_id)
    current_ts = int(time.time())

    txn = counter.functions.createExpense(group_id_bytes, amount, description,
                        current_ts, member_addresses).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )

    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(tx_receipt['transactionHash'])
    return current_ts, tx_receipt['status']

def remove_group_membership(group_id, member_address):

    nonce = w3.eth.getTransactionCount(me.address)
    group_id_bytes = w3.toBytes(hexstr=group_id)
    # group_id_bytes = group_id.encode('utf-8')
    # print(type(group_id_bytes))
    # print(group_id_bytes)
    # print(type(member_address))
    txn = counter.functions.removeGroupMembership(group_id_bytes,
                        member_address).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )

    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    # print(tx_receipt['transactionHash'])
    return tx_receipt['status']


def settle_expense(group_id, amount):
    nonce = w3.eth.getTransactionCount(me.address)
    group_id_bytes = w3.toBytes(hexstr=group_id)
    current_ts = int(time.time())

    txn = counter.functions.settleUp(group_id_bytes, amount,
                        current_ts).buildTransaction(
                        {
                        "nonce": nonce,
                        "gas": w3.toHex(3000000)
                        }
                    )

    signed = w3.eth.account.signTransaction(txn, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(tx_receipt['transactionHash'])
    return current_ts, tx_receipt['status'], me.address

