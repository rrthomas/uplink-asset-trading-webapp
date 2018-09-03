#!/usr/bin/env python3

import os
import argparse
import binascii

from ecdsa import SigningKey, SECP256k1
from uplink import *


# Command-line arguments
parser = argparse.ArgumentParser(prog='create-test-asset',
                                 description='''
Creates an asset in the Uplink system, and circulate all the
corresponding tokens to the account that issued the asset.
''')
parser.add_argument('account_address', metavar='ACCOUNT-ADDRESS', nargs=1,
                    help="The account creating the asset, to which the asset tokens will be circulated")
parser.add_argument('signing_key', metavar='SIGNING-KEY-HEX', nargs=1,
                    help="The account's private key")

args = parser.parse_args()

account_address = args.account_address[0]
signing_key = args.signing_key[0]


# Recode keys
skey = binascii.a2b_hex(signing_key)
privkey = SigningKey.from_string(skey, curve = SECP256k1)

# Connect to Uplink
rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# Create asset
tx_hash, asset_address = rpc.uplink_create_asset(
        private_key    = privkey,
        origin         = account_address,
        name           = "Toyota Prius XV189CF",
        supply         = 1000,
        asset_type_nm  = "Discrete",
        reference      = "Token",
        issuer         = account_address
)
print("Asset address: " + asset_address)

# Circulate asset to issuer, so its tokens can be transferred between
# accounts
result = rpc.uplink_circulate_asset(
        private_key   = privkey,
        from_address  = account_address,
        amount        = 1000,
        asset_address = asset_address
)
