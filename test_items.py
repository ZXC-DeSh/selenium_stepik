import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time 

@pytest.mark.parametrize("item_link", ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_items(browser, item_link):
    browser.get(item_link)
    time.sleep(30)
    add_to_basket_btn = browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert len(add_to_basket_btn) > 0, "Кнопка 'Add to basket' не найдена на странице"
   