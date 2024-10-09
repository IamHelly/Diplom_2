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
def payload_login_new():
    payload_login_new = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        }
    return payload_login_new

@pytest.fixture()
def payload_login():
    payload_login = {
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        }
    return payload_login
