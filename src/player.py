# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, command):
        if command == "n":
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
        elif command == "q":
            print("Goodbye!")
            exit()
        else:
            print("Please input n,s,e,w to move a direction or q to quit")