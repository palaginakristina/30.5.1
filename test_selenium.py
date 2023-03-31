from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome(executable_path="C:\\Users\\duda-\\PycharmProjects\\30.5.1\\chromedriver.exe")

@pytest.fixture(autouse=True, scope="session")
def testing():
    '''Вход на страницу Мои питомцы - один раз на всю сессию'''
#    options = webdriver.ChromeOptions()
#    # задаем максимальный размер окна, чтобы была видна кнопка "Мои питомцы"
#    options.add_argument("--start-maximized")
#    pytest.driver = webdriver.Chrome('d:/chromedriver.exe', chrome_options=options)
    # этот вопрос решен ниже через проверку наличия иконки на экране браузера
pytest.driver = webdriver.Chrome('C:\\Users\\duda-\\PycharmProjects\\30.5.1\\chromedriver.exe')

    # активируем неявное ожидание (даем браузеру время на загрузку страницы)
    pytest.driver.implicitly_wait(10)

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    # Очищаем поле и вводим email
    field_email = pytest.driver.find_element(By.ID, 'email')
    field_email.clear()
    field_email.send_keys(valid_email)

    # Очищаем поле и вводим пароль
    field_pass = pytest.driver.find_element(By.ID, 'pass')
    field_pass.clear()
    field_pass.send_keys(valid_password)
    time.sleep(2)

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Проверяем, что находимся на главной странице пользователя
#    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets', "Некорректный email или пароль"
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        pytest.driver.quit()
        raise Exception("Некорректный email или пароль")
# Если окно браузера маленькое, т.е. на экране есть иконка, чтобы увидеть кнопку Мои питомцы, надо нажать на иконку
    if pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").is_displayed():
        time.sleep(2)
        pytest.driver.find_element(By.XPATH, "//body/nav[1]/button[1]").click()
        time.sleep(2)

# Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]").click()

# Проверяем, что перешли на страницу "Мои питомцы"
#    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets', "Это не страница Мои питомцы"
    if not pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets':
        pytest.driver.quit()
        raise Exception("Это не страница Мои питомцы")

    yield


pytest.driver.quit()
