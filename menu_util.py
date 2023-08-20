
def get_user_selection(prompt, options):
    print(prompt)
    for x in range(len(options)):
        print(str(x + 1) + ". " + str(options[x]))
    selection = input("selection: ")
    try:
        selection = int(selection)
    except ValueError:
        print("Invalid selection. Please enter a number corresponding to your selection.")
        print("")
        return get_user_selection(prompt, options)
    if selection < 1 or selection > len(options):
        print("Invalid selection. Please enter a number corresponding to your selection.")
        print("")
        return get_user_selection(prompt, options)
    return selection
