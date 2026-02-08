import allure
import pytest
import requests
from data import ErrorMessages, StatusCodes
from helpers import generate_random_string
from urls import ApiUrls

@allure.feature("Логин курьера")
class TestCourierLogin:
    @allure.title("Позитивный тест: успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        with allure.step("Подготовить данные для авторизации"):
            payload = {
                "login": courier_data["login"],
                "password": courier_data["password"]
            }

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(ApiUrls.COURIER_LOGIN, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.OK

        with allure.step("Проверить наличие ID в ответе"):
            assert "id" in response.json()

    @pytest.mark.parametrize(
        "missing_field, payload",
        [
            ("логин", {"password": "testpassword"}),
            ("пароль", {"login": "testlogin"})
        ]
    )
    @allure.title("Негативный тест: авторизация без обязательных полей")
    def test_login_missing_fields_fails(self, missing_field, payload):
        with allure.step(f"Подготовить данные без поля {missing_field}"):
            for key in payload:
                if payload[key].startswith("test"):
                    payload[key] = generate_random_string(10)

        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(ApiUrls.COURIER_LOGIN, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.BAD_REQUEST

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.NOT_ENOUGH_DATA_TO_LOGIN in response.text

    @allure.title("Негативный тест: авторизация с неверным логином")
    def test_login_with_wrong_login_fails(self, courier_data):
        payload = {
            "login": "wrong_login",
            "password": courier_data["password"]
        }
        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(ApiUrls.COURIER_LOGIN, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.NOT_FOUND

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text

    @allure.title("Негативный тест: авторизация с неверным паролем")
    def test_login_with_wrong_password_fails(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": "wrong_password"
        }
        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(ApiUrls.COURIER_LOGIN, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.NOT_FOUND

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text

    @allure.title("Негативный тест: авторизация несуществующего курьера")
    def test_login_non_existent_courier_fails(self):
        payload = {
            "login": "non_existent_login",
            "password": "non_existent_password"
        }
        with allure.step("Отправить запрос на авторизацию"):
            response = requests.post(ApiUrls.COURIER_LOGIN, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.NOT_FOUND

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
