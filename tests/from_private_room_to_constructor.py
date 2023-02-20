from conftest import *
from tests.locators import Locators


class TestFromPrivate_room_to_constructor:
    # Проверка перехода по клику на «Конструктор» без авторизации
    def test_move_by_click_to_constructor(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.constructor_btn).click()
        make_burger_title = driver.find_element(By.XPATH, Locators.make_burger_title).text
        assert make_burger_title == 'Соберите бургер'

    # Проверка перехода по клику на «Конструктор» после авторизации
    def test_move_by_click_to_constructor_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        driver.find_element(By.XPATH, Locators.constructor_btn).click()
        make_burger_title = driver.find_element(By.XPATH, Locators.make_burger_title).text
        assert make_burger_title == 'Соберите бургер'

    # Проверка перехода по клику на логотип Stellar Burgers без регистрации
    def test_move_by_click_to_logo_without_registration(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.logo_btn).click()
        make_burger_title = driver.find_element(By.XPATH, Locators.make_burger_title).text
        assert make_burger_title == 'Соберите бургер'

    # Проверка перехода по клику на логотип Stellar Burgers с регистрацией
    def test_move_by_click_to_logo_with_registration(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.private_room_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        driver.find_element(By.XPATH, Locators.logo_btn).click()
        make_burger_title = driver.find_element(By.XPATH, Locators.make_burger_title).text
        assert make_burger_title == 'Соберите бургер'