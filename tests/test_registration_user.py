from urls import Urls
from data_users import DataUser, DataUniqueUser
import requests
import allure


class TestsRegistrationUser:
    @allure.title('Проверка создания уникального пользователя')
    def test_registration_unique_user(self):
        payload = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD,
            "name": DataUniqueUser.NAME
        }
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload)
        check_success_registration_user = response_register.json()["success"]
        assert response_register.status_code == 200 and check_success_registration_user is True
        # Удаление созданного пользователя для сохранения условия уникальности регистрации
        token = response_register.json()["accessToken"]
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_registration_existing_user(self):
        payload = {
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD,
            "name": DataUser.NAME
        }
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload)
        message = response_register.json()["message"]
        assert response_register.status_code == 403 and message == 'User already exists'

    @allure.title('Проверка создания пользователя без заполнения одного из обязательных полей')
    def test_registration_user_without_required_parameter(self):
        payload = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        }
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload)
        message = response_register.json()["message"]
        assert response_register.status_code == 403 and message == 'Email, password and name are required fields'
