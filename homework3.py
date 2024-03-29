def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def birthdays(contacts):
        today = datetime.now()
        one_week_later = today + timedelta(days=7)
        upcoming_birthdays = []

        for name, info in contacts.items():
            if 'birthday' in info:
                birthday_date = datetime.strptime(info['birthday'], "%d.%m.%Y")
                if today <= birthday_date <= one_week_later:
                    upcoming_birthdays.append((name, info['birthday']))
    
        if upcoming_birthdays:
            return '\n'.join([f"{name}: {birthday}" for name, birthday in upcoming_birthdays])
        else:
            return "No birthdays within the next week."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f'{name} was changed {phone}'
    return "Contact not found"

def add_birthday(self, birthday):
    self.birthday = Birthday(birthday)

def show_birthday(self):
    return str(self.birthday)

def show_phone(args, contacts):
    name, *_ = args
    return contacts.get(name, 'Contact not found')
    
def show_all(args, contacts):
    contact = ""
    for name,phone in contacts.items():
        contact += f'{name} {phone}\n'
    return contact
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "add-birthday":
            name, birthday = args
            print(add_birthday(name, birthday, contacts))
        elif command == "show-birthday":
            name = args[0]
            print(show_birthday(name, contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value
        
    def __str__(self):
        return str(self.value)

    def is_valid(self, value):
        return True

class Name(Field):
    pass

class Phone(Field):
    def is_valid(self, value):
        return len(value) == 10 and value.isdigit()
    
class Birthday(Field):
    def is_valid(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
            return True
        except ValueError:
            return False
        
class Record(Birthday):
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def find_phone(self, number: str) -> Phone:
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None
    
    def add_phone(self, number):
        phone = Phone(number)
        self.phones.append(phone)
        return phone

    def remove_phone(self, number):
        phone = self.find_phone(number)
        if not phone:
            raise ValueError
        self.phones.remove(phone)

    def add_birthday(name, birthday, contacts):
        if name in contacts:
            contacts[name]['birthday'] = birthday
            return "Birthday added."
        else:
            return "Contact not found."

    def show_birthday(name, contacts):
        if name in contacts and 'birthday' in contacts[name]:
            return contacts[name]['birthday']
        else:
            return "Birthday not found."

    def edit_phone(self, oldnumber, newnumber):
        if self.find_phone(oldnumber):
            self.add_phone(newnumber)
            self.remove_phone(oldnumber)
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Record:
        return self.data.get(name, None)
    
    def delete(self, name: str) -> Record:
        return self.data.pop(name, None)
    
    def get_birthdays_per_week(self):
        today = datetime.now()

    def __str__(self):
        result = ""
        for record in self.data.values():
            result += f'{str(record)}\n'
        return result