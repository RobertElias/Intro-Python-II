from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Please enter your name: '), room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(player.current_room.name)
    print(player.current_room.description)

    command = input('\nEnter a direction or press "q" to quit + "Enter" to leave: \n')

    if command == 'q':
        print("Goodbye!")
        exit(0)
    
    elif command == 'n':
        # this is north
        if player.current_room.n_to is not None:
            player.current_room = player.current_room.n_to
        else:
            print('You seem to be going in the wrong direction')
    
    
    elif command == 's':
        # this is north
        if player.current_room.s_to is not None:
            player.current_room = player.current_room.s_to
        else:
            print('You seem to be going in the wrong direction')
    
    elif command == 'e':
        # this is north
        if player.current_room.e_to is not None:
            player.current_room = player.current_room.e_to
        else:
            print('You seem to be going in the wrong direction')
    
    elif command == 'w':
        # this is north
        if player.current_room.w_to is not None:
            player.current_room = player.current_room.w_to
        else:
            print('You seem to be going in the wrong direction')
    else:
        print('Please make a different selection')

try: 
    player.current_room = getattr(player.current_room)

except AttributeError:
    print('You are unable to enter!!!')
