import pytest
from selene import browser


"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


@pytest.fixture(params=['desk', 'mobile'])
def param_browser(request):
    if request.param == 'desk':
        browser.open('https://github.com/')
        browser.driver.maximize_window()
    if request.param == 'mobile':
        browser.open('https://github.com/')
        browser.config.window_width = 412
        browser.config.window_height = 914


@pytest.mark.parametrize("param_browser", ['desk'], indirect=True)
def test_github_desktop(param_browser):
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize("param_browser", ['mobile'], indirect=True)
def test_github_mobile(param_browser):
    browser.element('.Button-content div:nth-child(1)').click()
    browser.element('[href="/login"]').click()

