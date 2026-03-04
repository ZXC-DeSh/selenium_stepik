from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открываем страницу
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим элементы с числами и получаем их значения
    num1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    num2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    
    # Извлекаем текст и преобразуем в целые числа
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    
    # Вычисляем сумму
    sum_result = num1 + num2
    
    # Работа с выпадающим списком
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(sum_result))
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Закрываем браузер
    time.sleep(5)
    browser.quit()