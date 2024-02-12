#Melissa Smith

#Function showing the goal of the game and move commands
def show_instructions():
   #print a main menu and the commands
   print("Zombie Text Adventure Game")
   print("Collect 6 items to win the game, or be killed by the zombie.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print()


#Function showing players status

def show_status(cur, inventory, rooms):
   #print the player's current status
   #print the current inventory
   #print an item if there is one
   if cur == 'Invalid input':
      print('Invalid input')
   else:
      print('You are in the {}'.format(cur))
   print('Inventory: ', inventory)
   print('-' * 27)
   if cur == 'Bedroom':
      if not rooms['Bedroom']['item'] in inventory:
         print('You see a {}'.format(rooms['Bedroom']['item']))
         print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Bedroom']['item'].lower():
                  inventory.append(rooms['Bedroom']['item'])
                  print('Shield retrieved')
         else:
            print('Invalid input')
      return rooms['Bedroom']['item']
   elif cur == 'Bathroom':
      if not rooms['Bathroom']['item'] in inventory:
         print('You see a {}'.format(rooms['Bathroom']['item']))
         #print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Bathroom']['item'].lower():
                  inventory.append(rooms['Bathroom']['item'])
                  print('Helmet retrieved')
         else:
            print('Invalid input')
      return rooms['Bathroom']['item']
   elif cur == 'Office':
      if not rooms['Office']['item'] in inventory:
         print('You see an {}'.format(rooms['Office']['item']))
         print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Office']['item'].lower():
                  inventory.append(rooms['Office']['item'])
                  print('iPad retrieved')
         else:
            print('Invalid input')
      return rooms['Office']['item']
   elif cur == 'Entryway':
      if not rooms['Entryway']['item'] in inventory:
         print('You see {}'.format(rooms['Entryway']['item']))
         print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Entryway']['item'].lower():
                  inventory.append(rooms['Entryway']['item'])
                  print('Armor retrieved')
         else:
            print('Invalid input')
      return rooms['Entryway']['item']
   elif cur == 'Garage':
      if not rooms['Garage']['item'] in inventory:
         print('You see a {}'.format(rooms['Garage']['item']))
         print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Garage']['item'].lower():
                  inventory.append(rooms['Garage']['item'])
                  print('Gun retrieved')
         else:
            print('Invalid input')
      return rooms['Garage']['item']
   elif cur == 'Kitchen':
      if not rooms['Kitchen']['item'] in inventory:
         print('You see a {}'.format(rooms['Kitchen']['item']))
         print('-' * 27)
         print('Enter your move:')
         item_input = input()
         item_input_string = item_input.split()
         if len(item_input_string) == 2:
            if item_input_string[0] == 'get':
               if item_input_string[1].lower() == rooms['Kitchen']['item'].lower():
                  inventory.append(rooms['Kitchen']['item'])
                  print('Potion retrieved')
         else:
            print('Invalid input')
      return rooms['Kitchen']['item']
   elif cur == 'Dining Room':
      print('You see a {}'.format(rooms['Dining Room']['item']))
      return rooms['Dining Room']['item']
   else:
      return 'Invalid'
# ---- end of show_status ----------

def move_rooms(curr, move):
   if curr == 'Living Room':
      if move == 'south':
         return 'Kitchen'
      elif move == 'north':
         return 'Entryway'
      elif move == 'east':
         return 'Bedroom'
      elif move == 'west':
         return 'Office'
      else:
         return 'Invalid input'
   elif curr == 'Bedroom':
      if move == 'north':
         return 'Bathroom'
      elif move == 'west':
         return 'Living Room'
      else:
         return 'Invalid input'
   elif curr == 'Bathroom':
      if move == 'south':
         return 'Bedroom'
      else:
         return 'Invalid input'
   elif curr == 'Office':
      if move == 'east':
         return 'Living Room'
      else:
         return 'Invalid input'
   elif curr == 'Entryway':
      if move == 'south':
         return 'Living Room'
      elif move == 'east':
         return 'Garage'
      else:
         return 'Invalid input'
   elif curr == 'Garage':
      if move == 'west':
         return 'Entryway'
      else:
         return 'Invalid input'
   elif curr == 'Kitchen':
      if move == 'north':
         return 'Living Room'
      elif move == 'east':
         return 'Dining Room'
      else:
         return 'Invalid input'
   elif curr == 'Dining Room':
      if move == 'west':
         return 'Kitchen'
      else:
         return 'Invalid input'
# --- end of move_rooms ------------


def main():
   #a dictionary linking a room to other rooms
   # and linking one item for each room except the Start room (Living Room) and the room containing the villain
   # define an inventory, which is initially empty
   inventory = []
   rooms = {
      'Living Room': {'south': 'Kitchen', 'north': 'Entryway', 'east': 'Bedroom', 'west': 'Office'},
      'Bedroom': {'north': 'Bathroom', 'west': 'Living Room', 'item': 'Shield'},
      'Bathroom': {'south': 'Bedroom', 'item': 'Helmet'},
      'Office': {'east': 'Living Room', 'item': 'iPad'},
      'Entryway': {'south': 'Living Room', 'east': 'Garage', 'item': 'Armor'},
      'Garage': {'west': 'Entryway', 'item': 'Gun'},
      'Kitchen': {'north': 'Living Room', 'east': 'Dining Room', 'item': 'Potion'},
      'Dining Room': {'west': 'Kitchen', 'item': 'Zombie'}  # villain
   }


   show_instructions()
   # start the player in the Living Room
   current = 'Living Room'

   while True:
      return_val = show_status(current, inventory, rooms)
      if return_val == 'Zombie':
         if len(inventory) == 6:
            print('Congratulations! You have collected all items and defeated the zombie!')
            print('Thanks for playing the game. Hope you enjoyed it!')
            break
         else:
            print('The zombie got you... GAME OVER!')
            print('Thanks for playing the game. Hope you enjoyed it!')
            break
      else:

         #inventory.append(return_val)
         user_move = input('Enter your move:')
         user_move_split = user_move.split()
         if len(user_move_split) == 2:
            if user_move_split[0] == 'go':
               move_response = move_rooms(current, user_move_split[1].lower())
               if move_response == 'Invalid input':
                  print('Invalid input')
               else:
                  current = move_response
         else:
            print('Invalid input')
# --- end of main ------------

if __name__ == '__main__':
   main()







