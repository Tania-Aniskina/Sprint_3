from conftest import *
from tests.locators import Locators


class TestLogin:
    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_enter_button_log_in(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'

    # Проверка входа через кнопку «Личный кабинет»
    def test_enter_private_room(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'

    # Проверка входа через кнопку в форме регистрации через личный кабинет
    def test_registration_enter_log_in_private_room(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.registration_link_btn).click()
        driver.find_element(By.XPATH, Locators.enter_link_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'

    # Проверка входа через кнопку в форме регистрации через кнопку "Вход в аккаунт"
    def test_registration_enter_button_log_in_(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.registration_link_btn).click()
        driver.find_element(By.XPATH, Locators.enter_link_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'

    # Проверка входа через кнопку в форме восстановления пароля через кнопку «Личный кабинет»
    def test_forgot_password_enter_log_in_button_private_room(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.restore_password_link_btn).click()
        driver.find_element(By.XPATH, Locators.enter_link_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'

    # Проверка входа через кнопку в форме восстановления пароля по кнопке «Войти в аккаунт» на главной
    def test_forgot_password_enter_button_log_in_button_log_in(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.restore_password_link_btn).click()
        driver.find_element(By.XPATH, Locators.enter_link_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        make_order_btn = driver.find_element(By.XPATH, Locators.make_order_btn).text
        assert make_order_btn == 'Оформить заказ'