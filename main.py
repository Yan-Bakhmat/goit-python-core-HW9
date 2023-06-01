CONTACTS = {}


def hello():
    return 'How can I help you?'


def add_or_change_contact(name_and_number):
    name_and_number = name_and_number.split(' ')
    CONTACTS[name_and_number[0]] = name_and_number[1]
    return "Done!"


def show_number(name):
    return CONTACTS[name]


def show_all(contacts):
    if contacts:
        for name, number in contacts.items():
            yield f'{name}: {number}'
    else:
        return 'The contact list is empty.'


def close():
    return "Good bye!"


def input_error(func):
    def inner():
        try:
            func()
        except IndexError:
            print('Enter the name and number separated by a space.')
        except KeyError:
            print("The contact is missing.")
        result = func()
        return result
    return inner


@ input_error
def main():
    bot_status = True
    while bot_status:
        command = input('Enter the command: ').lower()
        if command == 'hello':
            print(hello())
        elif 'add' in command:
            print(add_or_change_contact(
                command.removeprefix('add ')))
        elif "change" in command:
            print(add_or_change_contact(
                command.removeprefix('change ')))
        elif "phone" in command:
            print(show_number(command.removeprefix("phone ")))
        elif command == "show all":
            for contact in show_all(CONTACTS):
                print(contact)
        elif command in ("good bye", "close", "exit"):
            print(close())
            bot_status = False
        else:
            print("Enter correct command, please.")


main()
