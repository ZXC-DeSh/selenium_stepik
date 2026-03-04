import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BaseRegistrationTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Подготовка перед всеми тестами класса"""
        cls.browser = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        """Очистка после всех тестов класса"""
        time.sleep(7)
        cls.browser.quit()
    
    def fill_and_submit_form(self, link):
        """Заполнение и отправка формы"""
        self.browser.get(link)
        
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("egor")
        
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("korobkin")
        
        email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("egorkor@www.com")
        
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        time.sleep(1)
        
        return self.browser.find_element(By.TAG_NAME, "h1").text

class TestRegistrationFirstPage(BaseRegistrationTest):
    """Тесты для первой страницы регистрации"""
    
    def test_registration_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_and_submit_form(link)
        
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, welcome_text)

class TestRegistrationSecondPage(BaseRegistrationTest):
    """Тесты для второй страницы регистрации"""
    
    def test_registration_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_and_submit_form(link)
        
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(expected_text, welcome_text)

if __name__ == "__main__":
    unittest.main()