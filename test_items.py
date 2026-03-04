import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_should_see_add_to_cart_button_on_wildberries(browser):
    """Тест проверяет наличие кнопки добавления в корзину на Wildberries"""
    
    # Открываем главную страницу Wildberries
    link = "https://global.wildberries.ru/"
    browser.get(link)
    
    # Для визуальной проверки (раскомментируйте при необходимости)
    # time.sleep(30)
    
    # Проверяем наличие элемента корзины в шапке сайта
    try:
        # Ищем кнопку/ссылку корзины в навигационной панели
        cart_element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar-pc__link[data-wba-header-name='Cart']"))
        )
        
        # Проверяем, что элемент видим
        assert cart_element.is_displayed(), "Элемент корзины не виден на странице"
        
        # Получаем и выводим текст кнопки корзины
        cart_text = cart_element.text
        print(f"\nТекст элемента корзины: '{cart_text}'")
        
        # Проверяем, что элемент содержит иконку корзины
        cart_icon = cart_element.find_element(By.CSS_SELECTOR, ".navbar-pc__icon--basket")
        assert cart_icon.is_displayed(), "Иконка корзины не найдена"
        
    except Exception as e:
        # Если элемент не найден, тест падает с информативным сообщением
        pytest.fail(f"Элемент корзины не найден на странице Wildberries. Ошибка: {e}")

def test_guest_should_see_product_add_to_cart_button(browser):
    """Тест проверяет наличие кнопки добавления товара в корзину на странице товара"""
    
    # Открываем страницу с конкретным товаром (например, книга)
    # Это реальный товар на Wildberries, но ссылку нужно проверить
    link = "https://global.wildberries.ru/catalog/books/poznavatelnaya-literatura"  # Замените на актуальную ссылку товара
    browser.get(link)
    
    # Для визуальной проверки (раскомментируйте для проверки задания)
    time.sleep(30)
    
    # Поиск кнопки добавления в корзину на странице товара
    # Примечание: селектор может меняться, нужно уточнить актуальный
    selectors = [
        ".product-page__btn-buy",  # Возможный селектор кнопки покупки
        ".btn-main",                # Общий класс кнопок
        "[data-tag='addToBasket']",  # Data-атрибут для добавления в корзину
        ".j-add-to-basket"           # jQuery-селектор
    ]
    
    button_found = False
    button_text = ""
    
    for selector in selectors:
        try:
            buttons = browser.find_elements(By.CSS_SELECTOR, selector)
            for button in buttons:
                if button.is_displayed():
                    button_found = True
                    button_text = button.text
                    print(f"\nКнопка найдена по селектору: {selector}")
                    print(f"Текст кнопки: '{button_text}'")
                    break
            if button_found:
                break
        except:
            continue
    
    assert button_found, "Кнопка добавления в корзину не найдена на странице товара"

def test_basket_icon_visible_in_header_for_all_languages(browser):
    """Тест проверяет, что иконка корзины отображается в шапке для любого языка"""
    
    link = "https://global.wildberries.ru/"
    browser.get(link)
    
    # Проверяем наличие блока корзины в шапке
    basket_content = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#basketContent"))
    )
    
    # Проверяем, что ссылка на корзину существует
    basket_link = basket_content.find_element(By.CSS_SELECTOR, ".navbar-pc__link")
    
    assert basket_link.is_displayed(), "Ссылка на корзину не отображается"
    assert basket_link.get_attribute("href"), "У ссылки на корзину отсутствует href"
    
    # Проверяем наличие иконки корзины
    basket_icon = basket_link.find_element(By.CSS_SELECTOR, ".navbar-pc__icon--basket")
    assert basket_icon.is_displayed(), "Иконка корзины не отображается"