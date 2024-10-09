from urls import Urls
import requests
import allure


class TestsRegistrationUser:
    @allure.title('Проверка создания уникального пользователя')
    def test_registration_unique_user(self, payload_new):
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload_new)
        check_success_registration_user = response_register.json()["success"]
        assert response_register.status_code == 200 and check_success_registration_user is True
        # Удаление созданного пользователя для сохранения условия уникальности регистрации
        token = response_register.json()["accessToken"]
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})

    @allure.title('Проверка создания пользователя, который уже зарегистрирован')
    def test_registration_existing_user(self, payload_existing):
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload_existing)
        message = response_register.json()["message"]
        assert response_register.status_code == 403 and message == 'User already exists'

    @allure.title('Проверка создания пользователя без заполнения одного из обязательных полей')
    def test_registration_user_without_required_parameter(self, payload_new_unnamed):
        response_register = requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload_new_unnamed)
        message = response_register.json()["message"]
        assert response_register.status_code == 403 and message == 'Email, password and name are required fields'
