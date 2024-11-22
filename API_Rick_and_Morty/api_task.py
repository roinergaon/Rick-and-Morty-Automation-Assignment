import random
from API_Rick_and_Morty.api_utils import get_all_episodes, get_filtered_random_episode, print_episode_details, fetch_two_characters, \
    create_text_file

def run_api_task():

    # 1,2 Fetch all episodes.
    episodes = get_all_episodes()

    #3,4 Randomly choose one episode from the list where the number of characters exceeds or equal 30 and print details.
    selected_episode = get_filtered_random_episode(episodes)
    print_episode_details(selected_episode)

    # 5 Randomly select two characters from the episode and store them as character objects (see inside))
    character_url = random.sample(selected_episode['characters'], 2)
    characters_obj = fetch_two_characters(character_url) #fetch_two_characters and return objects

    # 6. Write introductions to a file\
    create_text_file(characters_obj)

    return characters_obj





