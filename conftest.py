import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Добавление опции командной строки для выбора языка"""
    parser.addoption(
        '--language',
        action='store',
        default='ru',
        help="Choose language: --language=ru or --language=en"
    )

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура инициализации браузера с выбранным языком"""
    # Получаем параметр language из командной строки
    user_language = request.config.getoption("language")
    
    # Настройка опций браузера для указанного языка
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    
    # Инициализация браузера
    browser = webdriver.Chrome(options=options)
    
    # Неявное ожидание для стабильности тестов
    browser.implicitly_wait(10)
    
    # Возвращаем браузер в тест
    yield browser
    
    # Закрываем браузер после теста
    browser.quit()