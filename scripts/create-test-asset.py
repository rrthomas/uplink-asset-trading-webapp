import binascii
import os
from ecdsa import SigningKey, SECP256k1
from uplink import *

# This script creates an asset in the Uplink system, and
# circulates all the corresponding tokens to the account
# that issued the asset.

rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)

# ACCOUNT_ADDRESS is the user who is creating the asset, and to whom
# all the asset tokens will be circulated.

# SIGNING_KEY_HEX is the private key that was generated when the account
# was created.

# If you used scripts/create-test-accounts.py, you can get suitable
# values from the output of that script, and set environment variables
# before running this script.

# NB: The script will output the private key as: b'SOMETHING'
# The corresponding enviroment variable should be set like this:
#   export SIGNING_KEY_HEX=SOMETHING

if not 'ACCOUNT_ADDRESS' in os.environ:
    raise ValueError("ACCOUNT_ADDRESS environment variable is not set. Which account is issuing this asset?")

if not 'SIGNING_KEY_HEX' in os.environ:
    raise ValueError('SIGNING_KEY_HEX environment variable is not set. Provide the private key that corresponds to the ACCOUNT_ADDRESS')

account_address = os.environ['ACCOUNT_ADDRESS']
signing_key     = os.environ['SIGNING_KEY_HEX']

skey = binascii.a2b_hex(signing_key)

privkey = SigningKey.from_string(skey, curve = SECP256k1)

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

# Circulate the asset to the issuer, so that its tokens can be
# transferred between accounts

result = rpc.uplink_circulate_asset(
        private_key   = privkey,
        from_address  = account_address,
        amount        = 1000,
        asset_address = asset_address
)

