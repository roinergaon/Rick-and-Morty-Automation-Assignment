import allure
import pytest
from UI_Rick_and_Morhy.pageObjects.google_images_page import GoogleImagesPage
from UI_Rick_and_Morhy.pageObjects.google_page import GooglePage

@pytest.mark.usefixtures("setup")
class TestGooglePage():

    @allure.description("Verify google image page is displayed")
    @allure.title("google image")
    @allure.feature("google image")
    @allure.tag("google image")
    def test_tc_01(self):
        google_page = GooglePage(self.driver)
        google_page.open_google_images()
        google_images_page = GoogleImagesPage(self.driver)

        is_google_images_displayed = google_images_page.is_displayed(GoogleImagesPage.google_image_pic) #verify enter to the right page
        assert is_google_images_displayed, "Google image isn't displayed"


