from cd_stack import *
from menu_util import *

# TODO:
# - implement multiple CD stacks.
# - implement creating new CD stack
# - implement deleting a CD stack
# - implement listing CD stacks
# - implement selecting a CD stack to open

cds_stacks = []


def main_menu():
    while True:
        user_input = get_user_selection("CD Organizer", [
            "Create a CD stack",
            "Manage a CD stack",
            "List CD stacks",
            "Delete a CD stack",
            "Exit"
        ])
        if user_input == 1:
            add_cd_stack()
        elif user_input == 2:
            manage_cd_stack()
        elif user_input == 3:
            pass
        elif user_input == 4:
            pass
        elif user_input == 5:
            break
        print(cds_stacks)


def add_cd_stack():
    name = input("What is the name of your CD Stack?")
    cds_stacks.append(CDStack(name))


def manage_cd_stack():
    user_input = get_user_selection("Which CD stack do you want to manage?", cds_stacks)
    cds_stacks[user_input - 1].open_menu()


if __name__ == '__main__':
    main_menu()
