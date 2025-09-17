# 1. Project: Simple Contact Manager 
# Description: 
# A program to store, manage, and search contacts. Users can add, remove, view, and search 
# contacts. All data is stored in a text file for persistence. 
# Requirements: 
# 1. Store contacts in a file (contacts.txt). 
# o Each contact should include: name, phone number, email. 
# 2. Allow the user to: 
# o Add a contact 
# o View all contacts 
# o Search contact by name 
# o Remove a contact 
# o Exit the program 
# 3. Data must persist even after closing the program.


def store_contact():
    contacts = []
    try:
        with open("/Users/adith/OneDrive/Documents/Desktop/www/Python/simpleProject/contactManager/contacts.txt","r") as f:
            for i in f:
                name, phone, email = i.strip().split("|")
                contacts.append({"name":name, "phone":phone, "email":email})
    except FileNotFoundError:
        print("File Not Found")
    return contacts

def save_contacts(contacts):
        with open("/Users/adith/OneDrive/Documents/Desktop/www/Python/simpleProject/contactManager/contacts.txt","w") as f:
            for c in contacts:
                f.write(f"{c['name']}|{c['phone']}|{c['email']}\n")
     
def add_contact(contacts):
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    email = input("Enter your email: ")
    contacts.append({"name":name, "phone":phone, "email":email})
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("Contacts are empty!")
    else:
        print("--All Contacts--")
        i=1
        for c in contacts:
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
            i+=1
        print("_____\n")

def remove_contacts(contacts):
    name = input("Enter the name you wants to remove: ")
    updated_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(updated_contacts) < len(contacts):
        save_contacts(updated_contacts)
        print(" Contact removed successfully!")
    else:
        print("Contact not found.")

def search_contacts(contacts):
    name = input("Enter name to search: ")
    found = [c for c in contacts if c['name'].lower() == name.lower()]
    if found:
        for c in found:
            print(f"Found: {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("Contact not found.")

def contactManage():
    contacts = store_contact()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            remove_contacts(contacts)
            contacts = store_contact()
        elif choice == "5":
            print("See You Again!")
            break
        else:
            print(" Invalid choice, please try again.")
if __name__ == "__main__":
    contactManage()