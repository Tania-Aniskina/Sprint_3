class Locators:
    # Кнопка "Войти в аакаунт"
    login_account_btn = '//*[text()="Войти в аккаунт"]'
    # Поле Имя
    email_field = './/label[text()="Email"]//following-sibling::*'
    # Поле Email
    user_name_field = 'name'
    # Поле Пароль
    password_field = './/input[@name="Пароль"]'
    # Кнопка "Войти"
    enter_btn = './/button[text()="Войти"]'
    # Кнопка "Личный кабинет"
    private_room_btn = './/p[text()="Личный Кабинет"]'
    # Заголовок "Вход" формы входа в аккаунт
    enter_title = './/h2[text()="Вход"]'
    # Кнопка "Сохранить"
    save_btn = './/button[text()="Сохранить"]'
    # Кнопка "Выход"
    logout_btn = './/button[text()="Выход"]'
    # Ссылка "Зарегистрироваться"
    registration_link_btn = './/a[text()="Зарегистрироваться"]'
    # Кнопка "Зарегистрироваться"
    registration_btn = './/button[text()="Зарегистрироваться"]'
    # Ссылка "Восстановить пароль"
    restore_password_link_btn = './/a[text()="Восстановить пароль"]'
    # Ссылка "Войти"
    enter_link_btn = './/a[text()="Войти"]'
    # Сообщение "Некорректный пароль"
    incorrect_password_message = './/p[text()="Некорректный пароль"]'
    # Кнопка "Оформить заказ"
    make_order_btn = './/button[text()="Оформить заказ"]'
    # Кнопка "Конструктор"
    constructor_btn = './/p[text()="Конструктор"]'
    # Кнопка логотипа
    logo_btn = './/div[@class="AppHeader_header__logo__2D0X2"]'
    # Заголовок "Собери бургер"
    make_burger_title = './/h1[text()="Соберите бургер"]'
    # Раздел "Соусы"
    sause_section = './/span[text()="Соусы"]'
    # Выбранный раздел "Соусы"
    select_sause_section = './/div[contains(@class, "current")]/child::span[text()="Соусы"]'
    # Раздел "Булки"
    bagels_section = './/span[text()="Булки"]'
    # Невыбранный раздел "Булки"
    no_select_bagels_section = './/div[contains(@class, "noselect") and not (contains(@class, "current"))]/child::span[text()="Булки"]'
    # Выбранный раздел "Булки"
    select_bagels_section = './/div[contains(@class, "current")]/child::span[text()="Булки"]'
    # Раздел "Начинки"
    filling_section = './/span[text()="Начинки"]'
    # Выбранный раздел "Начинки"
    select_filling_section = './/div[contains(@class, "current")]/child::span[text()="Начинки"]'

