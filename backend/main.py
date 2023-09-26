from components.contact_list_app import ContactListApp
from components.contact import Person

if __name__ == "__main__":
    pb_app = ContactListApp("./data/contacts.json")
    pb_app.load_contacts_from_file()

    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View All Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            person = Person(name)
            person.add_number(number)
            pb_app.add_person(person)
            print("Contact added successfully.")

        elif choice == "2":
            name = input("Enter name of contact to remove: ")
            person = Person(name)
            pb_app.remove_person(person)
            print("Contact removed successfully.")

        elif choice == "3":
            contacts = pb_app.get_all_persons()
            if not contacts:
                print("Contact list is empty.")
            else:
                for contact in contacts:
                    print(f"Name: {contact.name:<20} Numbers: {', '.join(contact.numbers)}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
