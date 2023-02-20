from conftest import *
from tests.locators import Locators
import time

class TestMoveToPrivateRoom:
    # Проверка перехода по клику на «Личный кабинет» без регистрации
    def test_move_by_click_to_private_room_without_registration(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        enter_title = driver.find_element(By.XPATH, Locators.enter_title).text
        assert enter_title == 'Вход'

    # Проверка перехода по клику на «Личный кабинет» после авторизации пользователя
    def test_move_by_click_to_private_room_with_registration(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        save_btn = driver.find_element(By.XPATH, Locators.save_btn).text
        assert save_btn == 'Сохранить'
