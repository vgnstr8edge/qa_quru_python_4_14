import pytest
from selene import browser


"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture
def browser_desk():
    browser.config.hold_browser_open = True
    browser.open('https://github.com/')
    browser.driver.maximize_window()
    yield
    browser.quit()


@pytest.fixture
def browser_mobile():
    browser.config.hold_browser_open = True
    browser.open('https://github.com/')
    browser.config.window_width = 412
    browser.config.window_height = 914
    yield
    browser.quit()


def test_github_desktop(browser_desk):
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_mobile):
    browser.element('.Button-content div:nth-child(1)').click()
    browser.element('[href="/login"]').click()

