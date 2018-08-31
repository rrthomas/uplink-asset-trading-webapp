from django.shortcuts import render
from uplink import *

# Create your views here.

def is_validator(account):
    if 'validator' in account.metadata:
        return account.metadata['validator'] == 'true'

def index(request):
    rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)
    all_accounts = rpc.uplink_accounts()

    accounts = []

    for acct in all_accounts:
        if not is_validator(acct):
            accounts.append(acct)

    context = {'accounts': accounts}

    return render(request, 'accounts/index.html', context)
