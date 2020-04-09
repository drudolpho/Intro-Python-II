from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Items

items = {
    "sword": Item("sword", "a decent weapon"),
    "bread": Item("bread", "a small piece of bread"),
    "coin": Item("coin", "a shiny coin")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room["outside"].add_item(items["sword"])
room["foyer"].add_item(items["bread"])
room["narrow"].add_item(items["coin"])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Dennis", room["outside"])

# Write a loop that:

# Loop
while True:
    # Print
    print(f"\n{player.name}: {player.current_room}")
    player.current_room.print_room_info()

    # Read
    cmd = input("~~> ")
    # Eval
    player.command(cmd)



#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



# Create a file called item.py and add an Item class in there.
#
# The item should have name and description attributes.
#
# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.
#
# Add the ability to add items to rooms.
#
# The Room class should be extended with a list that holds the Items that are currently in that room.
#
# Add functionality to the main loop that prints out all the items that are visible to the player when they are in that room.
#
# Add capability to add Items to the player's inventory. The inventory can also be a list of items "in" the player, similar to how Items can be in a Room.
#
# Add a new type of sentence the parser can understand: two words.
#
# Until now, the parser could just understand one sentence form:
#
# verb
#
# such as "n" or "q".
#
# But now we want to add the form:
#
# verb object
#
# such as "take coins" or "drop sword".
#
# Split the entered command and see if it has 1 or 2 words in it to determine if it's the first or second form.
#
# Implement support for the verb get followed by an Item name. This will be used to pick up Items.
#
# If the user enters get or take followed by an Item name, look at the contents of the current Room to see if the item is there.
#
# If it is there, remove it from the Room contents, and add it to the Player contents.
#
# If it's not there, print an error message telling the user so.
#
# Add an on_take method to Item.
#
# Call this method when the Item is picked up by the player.
#
# on_take should print out "You have picked up [NAME]" when you pick up an item.
#
# The Item can use this to run additional code when it is picked up.
#
# Add an on_drop method to Item. Implement it similar to on_take.
#
# Implement support for the verb drop followed by an Item name. This is the opposite of get/take.
#
# Add the i and inventory commands that both show a list of items currently carried by the player.