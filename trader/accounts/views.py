from django.http import HttpResponse
from uplink import *

# Create your views here.

def is_validator(account):
    if 'validator' in account.metadata:
        return account.metadata['validator'] == 'true'


def index(request):
    rpc = UplinkJsonRpc(host="localhost", port=8545, tls=False)
    accounts = rpc.uplink_accounts()

    rtn = "<h2>Accounts</h2>\n"

    for acct in accounts:
        if not is_validator(acct):
            rtn += "<p>" + acct.address + "</p>"

    return HttpResponse(rtn)
