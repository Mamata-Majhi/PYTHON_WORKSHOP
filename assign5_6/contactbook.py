contact_details = {'Mamata':{'Phone': '9800984492', 'Email': 'majhimam123@gmail.com'}}


def add(name, phone, email):
    contact_details[name] = {'Phone': phone, 'Email': email}
    print(f"Contact {name} added.")

def edit(name, phone, email):
    if name in contact_details:
        contact_details[name] = {'Phone': phone, 'Email': email}
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

def read(name):
    if name in contact_details:
        print(f"Contact Details of {name}:")
        print(f"Phone: {contact_details[name]['Phone']}")
        print(f"Email: {contact_details[name]['Email']}")
    else:
        print(f"Contact {name} not found.")

def delete(name):
    if name in contact_details:
        del contact_details[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

while True:
    print("1. Add")
    print("2. Edit")
    print("3. Read")
    print("4. Delete")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        add(name, phone, email)
    elif choice == "2":
        name = input("Enter contact name to edit: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        edit(name, phone, email)
    elif choice == "3":
        name = input("Enter contact name to read: ")
        read(name)
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        delete(name)
    elif choice == "5":
        break
    else:
        print("Please enter a number between 1 and 5.")