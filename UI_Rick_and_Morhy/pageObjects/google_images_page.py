from selenium.webdriver.common.by import By
from UI_Rick_and_Morhy.pageObjects.base_page import BasePage


class GoogleImagesPage(BasePage):
    google_image_pic = (By.CSS_SELECTOR, "[alt = 'Google Images']")
    search_field = (By.CSS_SELECTOR, "#APjFqb")
    search_button = (By.CSS_SELECTOR, "[class='zgAlFc']")
    images_results = (By.CSS_SELECTOR, "[jsname='dTDiAc']")
    selected_image = (By.CSS_SELECTOR, "a > img.sFlh5c.FyHeAf.iPVvYb")

    def enter_data(self, character_name):
        self.insert_text(self.search_field, character_name)

