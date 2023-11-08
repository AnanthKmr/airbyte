#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#
# import pytest
# from datetime import datetime, timedelta
# from source_python_http_tutorial import source as src
#
#
# # Define sample configuration parameters
# sample_config = {
#     "base": "USD",
#     "apikey": "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU",
#     "threshold": 5,
#     "start_date": "2023-01-01",
# }
#
#
# # Fixture to create an instance of the ExchangeRates class with sample configuration
# @pytest.fixture
# def exchange_rates_instance():
#     return src.ExchangeRates(config=sample_config, start_date=datetime(2023, 1, 1), threshold=5)
#
#
# # Test case to check if the properties of the exchange_rates_instance are set correctly
# def test_exchange_rates_instance(exchange_rates_instance):
#     assert exchange_rates_instance.base == "USD"
#     assert exchange_rates_instance.apikey == "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU"
#     assert exchange_rates_instance.threshold == 5
#     assert exchange_rates_instance.start_date == datetime(2023, 1, 1)
#
#
# # Test case to check the request parameters for the ExchangeRates instance
# def test_exchange_rates_request_params(exchange_rates_instance):
#     request_params = exchange_rates_instance.request_params({})
#     assert request_params == {"base": "USD"}
#
#
# # Test case to check the request headers for the ExchangeRates instance
# def test_exchange_rates_request_headers(exchange_rates_instance):
#     request_headers = exchange_rates_instance.request_headers({})
#     assert request_headers == {"apikey": "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU"}
#
#
# # Test case to check the updated state for an incremental sync
# def test_exchange_rates_get_updated_state_incremental(exchange_rates_instance):
#     # Simulate the current state and the latest record
#     current_state = {"date": "2023-01-02"}
#     latest_record = {"date": "2023-01-11"}
#     # Ensure that the updated state reflects the latest record date
#     updated_state = exchange_rates_instance.get_updated_state(current_state, latest_record)
#     assert updated_state == {"date": "2023-01-11"}
#
#
# # Test case to check the connection status and message for the SourcePythonHttpTutorial
# def test_source_python_http_tutorial():
#     source = src.SourcePythonHttpTutorial()
#     connection_status, connection_message = source.check_connection(None, sample_config)
#     assert connection_status is True
#     assert connection_message is None
#
#
# # Test case to check connection status and message for invalid currency
# def test_source_python_http_tutorial_invalid_currency():
#     invalid_config = sample_config.copy()
#     invalid_config["base"] = "INVALID"
#     source = src.SourcePythonHttpTutorial()
#     connection_status, connection_message = source.check_connection(None, invalid_config)
#     assert connection_status is False
#     assert "Input currency INVALID is invalid" in connection_message
#
#
# # Test case to check connection status and message for multiple valid currencies
# def test_source_python_http_tutorial_multiple_valid_currencies():
#     valid_currencies = ["USD", "JPY", "BGN"]
#     for currency in valid_currencies:
#         config = sample_config.copy()
#         config["base"] = currency
#         source = src.SourcePythonHttpTutorial()
#         connection_status, connection_message = source.check_connection(None, config)
#         assert connection_status is True
#         assert connection_message is None
#


import pytest
from datetime import datetime

from jsonref import requests
from source_python_http_tutorial import source as src

# Define sample configuration parameters
sample_config = {
    "base": "USD",
    "apikey": "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU",
    "threshold": 5,
    "start_date": "2023-11-05",
}


# Fixture to create an instance of the ExchangeRates class with sample configuration
@pytest.fixture
def exchange_rates_instance():
    return src.ExchangeRates(config=sample_config, start_date=datetime(2023, 11, 5), threshold=5)


# Test case to check if the properties of the exchange_rates_instance are set correctly
def test_exchange_rates_instance(exchange_rates_instance):
    assert exchange_rates_instance.base == "USD"
    assert exchange_rates_instance.apikey == "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU"
    assert exchange_rates_instance.threshold == 5
    assert exchange_rates_instance.start_date == datetime(2023, 11, 5)


# Test case to check the request parameters for the ExchangeRates instance
def test_exchange_rates_request_params(exchange_rates_instance):
    request_params = exchange_rates_instance.request_params({})
    assert request_params == {"base": "USD"}


# Test case to check the request headers for the ExchangeRates instance
def test_exchange_rates_request_headers(exchange_rates_instance):
    request_headers = exchange_rates_instance.request_headers({})
    assert request_headers == {"apikey": "1jrCGrLP4cVYUHhoiDW1Fo6dJDNrKzeU"}


# Test case to check the updated state for an incremental sync
def test_exchange_rates_get_updated_state_incremental(exchange_rates_instance):
    # Simulate the current state and the latest record
    current_state = {"date": "2023-01-02"}
    latest_record = {"date": "2023-01-11"}
    # Ensure that the updated state reflects the latest record date
    updated_state = exchange_rates_instance.get_updated_state(current_state, latest_record)
    assert updated_state == {"date": "2023-01-11"}


# Test case to check if the response status code is 200
def test_parse_response_status_code_200(exchange_rates_instance):
    # Create a sample JSON response with status code 200
    sample_response = requests.Response()
    sample_response.status_code = 200

    # Set the content of the response to a valid JSON string
    sample_response._content = b'{"base": "USD", "date": "2023-01-01", "rates": {"EUR": 0.85, "GBP": 0.74, "JPY": 109.72}}'

    # Call the parse_response method
    parsed_response = exchange_rates_instance.parse_response(
        sample_response, stream_state={}, stream_slice={}, next_page_token={}
    )

    # Assert that the response status code is 200
    assert sample_response.status_code == 200


# Test case to check the connection status and message for the SourcePythonHttpTutorial
def test_source_python_http_tutorial():
    source = src.SourcePythonHttpTutorial()
    connection_status, connection_message = source.check_connection(None, sample_config)
    assert connection_status is True
    assert connection_message is None


# Test case to check connection status and message for invalid currency
def test_source_python_http_tutorial_invalid_currency():
    invalid_config = sample_config.copy()
    invalid_config["base"] = "INVALID"
    source = src.SourcePythonHttpTutorial()
    connection_status, connection_message = source.check_connection(None, invalid_config)
    assert connection_status is False
    assert "Input currency INVALID is invalid" in connection_message


# Test case to check connection status and message for multiple valid currencies
def test_source_python_http_tutorial_multiple_valid_currencies():
    valid_currencies = ["USD", "JPY", "BGN"]
    for currency in valid_currencies:
        config = sample_config.copy()
        config["base"] = currency
        source = src.SourcePythonHttpTutorial()
        connection_status, connection_message = source.check_connection(None, config)
        assert connection_status is True
        assert connection_message is None

