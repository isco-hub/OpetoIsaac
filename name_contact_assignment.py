class ContactManager:
    def __init__(self):
        self.contacts = []

    def _validate_phone(self, phone):
        if not phone:
            return True
        allowed = set("0123456789-+")
        if not all(c in allowed for c in phone):
            print("Error: Phone number can only contain digits, hyphens, and '+'.")
            return False
        return True

    def _validate_email(self, email):
        if not email:
            return True
        if "@" not in email or "." not in email:
            print("Error: Email must contain '@' and '.'.")
            return False
        return True

    def add_contact(self, name, phone, email=""):
        if not self._validate_phone(phone):
            return
        if not self._validate_email(email):
            return
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contact(self, name):
        for c in self.contacts:
            if c["name"].lower() == name.lower():
                print(f"Name : {c['name']}")
                print(f"Phone: {c['phone']}")
                print(f"Email: {c['email']}")
                return
        print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone=None, email=None):
        for c in self.contacts:
            if c["name"].lower() == name.lower():
                if phone is not None:
                    if not self._validate_phone(phone):
                        return
                    c["phone"] = phone
                if email is not None:
                    if not self._validate_email(email):
                        return
                    c["email"] = email
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for i, c in enumerate(self.contacts):
            if c["name"].lower() == name.lower():
                del self.contacts[i]
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

    def search_contacts(self, keyword):
        keyword_lower = keyword.lower()
        results = [c for c in self.contacts if keyword_lower in c["name"].lower()
                   or keyword_lower in c["phone"]
                   or keyword_lower in c["email"].lower()]
        if not results:
            print("No contacts found matching your search.")
            return
        print(f"\n{'='*40}")
        print(f"Search Results ({len(results)} found):")
        print(f"{'='*40}")
        for i, c in enumerate(results, 1):
            print(f"{i}. {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")
            print("-" * 40)

    def list_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print(f"\n{'='*40}")
        print(f"All Contacts ({len(self.contacts)} total):")
        print(f"{'='*40}")
        for i, c in enumerate(self.contacts, 1):
            print(f"{i}. {c['name']}")
            print(f"   Phone: {c['phone']}")
            print(f"   Email: {c['email']}")
            print("-" * 40)


def main():
    cm = ContactManager()
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email (optional): ").strip()
            cm.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to view: ").strip()
            cm.view_contact(name)

        elif choice == "3":
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone (leave blank to keep): ").strip()
            email = input("Enter new email (leave blank to keep): ").strip()
            cm.update_contact(name, phone or None, email or None)

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            cm.delete_contact(name)

        elif choice == "5":
            keyword = input("Enter search keyword: ").strip()
            cm.search_contacts(keyword)

        elif choice == "6":
            cm.list_all_contacts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
