import json
class FileHandler:
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        data = []
        try:
            with open(self.__filename, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            pass
        return data

    def save_person(self, person):
        data = self.load_file()
        data.append({"name": person.name, "numbers": person.numbers})
        with open(self.__filename, 'w') as file:
            json.dump(data, file, indent=4)

    def remove_person(self, person):
        data = self.load_file()
        updated_data = [entry for entry in data if entry["name"] != person.name]
        with open(self.__filename, 'w') as file:
            json.dump(updated_data, file, indent=4)
