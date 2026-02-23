from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Находим нужные элементы
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    # Прокручиваем страницу, чтобы элемент стал видимым
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    # Вводим ответ в текстовое поле
    answer_input.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio.click()

    # Нажимаем на кнопку Submit
    submit_button.click()

finally:
    # Закрываем браузер
    time.sleep(5)
    browser.quit()