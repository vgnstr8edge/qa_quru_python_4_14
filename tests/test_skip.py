import pytest
from selene import browser

"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


@pytest.fixture(params=['desk', 'mobile'])
def skip_param_browser(request):
    browser.open('https://github.com/')
    if request.param == 'desk':
        browser.driver.maximize_window()
    if request.param == 'mobile':
        browser.config.window_width = 412
        browser.config.window_height = 914
    yield request.param


def test_github_desktop(skip_param_browser):
    if skip_param_browser == 'desk':
        browser.open('https://github.com/')
        browser.element('[href="/login"]').click()
    if skip_param_browser == 'mobile':
        pytest.skip()


def test_github_mobile(skip_param_browser):
    if skip_param_browser == 'mobile':
        browser.open('https://github.com/')
        browser.element('.Button-content div:nth-child(1)').click()
        browser.element('[href="/login"]').click()
    if skip_param_browser == 'desk':
        pytest.skip()

