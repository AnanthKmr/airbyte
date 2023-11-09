import pytest
import requests
import json
from source_python_http_tutorial import source as src
from datetime import datetime
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator

@pytest.fixture
def readConfig():
    with open('source-python-http-tutorial/secrets/config.json', 'r') as f:
        data = json.load(f)
        return data

def test_api_request(readConfig):
    start_date = datetime.strptime(readConfig["start_date"], "%Y-%m-%d")
    # threshold = readConfig['threshold']
    param_base_currency = readConfig['base']
    header_apikey = readConfig['apikey']
    url_base = f"https://api.apilayer.com/exchangerates_data/latest?base={param_base_currency}"
    headers = {"apikey": header_apikey, "start_date": start_date}
    response = requests.get(url_base, headers)
    assert response.status_code == 200
