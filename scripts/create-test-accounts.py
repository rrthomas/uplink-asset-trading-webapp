#!/usr/bin/env python3

import argparse
import binascii
import json

from uplink import *


# Command-line arguments
parser = argparse.ArgumentParser(prog='create-test-asset',
                                 description='''
This script creates some accounts with a 'Name' metadata
field, and outputs the account keys and addresses as JSON.
''')

args = parser.parse_args()


# Connect to Uplink
rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Create test accounts
def create_account(rpc, name):
    pubkey, skey = ecdsa_new()

    metadata = dict(Name = name)

    txhash, address = rpc.uplink_create_account(
            private_key=skey,
            public_key=pubkey,
            from_address=None,
            metadata=metadata,
            timezone="CET"
            )

    return {
        'name': name,
        'address': address,
        'public_key': binascii.b2a_hex(pubkey.to_string()).decode(),
        'private_key': binascii.b2a_hex(skey.to_string()).decode()
    }

accounts = []
for name in ["Alice", "Bob", "Charlie", "David"]:
    accounts.append(create_account(rpc, name))
print(json.dumps(accounts, sort_keys=True, indent=4))
