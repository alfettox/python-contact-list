class ContactList:
    def __init__(self):
        self.__persons = []

    def add_number(self, name:str, number:str):
        pass

    def remove_number(self, name:str, number:str):
        pass

    def get_numbers(self, name: str):
        pass

    def get_all_numbers(self):
        return self
    
class Persons:
    def __init__(self):
        self

    
pb = ContactList()

pb.add_number("Giovanni", "514-953-2514")
pb.add_number("Alessio", "514-923-123")
pb.add_number("Nicolo", "514-133-2513")

print(pb.get_all_numbers())

