import allure
import pytest
import requests
from data import OrderData, StatusCodes
from urls import ApiUrls

@allure.feature("Создание заказа")
class TestOrderCreate:
    @pytest.mark.parametrize(
        "color", OrderData.COLOR_VARIANTS
    )
    @allure.title("Параметризованный тест: создание заказа с разными цветами")
    def test_create_order_parametrized(self, color):
        with allure.step("Подготовить данные для заказа"):
            order_payload = OrderData.BASE_ORDER_DATA
            order_payload["color"] = color

        with allure.step(f"Отправить запрос на создание заказа (цвет: {color})"):
            response = requests.post(ApiUrls.ORDER_CREATE, json=order_payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.CREATED

        with allure.step("Проверить наличие track в ответе"):
            response_data = response.json()
            assert "track" in response_data
