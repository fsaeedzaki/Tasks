Contacts = []

def Addc():
    Name = input("Enter name: ")
    Phone = input("Enter phone number: ")
    Email = input("Enter email address: ")
    Contact = {
        'Name': Name,
        'Phone': Phone,
        'Email': Email,
    }
    Contacts.append(Contact)
    print("Contact added successfully!\n")

def Viewc():
    for i, Contact in Contacts:
        print(f"{i}. {Contact['name']} - {Contact['phone']} - {Contact['email']}")
    print()

def Searchc():
    Search = input("Search your contact (by name or phone number): ").lower()
    for Contact in Contacts:
        if Search in Contact['name'].lower() or Search in Contact['phone']:
            print(f"{Contact['name']} - {Contact['phone']} - {Contact['email']}")
            Found = True
    if not Found:
        print("No matching contact found. :(\n")

def Deletec():
    Name = input("Enter the name of the contact to delete: ").lower()
    for Contact in Contacts:
        if Contact['name'].lower() == Name:
            Contacts.remove(Contact)
            print("Contact deleted successfully.\n")
            return
    print("Contact not found. :(\n")

def Updatec():
    Name = input("Enter the name of the contact to update: ").lower()
    for Contact in Contacts:
        if Contact['name'].lower() == Name:
            newname = input(f"New name ({Contact['name']}): ") or Contact['name']
            newphone = input(f"New phone ({Contact['phone']}): ") or Contact['phone']
            newemail = input(f"New email ({Contact['email']}): ") or Contact['email']
            Contact['name'] = newname
            Contact['phone'] = newphone
            Contact['email'] = newemail
            print("Contact updated successfully!\n")
            return
    print("Contact not found. :(\n")

def Togglef():
    Name = input("Enter the name of the contact to mark or unmark as favorite: ").lower()
    for Contact in Contacts:
        if Contact['name'].lower() == Name:
            Contact['favorite'] = not Contact['favorite']
            Markornot = "marked as favorite" if Contact['favorite'] else "removed from favorites"
            print(f"{Contact['name']} has been {Markornot}.\n")
            return
    print("Contact not found. :(\n")

def Viewf():
    Favs = [c for c in Contacts if c['favorite']]
    if not Favs:
        print("No favorite contacts. :(\n")
        return
    for Contact in Favs:
        print(f"{Contact['name']} - {Contact['phone']} - {Contact['email']}")

while True:
    print("(づ｡◕‿‿◕｡)づ Contact management! ٩(˘◡˘)۶")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Update a Contact")
    print("6. Mark/Unmark Favorite Contact")
    print("7. View Favorite Contacts")
    print("8. Exit")
    Choice = input("Choose an option! (1-8): ")
        
    if Choice == '1':
            Addc()
    elif Choice == '2':
            Viewc()
    elif Choice == '3':
            Searchc()
    elif Choice == '4':
            Deletec()
    elif Choice == '5':
            Updatec()
    elif Choice == '6':
            Togglef()
    elif Choice == '7':
            Viewf()
    elif Choice == '8':
           print("Exiting program. :(")
 