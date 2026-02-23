from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Переключаемся на confirm и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # Теперь мы на новой странице. Находим значение x и вычисляем функцию
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Получаем число из итогового alert
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Результат: {alert_text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()