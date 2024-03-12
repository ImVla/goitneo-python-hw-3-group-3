from datetime import datetime, timedelta
from collections import UserDict

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, args

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid phone number: {value}")
        super().__init__(value)

    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()

class Birthday(Field):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError(f"Invalid date format: {value}")
        super().__init__(value)

    def is_valid(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            return False

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phone = Phone(phone) if phone else None
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

class AddressBook(UserDict):
    def add_record(self, name, phone=None, birthday=None):
        self.data[name] = Record(name, phone, birthday)

    def change_phone(self, name, new_phone):
        if name in self.data:
            self.data[name].add_phone(new_phone)
            return True
        return False

    def get_phone(self, name):
        if name in self.data and self.data[name].phone:
            return self.data[name].phone.value
        return "Contact not found"

    def add_birthday(self, name, birthday):
        if name in self.data:
            self.data[name].add_birthday(birthday)
            return True
        return False

    def get_birthday(self, name):
        if name in self.data and self.data[name].birthday:
            return self.data[name].birthday.value
        return "Birthday not found"

    def upcoming_birthdays(self):
        upcoming = []
        today = datetime.now()
        one_week_later = today + timedelta(days=7)
        for name, record in self.data.items():
            if record.birthday:
                birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                this_year_birthday = birthday_date.replace(year=today.year)
                if today <= this_year_birthday <= one_week_later:
                    upcoming.append((name, record.birthday.value))
        return upcoming

    def show_all_contacts(self):
        return "\n".join([f"{name}: {record.phone.value if record.phone else 'No phone'}" for name, record in self.data.items()])

def main():
    book = AddressBook()
    print("Welcome to the contact management bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) >= 2:
                book.add_record(*args[:2])
                print(f"Contact {args[0]} added.")
            else:
                print("Insufficient arguments.")
        elif command == "change":
            if len(args) >= 2 and book.change_phone(*args[:2]):
                print(f"Phone for {args[0]} changed.")
            else:
                print("Contact not found or insufficient arguments.")
        elif command == "phone":
            print(book.get_phone(args[0]) if args else "Contact name required.")
        elif command == "all":
            print(book.show_all_contacts())
        elif command == "add-birthday":
            if len(args) >= 2 and book.add_birthday(*args[:2]):
                print(f"Birthday for {args[0]} added.")
            else:
                print("Contact not found or insufficient arguments.")
        elif command == "show-birthday":
            print(book.get_birthday(args[0]) if args else "Contact name required.")
        elif command == "birthdays":
            birthdays = book.upcoming_birthdays()
            if birthdays:
                for name, date in birthdays:
                    print(f"{name}: {date}")
            else:
                print("No birthdays within the next week.")

if __name__ == "__main__":
    main()