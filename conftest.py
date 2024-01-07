import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from locators import MainPageLocators, LoginPageLocators
import string
import random
import requests


@pytest.fixture
def browser():
    service = Service(executable_path='C:/Users/Юлия/WebDriver/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://stellarburgers.nomoreparties.site/')

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
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
    delete_response = requests.delete(delete_url, headers=headers)

    assert delete_response.status_code == 202


@pytest.fixture
def browser_with_user(user):
    service = Service(executable_path='C:/Users/Юлия/WebDriver/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://stellarburgers.nomoreparties.site/')
    data = user
    email = data["email"]
    password = data["password"]
    driver.find_element(*MainPageLocators.BUTT_ENTER_MAIN).click()
    driver.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(email)
    driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(password)
    driver.find_element(*LoginPageLocators.BUTT_ENTER).click()

    yield driver
    driver.quit()
