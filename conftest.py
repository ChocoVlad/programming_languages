import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers.table_helper import Table


@pytest.fixture(scope="session")
def driver():
    """
    Init a  Chrome WebDriver session.
    """
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def table_data(driver):
    """
    Navigates to the site page and returns a list of RowDataModel instances.
    """
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    driver.get(url)
    table = Table(driver, "table.wikitable")
    return table.get_rows_model()
