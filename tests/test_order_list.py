import allure
import pytest
import requests
from conftest import BASE_URL

@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        response = requests.get(f'{BASE_URL}/api/v1/orders')

        assert response.status_code == 200
        response_data = response.json()

        assert "orders" in response_data
        assert isinstance(response_data["orders"], list)

    @pytest.mark.parametrize("limit", [1, 5, 10, 15])
    @allure.title("Получение списка заказов с разными лимитами")
    def test_get_order_list_with_different_limits(self, limit):
        response = requests.get(f'{BASE_URL}/api/v1/orders', params={"limit": limit})

        assert response.status_code == 200
        response_data = response.json()

        assert "orders" in response_data
        assert isinstance(response_data["orders"], list)
        assert len(response_data["orders"]) <= limit
