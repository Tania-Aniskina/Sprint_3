from conftest import *
import random
from tests.locators import Locators


class TestRegistration:
    # Проверка успешной регистрации с тремя разными доменами почты
    @pytest.mark.parametrize('email', ['q@ya.ru', 'q@gmail.com', 'q@123.ru'])
    def test_registration_positive(self, driver, email):
        driver.implicitly_wait(3)
        a = random.randint(0, 1000)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.registration_link_btn).click()
        driver.find_element(By.NAME, Locators.user_name_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.email_field).send_keys(str(a) + email)
        driver.find_element(By.XPATH, Locators.password_field).send_keys(str(a) + 'password')
        driver.find_element(By.XPATH, Locators.registration_btn).click()
        enter_btn = driver.find_element(By.XPATH, Locators.enter_btn).text
        assert enter_btn == 'Войти'

    # Проверка ошибки некорректного пароля
    def test_registration_negative(self, driver):
        driver.implicitly_wait(3)
        a = random.randint(0, 1000)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.registration_link_btn).click()
        driver.find_element(By.NAME, Locators.user_name_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.email_field).send_keys(str(a) + 'krya@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys(a)
        driver.find_element(By.XPATH, Locators.registration_btn).click()
        incorrect_password_message = driver.find_element(By.XPATH, Locators.incorrect_password_message).text
        assert incorrect_password_message == 'Некорректный пароль'


