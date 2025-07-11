contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Phone: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
    choice = input("Choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")

