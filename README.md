def welcome():
  """Prints a welcome message and the menu options."""
  print("Welcome to the Contact Management System!")
  print("""
Menu:
  1. Add a new contact
  2. Edit an existing contact
  3. Delete a contact
  4. Search for a contact
  5. Display all contacts
  6. Export contacts to a text file
  7. Import contacts from a text file
  8. Quit
  """)

def get_contacts():
  """Loads contacts from a file or creates an empty dictionary if file is not found."""
  try:
    with open("contacts.txt", "r") as file:
      return eval(file.read())
  except FileNotFoundError:
    return {}

def save_contacts(contacts):
  """Saves contacts to a text file."""
  with open("contacts.txt", "w") as file:
    file.write(str(contacts))

# Functions for adding, editing, deleting, searching, displaying, exporting, and importing contacts (implementation details omitted for brevity)

def main():
  """The main function that drives the program."""
  contacts = get_contacts()
  while True:
    welcome()
    choice = input("Enter your choice: ")
    if choice == "1":
      add_contact(contacts)
    elif choice == "2":
      edit_contact(contacts)
    elif choice == "3":
      delete_contact(contacts)
    elif choice == "4":
      search_contact(contacts)
    elif choice == "5":
      display_contacts(contacts)
    elif choice == "6":
      export_contacts(contacts)
    elif choice == "7":
      import_contacts(contacts)
    elif choice == "8":
      save_contacts(contacts)
      print("Exiting Contact Management System...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
  
