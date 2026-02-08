import pytest
import requests
from data import StatusCodes
from helpers import generate_random_string
from urls import ApiUrls

@pytest.fixture
def courier_data():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

    response = requests.post(ApiUrls.COURIER_CREATE, data=payload)

    if response.status_code == StatusCodes.CREATED:
        return payload
    else:
        raise Exception(f"Не удалось создать курьера: {response.text}")
