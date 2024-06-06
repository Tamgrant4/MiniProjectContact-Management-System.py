def display_menu():
  print("\nWelcome to the Contact Management System!")
  print("Menu:")
  print("1. Add a new contact")
  print("2. Edit an existing contact")
  print("3. Delete a contact")
  print("4. Search for a contact")
  print("5. Display all contacts")
  print("6. Export contacts to a text file")
  print("7. Import contacts from a text file")
  print("8. Quit")

import re

def get_user_input(message):
  while True:
    user_input = input(message)
    if user_input.strip():  # Check for empty input
      return user_input
    else:
      print("Invalid input. Please enter a value.")

def validate_phone(phone_number):
  pattern = r"^\d{3}-\d{3}-\d{4}$"  # Example phone number format (XXX-XXX-XXXX)
  if re.match(pattern, phone_number):
    return phone_number
  else:
    print("Invalid phone number format. Please use XXX-XXX-XXXX")
    return None

def validate_email(email):
  pattern = r"^[^@]+@[^@]+\.[^@]+$"  # Basic email format validation
  if re.match(pattern, email):
    return email
  else:
    print("Invalid email format. Please use a valid email address.")
    return None

