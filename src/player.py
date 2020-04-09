# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def pickup_item(self, item):
        self.items.append(item)
        self.current_room.picked_item(item)
        print(f"Picked up {item.description}")

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.add_item(item)
        print(f"Dropped {item.description}")

    def command(self, command):

        # Take/Drop commands
        x = command.split()
        if x[0] == "take":
            for item in self.current_room.items:
                if item.name == x[1]:
                    self.pickup_item(item)
        elif x[0] == "drop":
            for item in self.items:
                if item.name == x[1]:
                    self.drop_item(item)

        # Directional Commands
        elif command == "n":
            if self.current_room.n_to is not None:
                self.current_room = self.current_room.n_to
            else:
                print("Can't go this way")
        elif command == "s":
            if self.current_room.s_to is not None:
                self.current_room = self.current_room.s_to
            else:
                print("Can't go this way")
        elif command == "e":
            if self.current_room.e_to is not None:
                self.current_room = self.current_room.e_to
            else:
                print("Can't go this way")
        elif command == "w":
            if self.current_room.w_to is not None:
                self.current_room = self.current_room.w_to
            else:
                print("Can't go this way")

        # Help commands
        elif command == "q":
            print("Goodbye!")
            exit()
        elif command == "i":
            print("My items:")
            for item in self.items:
                print(f"-- {item}")
        else:
            print("**Please input n,s,e,w to move a direction or q to quit"
                  "\n**To perform an action, type take or drop followed by item name"
                  "\n**To view your items, type i"
                  "\n--------------------------------")
