import allure
import pytest
import requests
from data import OrderData, StatusCodes
from urls import ApiUrls

@allure.feature("Список заказов")
class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_get_order_list(self):
        with allure.step("Отправить запрос на получение списка заказов"):
            response = requests.get(ApiUrls.ORDER_LIST)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.OK

        with allure.step("Проверить структуру ответа"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)

    @pytest.mark.parametrize("limit", OrderData.LIMIT_VARIANTS)
    @allure.title("Получение списка заказов с разными лимитами")
    def test_get_order_list_with_different_limits(self, limit):
        with allure.step(f"Отправить запрос на получение списка заказов с лимитом {limit}"):
            response = requests.get(ApiUrls.ORDER_LIST, params={"limit": limit})

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.OK

        with allure.step("Проверить количество полученных заказов"):
            response_data = response.json()
            assert "orders" in response_data
            assert isinstance(response_data["orders"], list)
            assert len(response_data["orders"]) <= limit
