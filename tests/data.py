class ErrorMessages:
    NOT_ENOUGH_DATA_TO_CREATE_ACCOUNT = "Недостаточно данных для создания учетной записи"
    LOGIN_ALREADY_EXISTS = "Этот логин уже используется"
    NOT_ENOUGH_DATA_TO_LOGIN = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409

class OrderData:
    BASE_ORDER_DATA = {
        "firstName": "Алина",
        "lastName": "Мурашко",
        "address": "Новосибирск, ул. Обская, 50",
        "metroStation": 1,
        "phone": "+79135553535",
        "rentTime": 5,
        "deliveryDate": "2026-02-07",
        "comment": "Тестовый заказ"
    }

    COLOR_VARIANTS = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]

    LIMIT_VARIANTS = [1, 5, 10, 15]

class CourierData:
    SUCCESS_RESPONSE = {"ok": True}
