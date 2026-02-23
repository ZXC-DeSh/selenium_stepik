from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Для проверки первой версии (работает)
    link = "http://suninjuly.github.io/registration1.html"
    
    # Для проверки второй версии (падает с ошибкой)
    # link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")
    
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("ivan.petrov@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    # Находим элемент с приветствием
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    
    # Проверяем, что ожидаемый текст совпадает с текстом на странице
    expected_text = "Congratulations! You have successfully registered!"
    actual_text = welcome_text
    
    assert expected_text == actual_text, f"Ожидаемый текст '{expected_text}', но получен '{actual_text}'"
    
    print("Тест успешно пройден! Регистрация выполнена.")

except Exception as e:
    print(f"Тест упал с ошибкой: {type(e).__name__}: {str(e)}")

finally:
    # Ожидание для визуальной оценки
    time.sleep(7)
    # Закрываем браузер
    browser.quit()