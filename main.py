FILE = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    with open(FILE, "a") as f:
        f.write(name + "," + phone + "\n")
    print("Contact Saved!")

def view_contacts():
    try:
        with open(FILE, "r") as f:
            data = f.readlines()
            if not data:
                print("No contacts found.")
            else:
                print("\n--- CONTACT LIST ---")
                for line in data:
                    name, phone = line.strip().split(",")
                    print(f"Name: {name} | Phone: {phone}")
    except:
        print("No contacts found.")

def search_contact():
    search = input("Enter name to search: ").lower()
    found = False
    with open(FILE, "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            if search in name.lower():
                print(f"Found → {name}: {phone}")
                found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    name_delete = input("Enter name to delete: ").lower()
    lines = []
    deleted = False

    with open(FILE, "r") as f:
        lines = f.readlines()

    with open(FILE, "w") as f:
        for line in lines:
            name, phone = line.strip().split(",")
            if name.lower() != name_delete:
                f.write(line)
            else:
                deleted = True

    if deleted:
        print("Contact Deleted!")
    else:
        print("Contact not found.")

while True:
    print("\n==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")