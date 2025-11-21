#Harlin Debien


  # Create a main menu and gameplay instructions
def show_instructions():
    print('Novascape Text Adventure Game')
    print('Enter the escape pod with all items or die to NOVA.')
    print('Move commands: go South, go North, go East, go West')
    print('Add to Inventory: get "item name"')
    print('Type "Exit" to quit the game')

def show_status(current_room, inventory, rooms):

    print('\nYou are in', current_room)
    print('Inventory:', inventory)

    # Check if there is an item in the room
    if 'item' in rooms[current_room]:
        print('You see a ', rooms[current_room]['item'])
    else:
        print("There are no items here.")

    # Check if the villain is in the room
    if 'villain' in rooms[current_room]:
        print("WARNING! The villain is here!")
        print("GAME OVER! The Alien Intruder has caught you!")
        exit()
    print('-' * 20)

def check_win_condition(current_room, inventory, required_items):
    if current_room == 'Escape Pod Bay' and all(item in inventory for item in required_items):
        print("\n Congratulations! You have collected all necessary items and reached the Escape Pod! ")
        print("You successfully escape the space station. Mission accomplished!\n")
        return True  # Signal the game to end
    return False  # Game continues

def move_player(current_room, direction, rooms):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]  # Move to the new room
    else:
        print("You can't go that way!")
        return current_room  # Stay in the same room if movement is not possible

  # Create a main function to initialize game mechanics
def main():
    show_instructions()
    #Game setup
    current_room = 'Command Center' # Starting room
    inventory = [] # Empty inventory at the start
    required_items = ['Keycard', 'Oxygen tank', 'Power cell', 'Toolkit', 'Flashlight',
                      'Fuel can']  # Items needed to win
    rooms = {
        'Command Center': {'North': 'Greenhouse', 'West': 'Crew Quarters', 'East': 'Storage Bay', 'South': 'Labratory'},
        'Crew Quarters': {'East': 'Command Center', 'item': 'keycard'},
        'Labratory': {'North': 'Command Center', 'East': 'Engineering Deck', 'item': 'oxygen tank'},
        'Engineering Deck': {'West': 'Labratory', 'item': 'power cell'},
        'Storage Bay': {'West': 'Command Center', 'North': 'Medical Bay', 'item': 'toolkit'},
        'Medical Bay': {'South': 'Storage Bay', 'villain': 'Nova'},
        'Greenhouse': {'South': 'Command Center', 'East': 'Escape Pod Bay', 'item': 'flashlight'},
        'Escape Pod Bay': {'West': 'Greenhouse', 'item': 'fuel can'}



    }
    while True:  # Game loop
        show_status(current_room, inventory, rooms)
        move = input("Enter your move: ").strip().lower()

        if move == "exit":
            print("Thanks for playing! Goodbye.")
            break  # Exit the game

        elif move.startswith("go "):  # Handle movement
            direction = move[3:].capitalize()  # Extract direction (e.g., "go North" → "North")
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]  # Update current room
            if check_win_condition(current_room, inventory, required_items):
                break  # End the game loop when the player wins

            else:
                print("You can't go that way!")


        elif move.startswith("get "):  # Handle item pickup
            item = move[4:].capitalize()
            if "item" in rooms[current_room] and rooms[current_room]["item"].lower() == item.lower():
                inventory.append(item)  # Add item to inventory
                del rooms[current_room]["item"]  # Remove item from room
                print(f"You picked up {item}!")
            if check_win_condition(current_room, inventory, required_items):
                break
            else:
                print("There's no such item here!")


        else:
            print("Invalid command!")

# Run the game
if __name__ == "__main__":
    main()




