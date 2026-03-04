from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем драйвер
driver = webdriver.Chrome()

try:
    # Открываем Metanit
    driver.get("https://metanit.com")
    
    # Ждем загрузку
    time.sleep(2)
    
    # Ищем раздел Python в боковом меню
    python_link = driver.find_element(By.XPATH, "//a[contains(@href, 'python')]")
    python_link.click()
    
    time.sleep(2)
    
    # Ищем руководство по Python
    tutorial_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Python') and contains(@href, 'tutorial')]")
    tutorial_link.click()
    
    time.sleep(2)
    
    # В боковой навигации ищем первую главу и первый параграф
    first_paragraph = driver.find_element(By.XPATH, "//a[contains(text(), '1.1') or contains(text(), 'Язык программирования Python')]")
    first_paragraph.click()
    
    time.sleep(2)

    page_title = driver.find_element(By.TAG_NAME, "h1").text
    print(f"Открыта страница: {page_title}")

finally:
    driver.quit()