from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем сайт
    link = "https://the-internet.herokuapp.com/upload"
    browser = webdriver.Chrome()
    browser.get(link)

   # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')
    
    # Загружаем файл
    browser.find_element(By.ID, "file-upload").send_keys(file_path)
    browser.find_element(By.ID, "file-submit").click()
    
    # Ждем загрузки
    time.sleep(2)
    
    # Проверяем результат
    result = browser.find_element(By.TAG_NAME, "h3").text
    print("Результат загрузки:", result)

finally:
    time.sleep(7)
    browser.quit()