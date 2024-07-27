class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("-----------------------")

    def search_contact(self, query):
        results = []
        for name, info in self.contacts.items():
            if query.lower() in name.lower() or query in info.values():
                results.append((name, info))
        if results:
            print("Search Results:")
            for name, info in results:
                print(f"Name: {name}")
                print(f"Phone: {info['phone']}")
                print(f"Email: {info['email']}")
                print(f"Address: {info['address']}")
                print("-----------------------")
        else:
            print("No matching contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            if name in contact_book.contacts:
                phone = input("Enter new phone number (leave blank to skip): ")
                email = input("Enter new email address (leave blank to skip): ")
                address = input("Enter new address (leave blank to skip): ")
                contact_book.update_contact(name, phone, email, address)
            else:
                print(f"Contact '{name}' not found.")

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
