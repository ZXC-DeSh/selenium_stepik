import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")  # первое поле input
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # поле с name="last_name"
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # поле с классом city
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")  # поле с id="country"
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()