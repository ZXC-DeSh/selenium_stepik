from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Находим элемент-картинку и получаем значение атрибута valuex
    treasure_img = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure_img.get_attribute("valuex")
    
    # Вычисляем значение функции
    y = calc(x)
    
    # Вводим ответ в текстовое поле
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    
    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    robots_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule.click()
    
    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Ждем, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()