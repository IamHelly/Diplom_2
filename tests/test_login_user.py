from urls import Urls
from data_users import DataUser
import requests
import allure


class TestsLoginUser:

    @allure.title('Проверка логина под существующим пользователем')
    def test_login_as_existing_user(self):
        payload = {
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        }
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload)
        check_success_login_user = response_login.json()["success"]
        assert response_login.status_code == 200 and check_success_login_user is True

    @allure.title('Проверка невозможности логина с неверным логином')
    def test_not_login_with_invalid_email(self):
        payload = {
            "email": "olgamenyailova@yandex.com",
            "password": DataUser.PASSWORD
        }
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload)
        message = response_login.json()["message"]
        assert response_login.status_code == 401 and message == 'email or password are incorrect'

    @allure.title('Проверка невозможности логина с неверным паролем')
    def test_not_login_with_invalid_password(self):
        payload = {
            "email": DataUser.EMAIL,
            "password": "Йцукен123."
        }
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload)
        message = response_login.json()["message"]
        assert response_login.status_code == 401 and message == 'email or password are incorrect'
