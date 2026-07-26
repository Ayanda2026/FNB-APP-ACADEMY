contacts = []

def add_contacts():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    New_contacts = { 
       "name": name,
       "phone": phone,
       "email": email
    }

contacts.append(new_contacts)
print("Contacts added successfully!")

add_contacts()





def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
        return None
    



def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact.remove(contact)
            print("Contact deleted successfully!")
            return
        
        print ("Contact not found.") 




        def view_all():

            if len(contact) == 0:
                print("No contact found.")
            else: 
                print("\n--- Contact List ---")
                for contact in contacts:
                    print(f"Name : {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print("-" * 20)



                    while True:
                     print("\nContact Book")
                     print("1. Add Contact")
                     print("2. Search Contact")
                     print("3. Delete Contact")
                     print("4. View Contact")
                     print("5. Exit")

                    choice = input("Choose an option: ")

                    if choice == "1":
                        add_contact()

                    elif choice == "2":
                        name = input("Enter name to search: ")
                        result = search_contact(name)

                        if result: 
                            print("Contact found")
                            print(f"Name : {result['name']}")
                            print(f"phone: {result['phone']}")
                            print(f"Email: {result['email']}")



                        else:
                            print("Contact not found")

                    elif choice == "3":
                              
                              name = input("Enter name to delete ")
                              delete_contact(name)

                    elif choice == "4":
                          view_all()  
                         
                    elif  choice == "5":   
                          print("Goodbye!")
                          break

                    else:
                         print("Invalid choice. Please try again.")
                         

                    
        
