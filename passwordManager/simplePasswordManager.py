# 3. Simple Password Manager 

# o View credentials for a specific website 
# o View all stored credentials 
# o Exit the program 
# 3. Data must be persistent even after the program closes. 
# 4. No encryption is required (simple plain-text storage). 

passwordFile  = "/Users/adith/OneDrive/Documents/Desktop/www/Python/simpleProject/passwordManager/passwords.txt"

def load_credentials():
    credentials = []
    try:
        with open(passwordFile ,"r") as f:
            for i in f:
                website, username, password = i.strip().split("|")
                credentials.append({"website":website, "username":username, "password":password})
    except FileNotFoundError:
        print("File not found")
    return credentials

def save_credentials(credentials):
    with open(passwordFile, "a") as f:
        for i in credentials:
            f.write(f"{i['website']}|{i['username']}|{i['password']}\n")

def add_credentials(credentials):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    credentials.append({"website":website, "username":username, "password":password})
    save_credentials(credentials)
    print("Credentials saved successfully!")

def view_credentials(credentials):
    website = input("Enter website to search: ").lower()
    for i in credentials:
        if i["website"].lower() == website:
            print(f"Website: {i['website']}, Username: {i['username']}, Password: {i['password']}")
            return
def view_credentials(credentials):
    website = input("Enter website to search: ").lower()
    for i in credentials:
        if i["website"].lower() == website:
            print(f"Website: {i['website']}, Username: {i['username']}, Password: {i['password']}")
            return
    print(" No credentials found for that website.")
def view_all(credentials):
    if not credentials:
        print("No credentials stored yet.")
        return
    for c in credentials:
        print(f"Website: {c['website']}, Username: {c['username']}, Password: {c['password']}")
def main():
    credentials = load_credentials()
    while True:
        print("\n--- Password Manager ---")
        print("1. Add New Credentials")
        print("2. View Credentials for a Website")
        print("3. View All Credentials")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_credentials(credentials)
        elif choice == "2":
            view_credentials(credentials)
        elif choice == "3":
            view_all(credentials)
        elif choice == "4":
            print("Exiting... Goodbye! ")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
