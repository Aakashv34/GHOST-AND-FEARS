import random
import time

# Global Variables
inventory = []
game_over = False

# Function to start the game
def start_game():
    print("Welcome to 'Escape the Haunted Manor'!")
    user_name=input("Enter you name:")
    print(f"hi {user_name}, a brave adventurer trapped in a haunted house filled with traps and ghosts.")
    print("Your goal is to explore the rooms, collect items, and find a way to escape!")
    time.sleep(2)
    first_choice()

# Function for player's choices
def first_choice():
    while not game_over:
        print("\nYou are in the foyer of the manor. You can go:")
        print("1. Library")
        print("2. Kitchen")
        print("3. Workshop")
        print("4. Living Room")
        print("5. Secret Room")
        print("6. Check Inventory")
        print("7. Attempt to Escape")

        choice = input("Which way do you want to go? (1/2/3/4/5/6/7): ")

        if choice == '1':
            library()
        elif choice == '2':
            kitchen()
        elif choice == '3':
            workshop()
        elif choice == '4':
            living_room()
        elif choice == '5':
            secret_room()
        elif choice == '6':
            show_inventory()
        elif choice == '7':
            attempt_escape()
        else:
            print("Invalid choice, try again.")

# Room Functions
def library():
    print("\nYou enter the Library filled with dusty books.")
    print("You can:")
    print("1. Search for a hidden spell book.")
    print("2. Go back to the foyer.")

    choice = input("What do you want to do? (1/2): ")

    if choice == '1':
        found_item = random.choice(["a spell book", "nothing"])
        if found_item == "nothing":
            print("You searched but found nothing.")
        else:
            print("You found a spell book! It's magical and may help you.")
            inventory.append(found_item)
    elif choice == '2':
        return first_choice()
    else:
        print("Invalid choice, try again.")
        library()

def kitchen():
    print("\nYou enter the Kitchen. The smell of rotten food fills the air.")
    print("You can:")
    print("1. Look for food.")
    print("2. Go back to the foyer.")

    choice = input("What do you want to do? (1/2): ")

    if choice == '1':
        found_item = random.choice(["a knife", "a can of food", "nothing"])
        if found_item == "nothing":
            print("You searched but found nothing.")
        else:
            print(f"You found {found_item}!")
            inventory.append(found_item)
    elif choice == '2':
        return first_choice()
    else:
        print("Invalid choice, try again.")
        kitchen()

def workshop():
    print("\nYou enter the Workshop. Various tools and artifacts lie scattered around.")
    print("You can:")
    print("1. Search for useful tools.")
    print("2. Go back to the foyer.")

    choice = input("What do you want to do? (1/2): ")

    if choice == '1':
        found_item = random.choice(["a powerful tool", "a mystical relic", "nothing"])
        if found_item == "nothing":
            print("You searched but found nothing.")
        else:
            print(f"You found {found_item}! It may help you later.")
            inventory.append(found_item)
    elif choice == '2':
        return first_choice()
    else:
        print("Invalid choice, try again.")
        workshop()


def living_room():
    print("\nYou enter the Living Room. A ghost appears!")
    if "a spell book" in inventory:
        print("You use the spell book to scare the ghost away!")
        print("Congratulations! You've successfully scared away the ghost!")
        inventory.remove("a spell book")
    else:
        print("You can either:")
        print("1. Fight the ghost.")
        print("2. Run back to the foyer.")

        choice = input("What do you want to do? (1/2): ")

        if choice == '1':
            print("The ghost is too powerful! You were defeated.")
            end_game()
        elif choice == '2':
            return first_choice()
        else:
            print("Invalid choice, try again.")
            living_room()

def secret_room():
    print("\nYou discover a hidden door leading to a Secret Room!")
    print("You can:")
    print("1. Search for a way out.")
    print("2. Go back to the foyer.")

    choice = input("What do you want to do? (1/2): ")

    if choice == '1':
        if "a mystical relic" in inventory:
            print("You use the mystical relic to unlock the secret escape route!")
            print("Congratulations! You've escaped the haunted manor!")
            global game_over
            game_over = True
        else:
            print("You can't find a way out without the mystical relic.")
            print("You must return to explore other rooms.")
            return first_choice()
    elif choice == '2':
        return first_choice()
    else:
        print("Invalid choice, try again.")
        secret_room()

def attempt_escape():
    if "a mystical relic" in inventory:
        print("You use the mystical relic to try to escape.")
        print("Congratulations! You've escaped the haunted manor!")
        global game_over
        game_over = True
    else:
        print("You can't escape without the mystical relic.")
        print("You need to explore the manor more.")
        return first_choice()

def show_inventory():
    if inventory:
        print("Your inventory:", inventory)
    else:
        print("Your inventory is empty.")

def end_game():
    print("Game Over! You couldn't escape the haunted manor.")
    print("Your inventory contained:", set(inventory))
    global game_over
    game_over = True

# Start the game
start_game()
