import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import highlight


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_all_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        element.click()
        time.sleep(1)
    def click_webElement_element(self, webElement):
        highlight(webElement, self.driver)
        time.sleep(1)
        webElement.click()

    def is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        return element.is_displayed()

    def insert_text(self, locator, text):
        element = self.driver.find_element(*locator)
        highlight(element, self.driver)
        element.click()
        element.clear()
        element.send_keys(text)
