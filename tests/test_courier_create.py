import allure
import requests
from conftest import BASE_URL, generate_random_string

@allure.feature("Создание курьера")
class TestCourierCreate:
    @allure.title("Позитивный тест: успешное создание курьера")
    def test_register_new_courier_and_return_login_password_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Негативный тест: создание дубликата курьера")
    def test_create_duplicate_courier_fails(self, courier_data):
        duplicate_payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=duplicate_payload)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title("Негативный тест: создание курьера без логина")
    def test_register_new_courier_and_return_login_password_without_login_fails(self):
        payload = {
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text

    @allure.title("Негативный тест: создание курьера без пароля")
    def test_register_new_courier_and_return_login_password_without_password_fails(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text

    @allure.title("Негативный тест: создание курьера без имени")
    def test_register_new_courier_and_return_login_password_without_first_name_fails(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text
