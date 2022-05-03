import requests
import pytest

base_url  = 'http://127.0.0.1:5000/'

def test_api_integration():
    req = requests.get(base_url)
    assert req.status_code == 200