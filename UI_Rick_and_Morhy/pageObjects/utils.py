import os
import time
from datetime import datetime
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import allure
import requests
from selenium.webdriver.support.wait import WebDriverWait
from UI_Rick_and_Morhy.pageObjects.google_page import GooglePage

characters= {
    "First_character": 0,
    "Second_character": 1
}

def close_initial_google_popup_window(driver): # in case the browser opens with the coockies window "accept all"

    try:
        # Wait up to 2 seconds for the button to be clickable
        accept_button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(GooglePage.accept_button_locator)
        )
        accept_button.click()

    except:
        # Silently handle the case where the element doesn't appear
        pass

def open_the_english_version(driver): # in case the browser opens in hebrew

    try:
        # Wait up to 2 seconds for the English element to be clickable
        english_element = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable(GooglePage.english_element)
        )
        english_element.click()
    except:
        # Silently handle the case where the element doesn't appear
        pass



