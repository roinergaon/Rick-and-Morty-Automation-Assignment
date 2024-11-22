import os
import time
from datetime import datetime
import allure
import requests


def calculate_position(character_id):
    #Calculate the position based on the character ID

    char_id_str = str(character_id)
    if len(char_id_str) == 3:
        hundreds = int(char_id_str[0])  # First digit
        ones = int(char_id_str[2])  # Third digit
        position = hundreds + ones
    elif len(char_id_str) == 2:
        tens = int(char_id_str[0])  # First digit
        ones = int(char_id_str[1])  # Second digit
        position = tens + ones
    elif len(char_id_str) == 1:
        ones = int(char_id_str[0])  # First digit only if the ID has only 1 digit
        position = ones
    else:
        raise ValueError("ID doesn't have 1,2 or 3 digits")

    return position


def save_image(opened_image, name , id):
    image_url = opened_image.get_attribute("src")
    # Download the image
    response = requests.get(image_url)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{id}_{timestamp}.jpg"
    save_path = os.path.join("..", "..", filename)  # Navigate two folders up
    # Save the image
    with open(save_path, "wb") as file:
        file.write(response.content)

    # Attach the saved image to the Allure report
    with open(save_path, "rb") as file:
        allure.attach(file.read(), name=f"f{name}_{id}", attachment_type=allure.attachment_type.PNG)


def get_character_details(randomly_two_characters, characters):
    first_character_name = randomly_two_characters[characters["First_character"]].name
    first_character_location = randomly_two_characters[characters["First_character"]].location
    first_character_id = randomly_two_characters[characters["First_character"]].id
    second_character_name = randomly_two_characters[characters["Second_character"]].name
    second_character_location = randomly_two_characters[characters["Second_character"]].location
    second_character_id = randomly_two_characters[characters["Second_character"]].id

    return {
        "first_character_name": first_character_name,
        "first_character_location": first_character_location,
        "first_character_id": first_character_id,
        "second_character_name": second_character_name,
        "second_character_location": second_character_location,
        "second_character_id": second_character_id,
    }

def highlight(element, driver, duration=0.5):
    """Highlight"""
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(duration)
    apply_style(original_style)
