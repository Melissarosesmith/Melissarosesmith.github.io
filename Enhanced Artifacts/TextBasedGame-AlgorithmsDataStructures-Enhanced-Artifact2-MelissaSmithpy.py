"""
Melissa Smith
Email: mrsmith.121696@gmail.com
CS-499
Algorithms and Data Structures Enhancement
Version 1.2
Date: February 10th, 2024
Purpose: The following program is a text-based adventure game. The player moves through various rooms
collecting the item in each room and adding it to their inventory. If the player reaches the room with the
Zombie before collecting all 6 items, they lose. If the player reaches the room with the Zombie after
collecting all 6 items, they win!
"""


#Function showing the goal of the game and move commands
def show_instructions():
   #print a main menu and the commands
   print("Zombie Text Adventure Game")
   print("Collect 6 items to win the game, or be killed by the zombie.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print()


# This function processes user input to get an item and updates the inventory
def get_item_input(room, item, inventory):
   print(f'You see a {item}')
   print('-' * 27)
   print('Enter your move:')
# The following strips the input, normalizes to lowercase, and splits it for validation.
# The uniform processing aids in optimizing input handling as it avoids case-sensitive comparisons and
# unnecessary whitespace handling.
   item_input = input().strip().lower()
   command, *args = item_input.split()

# Validates the user input; expected command format is 'get <item>'
# This is an O(1) operation because it only checks the first split elements
   if command == 'get' and len(args) == 1 and args[0] == item.lower():
      inventory.append(item)
      print(f'{item.title()} retrieved')
   else:
      print('Invalid input')

# This function shows the player's current status.
# It optimizes algorithmic logic by using the current room (cur) as a dynamic key to access the information
# in the rooms dictionary.
# It also shows efficiency by simplifying the code and making it more scalable if more rooms are added in the future.
def show_status(cur, inventory, rooms):
   if cur == 'Invalid input':
      print('Invalid input')
   else:
      print(f'You are in the {cur}')
      print('Inventory: ', inventory)
      print('-' * 27)
      item = rooms[cur].get('item')
      # Check if the item is present in the room and not already in inventory
      # The 'in' operator has an average case time complexity of O(n) where n is the length of the inventory
      if item and item not in inventory:
         get_item_input(cur, item, inventory)
      return item

# This function checks if a move is valid based on the current room and desired direction
def move_rooms(curr, move, rooms):
   # Check if the move is valid in the current room
   # Dictionary key check is an O(1) operation making this check highly efficient
   if move in rooms[curr]:
      return rooms[curr][move]
   else:
      return 'Invalid input'



def main():
   # A dictionary linking a room to other rooms and items
   # The dictionary structure allows for O(1) time complexity when accessing room and item data,
   # making it an optimal choice for the game's room navigation and item retrieval logic

   inventory = []  # Define an inventory, which is initially empty

   # The rooms dictionary is designed to provide )(1) access to room and item data, which is an efficient way
   # to handle room navigation and item lookup.
   rooms = {
      'Living Room': {'south': 'Kitchen', 'north': 'Entryway', 'east': 'Bedroom', 'west': 'Office', 'item': None},
      'Bedroom': {'south': 'Living Room', 'east': 'Bathroom', 'item': 'Shield'},
      'Bathroom': {'west': 'Bedroom', 'item': 'Helmet'},
      'Office': {'east': 'Living Room', 'item': 'iPad'},
      'Entryway': {'north': 'Living Room', 'west': 'Garage', 'item': 'Armor'},
      'Garage': {'east': 'Entryway', 'item': 'Gun'},
      'Kitchen': {'south': 'Living Room', 'west': 'Dining Room', 'item': 'Potion'},
      'Dining Room': {'east': 'Kitchen', 'item': 'Zombie'}  # villain
   }


   show_instructions()
   # Start the player in the Living Room
   current = 'Living Room'

   #Main game loop
   while True:
      return_val = show_status(current, inventory, rooms)
      if return_val == 'Zombie':
         # Efficiently checking if the player has collected all items is an O(1) operation because it optimizes
         # the stored list length.
         if len(inventory) == 6: # Length check is O(1)
            print('Congratulations! You have collected all items and defeated the zombie!')
            print('Thanks for playing the game. Hope you enjoyed it!')
            break
         else:
            print('The zombie got you... GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it!')
            break
      else:
         # Process player movement
         user_move = input('Enter your move:').strip().lower()
         command, *args = user_move.split()
         # Validate movement input
         # Optimization and efficiency of algorithmic logic by splitting the user input and checking the command
         # is O(1) because it only considers the first element. 
         if command == 'go' and args:
            move_response = move_rooms(current, args[0], rooms)
            if move_response == 'Invalid input':
               print('Invalid input')
            else:
               current = move_response
         else:
            print('Invalid input')

if __name__ == '__main__':
   main()







