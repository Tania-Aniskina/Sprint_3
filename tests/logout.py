from conftest import *
from tests.locators import Locators
import time

class TestLogOut:
    # Проверка выход по кнопке «Выйти» в личном кабинете
    def test_log_out(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.logout_btn).click()
        enter_btn = driver.find_element(By.XPATH, Locators.enter_btn).text
        assert enter_btn == 'Войти'