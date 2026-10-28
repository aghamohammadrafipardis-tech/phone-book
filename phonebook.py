# Phone book dictionary
phone_book = {
  "sara": ["09011111111"]
}

# Main menu
menu_text = """
--- Phone Book ---
1- Add contact
2- Add number to contact
3- Search phone number by name
4- Delete contact
5- Number of contacts
6- Exit
"""

# Main loop
while True:
  user_choice = input(menu_text)

  # Exit
  if user_choice == "6" or user_choice == "":
    print("Goodbye")
    break

  result_message = ""

  # Add contact
  if user_choice == "1":
    name = input("Enter the contact name: ")
    if name in phone_book:
      result_message = "A contact with this name already exists"
    else:
      number = input("Enter the phone number: ")
      phone_book[name] = [number]
      result_message = "Contact added successfully"

  # Add number to contact
  elif user_choice == "2":
    name = input("Enter the contact name: ")
    if name not in phone_book:
      result_message = "No contact found with this name"
    else:
      number = input("Enter the new number: ")
      phone_book[name].append(number)
      result_message = "New number added"

  # Search by name
  elif user_choice == "3":
    name = input("Enter the contact name: ")
    if name in phone_book:
      result_message = str(phone_book[name])
    else:
      result_message = "No contact found with this name"

  # Delete contact
  elif user_choice == "4":
    name = input("Enter the contact name: ")
    if name in phone_book:
      del phone_book[name]
      result_message = "Contact deleted"
    else:
      result_message = "No contact found with this name"

  # Count contacts
  elif user_choice == "5":
    result_message = f"Number of contacts: {len(phone_book)}"

  # Invalid input
  else:
    result_message = "Input must be a value between 1 and 6"

  # Ask to continue
  result_message += " - Do you want to continue? (yes/no)"
  cont = input(result_message)
  if cont == "no" or cont == "":
    print("Goodbye")
    break