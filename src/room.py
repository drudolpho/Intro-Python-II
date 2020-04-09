# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        return f"{self.name}"

    def print_room_info(self):
        print(f"{self.description}")
        self.print_items()

    def print_items(self):
        if len(self.items) == 0:
            print("\nThere is nothing here")
            return
        else:
            print("\nThere is something here")
            for item in self.items:
                print(f"- {item}")
            return

    def add_item(self, item):
        self.items.append(item)

    def picked_item(self, item_to_remove):
        for item in self.items:
            if item == item_to_remove:
                item = self.items.remove(item)
                return item
            else:
                print("This item is not here")

