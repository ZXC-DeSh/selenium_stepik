from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Создаем драйвер
driver = webdriver.Chrome()

try:
    # Открываем сайт
    driver.get("https://fishtext.ru")
    time.sleep(2)
    
    # Находим поле ввода количества абзацев
    paragraphs_input = driver.find_element(By.NAME, "zas")
    paragraphs_input.clear()
    paragraphs_input.send_keys("99")
    
    # Нажимаем кнопку генерации
    generate_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    generate_btn.click()
    
    # Ждем генерации текста
    time.sleep(3)
    
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p.text-justify")
    all_text = ""
    for p in paragraphs:
        all_text += p.text + " "  # добавляем текст каждого абзаца
    
    # Считаем количество слов "структура" во всем собранном тексте
    word_count = len(re.findall(r'структура', all_text))
    
    print(f"\nСгенерировано {len(paragraphs)} абзацев текста")
    print(f"Слово 'структура' встречается {word_count} раз(а)")

finally:
    time.sleep(10)
    driver.quit()