from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

# Создаем драйвер
driver = webdriver.Chrome()

try:
    # Открываем Википедию
    driver.get("https://ru.wikipedia.org")
    
    # Вводим "Лермонтов"
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Лермонтов")
    
    # Нажимаем на кнопку поиска
    search_button = driver.find_element(By.ID, "searchButton")
    search_button.click()

    # Ждем загрузки
    time.sleep(3)

    infobox = driver.find_element(By.CSS_SELECTOR, ".infobox")
    rows = infobox.find_elements(By.TAG_NAME, "tr")
        
    for row in rows:
        if "Дата рождения" in row.text:
            date_text = row.text.replace("Дата рождения", "").strip()
            date_text = re.sub(r'\[\d+\]', '', date_text)
            print(f"Дата рождения: {date_text}")
            break

finally:
    time.sleep(10)
    driver.quit()