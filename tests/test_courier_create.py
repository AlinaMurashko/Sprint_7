import allure
import pytest
import requests
from data import CourierData, ErrorMessages, StatusCodes
from helpers import generate_random_string
from urls import ApiUrls

@allure.feature("Создание курьера")
class TestCourierCreate:
    @allure.title("Позитивный тест: успешное создание курьера")
    def test_register_new_courier_and_return_login_password_success(self):
        with allure.step("Подготовить нового курьера"):
            payload = {
                "login": generate_random_string(10),
                "password": generate_random_string(10),
                "firstName": generate_random_string(10)
            }

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(ApiUrls.COURIER_CREATE, data=payload)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.CREATED

        with allure.step("Проверить тело ответа"):
            assert response.json() == CourierData.SUCCESS_RESPONSE

    @allure.title("Негативный тест: создание дубликата курьера")
    def test_create_duplicate_courier_fails(self, courier_data):
        with allure.step("Отправить запрос на создание курьера с существующим логином"):
            response = requests.post(ApiUrls.COURIER_CREATE, data=courier_data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.CONFLICT

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.LOGIN_ALREADY_EXISTS in response.text

    @pytest.mark.parametrize(
        "missing_field, payload_data",
        [
            ("логин", {"password": "testpass", "firstName": "TestName"}),
            ("пароль", {"login": "testlogin", "firstName": "TestName"}),
            ("имя", {"login": "testlogin", "password": "testpass"})
        ]
    )
    @allure.title("Негативный тест: создание курьера без обязательных полей")
    def test_create_courier_with_missing_fields_fails(self, missing_field, payload_data):
        with allure.step(f"Подготовить данные без поля {missing_field}"):
            for key in payload_data:
                if payload_data[key] in ["testlogin", "testpass", "TestName"]:
                    payload_data[key] = generate_random_string(10)

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(ApiUrls.COURIER_CREATE, data=payload_data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == StatusCodes.BAD_REQUEST

        with allure.step("Проверить сообщение об ошибке"):
            assert ErrorMessages.NOT_ENOUGH_DATA_TO_CREATE_ACCOUNT in response.text
