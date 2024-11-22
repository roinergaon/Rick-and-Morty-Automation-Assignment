import requests
from API_Rick_and_Morty.Character import Character
from config import API_base_url
import random
from concurrent.futures import ThreadPoolExecutor
def get_all_episodes():
    episodes_response = requests.get(f"{API_base_url}/episode")
    episodes_data = episodes_response.json()
    episodes = episodes_data['results']
    while episodes_data['info']['next']:
        episodes_response = requests.get(episodes_data['info']['next'])
        episodes_data = episodes_response.json()
        episodes.extend(episodes_data['results'])
    return episodes

def get_filtered_random_episode(episodes):
    filtered_episodes = []
    for episode in episodes:
        if len(episode['characters']) >= 30:
            filtered_episodes.append(episode)
    # Randomly select an episode from the filtered list
    selected_episode = random.choice(filtered_episodes)
    return selected_episode

def print_episode_details(selected_episode):
    # 4 Print the episode name and number of characters
    print(f"Selected Episode: {selected_episode['name']}")
    print(f"Number of Characters: {len(selected_episode['characters'])}")

def fetch_character(url):
    return requests.get(url).json()
def fetch_two_characters(character_url):
    characters_obj = []
    with ThreadPoolExecutor() as executor:
        characters = list(executor.map(fetch_character, character_url)) #this for fetching simultaneously.
    for chara in characters:
        character = Character(chara) #save inside an object
        characters_obj.append(character)
    return characters_obj

def create_text_file(characters_obj):
    with open("../characters_introduction.txt", "w") as file: #save the files in the main folder project
        for char in characters_obj:
            file.write(f"Hi! I'm {char.name}, My ID is {char.id}, I'm from {char.location} and I am {char.status}.\n")
