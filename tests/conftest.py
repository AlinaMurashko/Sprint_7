import pytest
import requests
import random
import string

BASE_URL = "http://qa-scooter.praktikum-services.ru"

# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@pytest.fixture
def courier_data():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{BASE_URL}/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

@pytest.fixture
def create_order_payload():
    return {
        "firstName": "Алина",
        "lastName": "Мурашко",
        "address": "Новосибирск, ул. Обская, 50",
        "metroStation": 1,
        "phone": "+79135553535",
        "rentTime": 5,
        "deliveryDate": "2026-02-07",
        "comment": "Тестовый заказ"
    }
