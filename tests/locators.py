
# URLs
registration_page_url = 'https://stellarburgers.nomoreparties.site/register'  # ссылка регистрации
login_page_url = 'https://stellarburgers.nomoreparties.site/login'  # ссылка на вход
home_page_url = 'https://stellarburgers.nomoreparties.site/'  # ссылка на главную страницу
forgot_password_page_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
# ссылка на страницу восстановления пароля
account_page_url = 'https://stellarburgers.nomoreparties.site/account/profile'  # ссылка в Личный кабинет


# главная страница
souce_section_name = './/span[text()="Соусы"]'  # Секция с соусами, название
souce_section = './/span[text()="Соусы"]/parent::div'  # Секция с соусами

buns_section_name = './/span[text()="Булки"]'  # Секция с булками, название
buns_section = './/span[text()="Булки"]/parent::div'  # Секция с булками

filling_section_name = './/span[text()="Начинки"]'  # Секция с начинками, название
filling_section = './/span[text()="Начинки"]/parent::div'  # Секция с начинками

account_link = './/a[@href="/account"]'  # ссылка на Личный кабинет


# Форма регистрации и входа
registration_link = './/a[text()="Зарегистрироваться"]'  # Ссылка 'Зарегестрироваться'

log_in_text = './/h2[text()="Вход"]'  # Надпись 'Вход'

log_in_elements = './/*[contains(text(),"Войти")]'
# Элемент с текстом Войти - ссылки на форму входа и кнопки для входа

name_field = './/*[text() = "Имя"]/parent::div/input'  # Поле ввода 'Имя'
email_field = './/*[text() = "Email"]/parent::div/input'   # Поле ввода 'Email'
password_field = './/input[@name="Пароль"]'  # Поле ввода 'Пароль'
registration_button = './/button[text()="Зарегистрироваться"]'  # Кнопка 'Зарегистрироваться'

new_user_error_text = './/p[text()="Такой пользователь уже существует"]'
# надпись после попытки повторной регистрации с тем же логином
incorrect_password_error_text = './/p[text()="Некорректный пароль"]'  # ошибка о некорректном пароле


# Страница 'Личный Аккаунт'
log_out_button = './/button[text()="Выход"]'  # Кнопка выхода с аккаунта
account_login = './/*[text() = "Логин"]/parent::div/input'  # Поле "Логин"


# Хедер
logo_link = './/div[contains(@class, "logo")]/a'  # Логотип
constructor_link = './/p[text()="Конструктор"]/parent::a'  # Ссылка на главную страницу с Конструктором
