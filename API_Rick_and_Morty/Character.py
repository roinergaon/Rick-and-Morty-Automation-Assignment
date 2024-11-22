class Character:
    def __init__(self, char_data):
        self.id = char_data['id']
        self.name = char_data['name']
        self.status = char_data['status']
        self.species = char_data['species']
        self.location = char_data['location']['name']