class Person:
    def __init__(self, name: str):
        self.name = name
        self.numbers = []

    def add_number(self, number: str):
        self.numbers.append(number)

    def __str__(self):
        return f"Name: {self.name}, Numbers: {', '.join(self.numbers)}"


class ContactList:
    def __init__(self):
        self.__persons = []

    def add_person(self, person):
        for e in self.__persons:
            if e.name == person.name:
                e.numbers.extend(person.numbers)
                return
        self.__persons.append(person)

    def remove_person(self, person):
        for e in self.__persons:
            if e.name == person.name:
                self.__persons.remove(e)
                return

    def get_numbers(self, person):
        for e in self.__persons:
            if e.name == person.name:
                return e.numbers
        return []

    def get_all_persons(self):
        return self.__persons
