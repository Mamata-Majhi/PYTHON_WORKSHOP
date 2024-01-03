# # creating contact class
# class Contact:
#     def __init__(self,name,phone_number,email):
#         # attributes
#         self.name=name
#         self.phone_number=phone_number
#         self.email=email
#     # method for displaying contact details
#     def display(self):
#         print(f"Name={self.name}\nPhoneNumber={self.phone_number}\nEmail={self.email}")


# # creating contactBook class to manage a collection of contacts
# class contactBook:
#     def __init__(self.contacts):
#         self.contacts=contacts
#     # method for adding contacts 
#     def add(self,contacts:list):
#         self.contacts.append(contact)
#         print(f"Contact{contact.name} added successfully.!")


#     def display_contacts(self):
#         print("Contacts:")
#         for contact in self.contacts:
#             # print(f"Name={self.name}\nPhoneNumber={self.phone_number}\nEmail={self.email}")
#             contact.display()
#     def search(self):
#         for contact in self.contacts:
#             if query.lower() in contact.name:
#                 print(f"Name={contact.name}\nPhoneNumber={contact.phone_number}\nEmail={contact.email}")
#                 break



    
# Contact1=Contact(name="Mamata",phone_number=9800984492,email="majhimamata256@gmail.com")
# Contact2=Contact(name="Sahit",phone_number=9804070369,email="majhisahit652@gmail.com")
# contacts=[Mamata,Sahit]
# my_contact_book=contactBook(contacts=contacts)
# my_contact_book.add_contact(Contact1)
# my_contact_book.add_contact(Contact2)

# my_contact_book.display_contacts()
# # Contact1.display()


# creating a contact class
class Contact:
    def __init__(self,name,phone_number,email):
        self.name=name
        self.phone_number=phone_number
        self.email=email
    def display_contact(self):
        print(f"Name={self.name}\nPhone_number={self.phone_number}\nEmail_id={self.email}")

class ContactBook:
    def __init__(self):
        self.contacts=[]
    # method for adding contacts in ContactBook
    def add_contact(self,contact):
        self.contacts.append(contact)
        print(f"Contact{contact.name} added succesfully!")
    # method for displaying all the contacts from the ContactBook
    def display_contacts(self):
        print("Contacts in the ContactBook:")
        for contact in self.contacts:
            contact.display_contact()
    def search_contact_by_name(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():
                print(f"Contact found for name{name}:")
                contact.display_contact()
                return contact
        

        print(f"No contact found for {name}.")
        return None
        


contact1=Contact(name="Mamata Majhi",phone_number=9800984475,email="majhi1254@gmail.com")
contact2=Contact(name="Sahit Majhi",phone_number=9800478955,email="majhi4789@gmail.com")
contact_book=ContactBook()
contact_book.add_contact(contact1)
contact_book.add_contact(contact2)

# displaying all the contacts in the ContactBook
contact_book.display_contacts()

# searching for a contact by 
searched_contact=contact_book.search_contact_by_name("Sahit Majhi")