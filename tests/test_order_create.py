import allure
import pytest
import requests
from conftest import BASE_URL

@allure.feature("Создание заказа")
class TestOrderCreate:
    @pytest.mark.parametrize(
        "color", [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    @allure.title("Параметризованный тест: создание заказа с разными цветами")
    def test_create_order_parametrized(self, create_order_payload, color):
        create_order_payload["color"] = color

        response = requests.post(f'{BASE_URL}/api/v1/orders', json=create_order_payload)

        assert response.status_code == 201
        assert "track" in response.json()
