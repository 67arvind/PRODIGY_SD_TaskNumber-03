import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from a file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to a file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact for {name} added.")

def view_contacts(contacts):
    """View all contacts."""
    if contacts:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

def view_contacts_json():
    """View the raw JSON contents of the contacts file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            content = file.read()
            print("\nRaw JSON data from contacts.json:")
            print(content)
    else:
        print("No contacts.json file found.")

def edit_contact(contacts):
    """Edit an existing contact."""
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print(f"Current details - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email address (leave blank to keep current): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email

        print(f"Contact for {name} updated.")
    else:
        print(f"No contact found for {name}.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact for {name} deleted.")
    else:
        print(f"No contact found for {name}.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. View contacts.json file")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            view_contacts_json()
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
