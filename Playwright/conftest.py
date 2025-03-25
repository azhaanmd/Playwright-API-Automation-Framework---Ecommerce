import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )

    parser.addoption(
        "--url_name", action="store", default="chrome", help="write URL"
    )

@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page #yield behaves as return
    context.close()
    browser.close()