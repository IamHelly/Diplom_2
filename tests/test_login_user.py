from urls import Urls
import requests
import allure


class TestsLoginUser:

    @allure.title('Проверка логина под существующим пользователем')
    def test_login_as_existing_user(self, payload_login):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload_login)
        check_success_login_user = response_login.json()["success"]
        assert response_login.status_code == 200 and check_success_login_user is True

    @allure.title('Проверка невозможности логина с неверным логином')
    def test_not_login_with_invalid_email(self, payload_email_error):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload_email_error)
        message = response_login.json()["message"]
        assert response_login.status_code == 401 and message == 'email or password are incorrect'

    @allure.title('Проверка невозможности логина с неверным паролем')
    def test_not_login_with_invalid_password(self, payload_password_error):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data=payload_password_error)
        message = response_login.json()["message"]
        assert response_login.status_code == 401 and message == 'email or password are incorrect'
