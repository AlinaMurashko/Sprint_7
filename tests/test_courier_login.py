import allure
import requests
from conftest import BASE_URL

@allure.feature("Логин курьера")
class TestCourierLogin:
    @allure.title("Позитивный тест: успешная авторизация курьера")
    def test_login_courier_success(self, courier_data):
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Негативный тест: авторизация без логина")
    def test_login_without_login_fails(self, courier_data):
        payload = {
            "password": courier_data[1]
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title("Негативный тест: авторизация без пароля")
    def test_login_without_password_fails(self, courier_data):
        payload = {
            "login": courier_data[1]
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title("Негативный тест: авторизация с неверным логином")
    def test_login_with_wrong_login_fails(self, courier_data):
        payload = {
            "login": "wrong_login",
            "password": courier_data[1]
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Негативный тест: авторизация с неверным паролем")
    def test_login_with_wrong_password_fails(self, courier_data):
        payload = {
            "login": courier_data[0],
            "password": "wrong_password"
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title("Негативный тест: авторизация несуществующего курьера")
    def test_login_non_existent_courier_fails(self):
        payload = {
            "login": "non_existent_login",
            "password": "non_existent_password"
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
