from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("egor")
    
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("korobkin")
    
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("egorkorobkin@example.com")

    # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    
    # Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Закрываем браузер
    time.sleep(5)
    browser.quit()