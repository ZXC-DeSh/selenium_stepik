from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем драйвер
driver = webdriver.Chrome()

try:
    # Открываем Stepik
    driver.get("https://stepik.org/lesson/236895/step/1")
    
    # Ждем загрузку страницы
    time.sleep(3)
    
    # Нажимаем кнопку "Войти"
    login_button = driver.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
    login_button.click()
    time.sleep(2)
    
    # Вводим логин и пароль
    email_input = driver.find_element(By.NAME, "login")
    email_input.send_keys("---")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("---")
    
    # Нажимаем кнопку "Войти" в форме
    submit_button = driver.find_element(By.CSS_SELECTOR, ".sign-form__btn")
    submit_button.click()
    
    # Проверяем успешность авторизации
    time.sleep(10)
    print("Авторизация выполнена")

finally:
    driver.quit()