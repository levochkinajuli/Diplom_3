import pytest
import string
import random
import requests
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()


@pytest.fixture
def user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(5)}@ya.ru'
    password = generate_random_string(8)
    name = generate_random_string(5)

    url = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    data = {"email": email, "password": password, "name": name}
    response = requests.post(url, json=data)

    token = response.json().get("accessToken")

    yield data

    delete_url = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    headers = {'Authorization': token}
    requests.delete(delete_url, headers=headers)


@pytest.fixture
def browser_with_user(browser, user):
    email = user["email"]
    password = user["password"]

    LoginPage(browser).login(email, password)

    return browser
