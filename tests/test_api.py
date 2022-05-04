from main import server

def test_api_integration():
    req = server.test_client().get('/')
    assert req.status_code == 200