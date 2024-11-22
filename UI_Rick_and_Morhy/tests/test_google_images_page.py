import allure
import pytest
from UI_Rick_and_Morhy.pageObjects.google_images_page import GoogleImagesPage
from UI_Rick_and_Morhy.pageObjects.google_page import GooglePage
from UI_Rick_and_Morhy.pageObjects.utils import characters

from utils import calculate_position, get_character_details, save_image


@pytest.mark.usefixtures("setup")
class TestGoogleImagesPage():

    @allure.description("Save first image and verify locations are the same")
    @allure.title("first image Test")
    @allure.feature("first image")
    @allure.tag("first image")
    def test_tc_01(self):
        # get characters objects
        randomly_two_characters = self.characters

        # get characters details
        characters_data = get_character_details(randomly_two_characters, characters)

        # get position based on id
        position = calculate_position(characters_data["first_character_id"])

        google_page = GooglePage(self.driver)

        google_page.open_google_images() #Open google images
        google_images_page = GoogleImagesPage(self.driver)

        # insert relevant data for first character in the search field
        google_images_page.enter_data(f"'Rick and Morty {characters_data['first_character_name']}")
        google_images_page.click_element(google_images_page.search_button)  # click the search button

        # find all search results
        images_results = google_images_page.find_all_elements(google_images_page.images_results)
        elected_image_by_position = images_results[position - 1]  # reduce 1 in order to click the right picture

        # click the picture based on position
        google_images_page.click_webElement_element(elected_image_by_position)

        # find the opened click picture element
        opened_image = google_images_page.find_element(google_images_page.selected_image)

        # save image in project directory
        save_image(opened_image, characters_data['first_character_name'], characters_data['first_character_id'])

        # assert if locations of both characters are different
        assert characters_data["first_character_location"] == characters_data[
            "second_character_location"], f"{characters_data['first_character_name']} from {characters_data['first_character_location']} and {characters_data['second_character_name']} from {characters_data['second_character_location']}"

        print(f"Both characters are from {characters_data['first_character_name']}.")

    @allure.description("Save second image and verify locations are the same")
    @allure.title("second image Test")
    @allure.feature("second image")
    @allure.tag("second image")
    def test_tc_02(self):
        # get characters objects
        randomly_two_characters = self.characters

        # get characters details
        characters_data = get_character_details(randomly_two_characters, characters)

        # get position based on id
        position = calculate_position(characters_data["second_character_id"])

        google_images_page = GoogleImagesPage(self.driver)

        # insert relevant data for second character in the search field
        google_images_page.enter_data(f"'Rick and Morty {characters_data['second_character_name']}")
        google_images_page.click_element(google_images_page.search_button)  # click the search button

        # find all search results
        images_results = google_images_page.find_all_elements(google_images_page.images_results)
        elected_image_by_position = images_results[position - 1]  # reduce 1 in order to click the right picture

        # click picture based on position
        google_images_page.click_webElement_element(elected_image_by_position)

        # find the opened click picture element
        opened_image = google_images_page.find_element(google_images_page.selected_image)

        # save image in project directory
        save_image(opened_image, characters_data['second_character_name'], characters_data['second_character_id'])

        # assert if locations of both characters are different
        assert characters_data["first_character_location"] == characters_data["second_character_location"], f"{characters_data['first_character_name']} from {characters_data['first_character_location']} and {characters_data['second_character_name']} from {characters_data['second_character_location']}"

        print(f"Both characters are from {characters_data['first_character_name']}.")


