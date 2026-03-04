import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список URL для параметризации
urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    """Фикстура для запуска и закрытия браузера"""
    print("\nЗапуск браузера...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    print("\nЗакрытие браузера...")
    driver.quit()

@pytest.mark.parametrize('url', urls)
def test_stepik_feedback(browser, url):
    """Тест для проверки правильности ответа на Stepik"""
    
    # Открываем страницу
    browser.get(url)
    
    # Ждем загрузки страницы и нажимаем кнопку "Войти"
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))
    )
    login_button.click()
    
    # Вводим логин и пароль
    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_input.send_keys("egorkorobkin37@gmail.com")
    
    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys("67909141E!")
    
    # Нажимаем кнопку "Войти" в форме
    submit_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_button.click()
    
    # Ждем, что поп-ап с авторизацией исчез
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )
    
    # Ждем появления поля для ввода ответа
    textarea = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    
    # Вычисляем правильный ответ
    answer = math.log(int(time.time()))
    
    # Вводим ответ
    textarea.send_keys(str(answer))
    
    # Находим и нажимаем кнопку "Отправить"
    send_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    send_button.click()
    
    # Ждем появления фидбека
    feedback = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    )
    
    # Получаем текст фидбека
    feedback_text = feedback.text
    
    # Проверяем, что текст фидбека равен "Correct!"
    # Если текст другой, тест упадет и мы увидим кусочек послания
    assert feedback_text == "Correct!", f"Ожидался текст 'Correct!', но получен: '{feedback_text}'"