CONTACTS = {}


def add_or_change_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    CONTACTS[name_and_number[0]] = name_and_number[1]
    return "Done"


def show_number(name):
    return CONTACTS[name]


def show_all(contacts):
    for name, number in contacts.items():
        yield f'{name}: {number}\n'


def input_error(func):
    def inner():
        pass
    return inner


@input_error
def main():
    bot_status = True
    while bot_status:
        command = input('Enter the command: ').lower()
        if command == 'hellow':
            print('How can I help you?')
        elif ('add' or "change") in command:
            print(add_or_change_contact(
                command.removeprefix('add ').removeprefix('change ')))
        elif "phone" in command:
            print(show_number(command.removeprefix("phone ")))
        elif command == "show all":
            for i in show_all(contacts):
                print()
        elif command in ("good bye", "close", "exit"):
            print("Good bye!")
            bot_status = False
