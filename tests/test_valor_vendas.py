import requests

def test_total_vendas():
    base_url  = 'http://127.0.0.1:5000/get-vendas'
    req = requests.get(base_url)
    dicionario = req.json()
    assert dicionario['total_vendas'] == 3026.1000000000004
