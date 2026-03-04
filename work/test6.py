from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Создаем драйвер
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:

    driver.get("https://github.com")
    
    # Нажимаем кнопку Sign in
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.logged-out.env-production.page-responsive.header-overlay.header-overlay-fixed.js-header-overlay-fixed > div.position-relative.header-wrapper.js-header-wrapper > header > div > div.d-flex.flex-justify-between.flex-items-center.width-full.width-lg-auto > div.d-flex.flex-1.flex-order-2.text-right.d-lg-none.gap-2.flex-justify-end > a")))
    sign_in_btn.click()
    
    # Вводим логин и пароль
    login_input = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
    login_input.send_keys("ZXC-DeSh")
    
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Kf96Jfl69")
    
    # Нажимаем кнопку входа
    submit_btn = driver.find_element(By.NAME, "commit")
    submit_btn.click()
    
    # Ждем успешной авторизации
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".avatar")))    
    time.sleep(2)

   
    # Нажимаем кнопку "New"
    new_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.logged-in.env-production.page-responsive.full-width > div.application-main > div > div > aside > div > div > loading-context > div > div > div > div > div.hide-sm.hide-md.mb-1.d-flex.flex-justify-between.flex-items-center > a")))
    new_btn.click()
    
    # Заполняем название репозитория
    repo_name = wait.until(EC.presence_of_element_located((By.ID, "repository_name")))
    repo_name.send_keys("selenium_practice")
    
    # Заполняем описание
    repo_desc = driver.find_element(By.ID, "repository_description")
    repo_desc.send_keys("Задание 2 проверочной работы по Selenium")
    
    # Нажимаем кнопку создания
    create_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    create_btn.click()
    
    # Ждем создания и проверяем
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".repository-content")))
    print(f"Репозиторий успешно создан!")
    
    # Получаем URL созданного репозитория
    current_url = driver.current_url
    print(f"URL репозитория: {current_url}")

except TimeoutException:
    print("Ошибка: элемент не найден на странице")
except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Даем время посмотреть результат перед закрытием
    time.sleep(5)
    driver.quit()