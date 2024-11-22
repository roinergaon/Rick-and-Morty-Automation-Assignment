from selenium.webdriver.common.by import By
from UI_Rick_and_Morhy.pageObjects.base_page import BasePage


class GooglePage(BasePage):
    images_element = (By.CSS_SELECTOR, "[aria-label='Search for Images ']")
    english_element = (By.XPATH, "//a[text()='English']")
    accept_button_locator = (By.XPATH, "//button[normalize-space()='Accept all']")

    def open_google_images(self):
        self.click_element(self.images_element)



