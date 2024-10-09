from data_users import *
import pytest


@pytest.fixture()
def payload_new():
    payload_new = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD,
            "name": DataUniqueUser.NAME
        }
    return payload_new


@pytest.fixture()
def payload_new_unnamed():
    payload_new_unnamed = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        }
    return payload_new_unnamed


@pytest.fixture()
def payload_login_new():
    payload_login_new = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        }
    return payload_login_new


@pytest.fixture()
def payload_existing():
    payload_existing = {
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD,
            "name": DataUser.NAME
        }
    return payload_existing


@pytest.fixture()
def payload_login():
    payload_login = {
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        }
    return payload_login


@pytest.fixture()
def payload_email_error():
    payload_email_error = {
            "email": "olgamenyailova@yandex.com",
            "password": DataUser.PASSWORD
        }
    return payload_email_error


@pytest.fixture()
def payload_password_error():
    payload_password_error = {
            "email": DataUser.EMAIL,
            "password": "Йцукен123."
        }
    return payload_password_error
