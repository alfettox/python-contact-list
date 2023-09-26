import csv,json

from components.contact import Person, ContactList
from components.file_handler import FileHandler

class ContactListApp:
    def __init__(self, filename):
        self.__phonebook = ContactList()
        self.__filehandler = FileHandler(filename)

    def load_contacts_from_file(self):
        data = self.__filehandler.load_file()
        for entry in data:
            name = entry["name"]
            numbers = entry["numbers"]
            person = Person(name)
            for n in numbers:
                person.add_number(n)
            self.__phonebook.add_person(person)

    def add_person(self, person):
        self.__phonebook.add_person(person)
        self.__filehandler.save_person(person)

    def remove_person(self, person):
        self.__phonebook.remove_person(person)
        self.__filehandler.remove_person(person)

    def get_numbers(self, person):
        numbers = self.__phonebook.get_numbers(person)
        if numbers is not None:
            return numbers
        else:
            return []

    def get_all_persons(self):
        return self.__phonebook.get_all_persons()
