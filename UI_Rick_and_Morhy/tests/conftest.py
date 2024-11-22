import pytest
from selenium import webdriver
from UI_Rick_and_Morhy.pageObjects.utils import close_initial_google_popup_window, open_the_english_version
from config import UI_base_url
from API_Rick_and_Morty.api_task import run_api_task

@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(UI_base_url)
    close_initial_google_popup_window(driver)  # in case it exists
    open_the_english_version(driver)  # in case the Google in the hebrew change to english
    characters = run_api_task()
    request.cls.driver = driver
    request.cls.characters = characters
    yield
    driver.close()


