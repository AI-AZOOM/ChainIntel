import requests

HEADERS = {'accept': 'application/json'}

def fetch_wallet_tokens(wallet):
    url = f'https://public-api.solscan.io/account/tokens?account={wallet}'
    res = requests.get(url, headers=HEADERS)
    return res.json() if res.status_code == 200 else None

def fetch_token_metadata(token_address):
    url = f'https://public-api.solscan.io/token/meta?tokenAddress={token_address}'
    res = requests.get(url, headers=HEADERS)
    return res.json() if res.status_code == 200 else None