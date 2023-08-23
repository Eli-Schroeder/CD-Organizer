from CD import CD
from menu_util import *


class CDStack:

    def __init__(self, name):
        self.cds = []
        self.name = name

    def open_menu(self):
        while True:
            print("")
            user_input = get_user_selection(self.name, ["Add a CD", "List CDs", "Search for CDs", "Remove a CD", "Exit"])
            if user_input == 1:
                self.add_a_cd()
            elif user_input == 2:
                self.search_cds()
            elif user_input == 3:
                query = input("Search filter: ")
                self.search_cds(query)
            elif user_input == 4:
                self.remove_cds()
            elif user_input == 5:
                break

    def add_a_cd(self):
        name = input("Enter CD name: ")
        artist = input("Enter CD artist: ")
        album = input("Enter CD album (or 'single' if it is a single): ")
        self.cds.append(CD(name, artist, album))
        print("")
        print("CD Added")

    def search_cds(self, query=None):
        print("")
        print("CDs:")
        for n in range(len(self.cds)):
            cd = self.cds[n]
            if query is None or query in cd.__str__():
                print(str(n + 1) + ". " + str(cd))

    def remove_cds(self):
        user_input = get_user_selection("Select a CD to remove:", self.cds)
        del self.cds[user_input - 1]
        print("")
        print("CD Removed")

    def __str__(self):
        return self.name
