from conftest import *
from locators import Locators


class TestSectionConstructor:
    # Проверка переходы к разделам "Булки" для авторизированного пользователя
    def test_section_bagel_with_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        driver.find_element(By.XPATH, Locators.sause_section).click()
        driver.find_element(By.XPATH, Locators.no_select_bagels_section)
        driver.find_element(By.XPATH, Locators.bagels_section).click()
        driver.find_element(By.XPATH, Locators.select_bagels_section)

    # Проверка переходы к разделам "Булки" для неавторизированного пользователя
    def test_section_bagel_without_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.sause_section).click()
        driver.find_element(By.XPATH, Locators.no_select_bagels_section)
        driver.find_element(By.XPATH, Locators.bagels_section).click()
        driver.find_element(By.XPATH, Locators.select_bagels_section)

    # Проверка переходы к разделам "Соусы" для авторизированного пользователя
    def test_section_sauce_with_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        driver.find_element(By.XPATH, Locators.sause_section).click()
        driver.find_element(By.XPATH, Locators.select_sause_section)

    # Проверка переходы к разделам "Соусы" для неавторизированного пользователя
    def test_section_sauce_without_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.sause_section).click()
        driver.find_element(By.XPATH, Locators.select_sause_section)

    # Проверка переходы к разделам "Начинки" для авторизированного пользователя
    def test_section_filling_with_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.login_account_btn).click()
        driver.find_element(By.XPATH, Locators.email_field).send_keys('tania_aniskina_7_123@ya.ru')
        driver.find_element(By.XPATH, Locators.password_field).send_keys('Афанасий')
        driver.find_element(By.XPATH, Locators.enter_btn).click()
        driver.find_element(By.XPATH, Locators.filling_section).click()
        driver.find_element(By.XPATH, Locators.select_filling_section)

    # Проверка переходы к разделам "Начинки" для неавторизированного пользователя
    def test_section_filling_without_login(self, driver):
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, Locators.filling_section).click()
        driver.find_element(By.XPATH, Locators.select_filling_section)