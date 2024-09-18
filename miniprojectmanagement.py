def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

contacts = {
    "7731234789": {"name": "Tameka Grant", "email": "tamekagrant@gmail.com", "additional_info": "Friend from school"}
}
import re

def add_contact():
    phone = input("Enter phone number: ")
    if re.fullmatch(r"\d{10}", phone) and phone not in contacts:
        name = input("Enter name: ")
        email = input("Enter email: ")
        additional_info = input("Enter additional information (optional): ")
        contacts[phone] = {"name": name, "email": email, "additional_info": additional_info}
        print("Contact added successfully!")
    else:
        print("Invalid phone number or contact already exists.")

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone in contacts:
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        additional_info = input("Enter additional information: ")
        contacts[phone] = {"name": name, "email": email, "additional_info": additional_info}
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    phone = input("Enter the phone number to search: ")
    if phone in contacts:
        print(f"Name: {contacts[phone]['name']}")
        print(f"Email: {contacts[phone]['email']}")
        print(f"Additional Info: {contacts[phone]['additional_info']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if contacts:
        for phone, info in contacts.items():
            print(f"Phone: {phone}, Name: {info['name']}, Email: {info['email']}, Additional Info: {info['additional_info']}")
    else:
        print("No contacts found.")

def export_contacts():
    with open("contacts.txt", "w") as file:
        for phone, info in contacts.items():
            file.write(f"{phone},{info['name']},{info['email']},{info['additional_info']}\n")
    print("Contacts exported to contacts.txt.")

def import_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                phone, name, email, additional_info = line.strip().split(',')
                contacts[phone] = {"name": name, "email": email, "additional_info": additional_info}
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("contacts.txt not found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
