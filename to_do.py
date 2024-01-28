to_do = []

def save_to_file(to_do):
    with open("todo.txt", "w") as file:
        for item in to_do:
            file.write(item + "\n")

def load_from_file():
    try:
        with open("todo.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

print("Hello, Welcome to your To-Do List")

to_do = load_from_file()

def to_do_list():
    while True:
        choosing = input("Would you like to add, remove, or exit from the list? ")

        if choosing.lower() == "add":
            add_mode(to_do)

        elif choosing.lower() == "remove":
            remove_mode(to_do)

        elif choosing.lower() == 'exit':
            save_to_file(to_do)
            break
        else:
            print("\n\n\nInvalid input. Please enter 'add', 'remove', or 'exit'.\n\n\n")

def add_mode(to_do):
    while True:
        print("Your to-do list:", to_do)
        add = input("Enter to add to your to-do list (or enter 'no' to stop adding): ")
        
        if add.lower() == "no":
            print("Your to-do list:", to_do)
            break
        else:
            to_do.append(add)
            
def remove_mode(to_do):
    while True:
        print("Your to-do list:", to_do)
        where_to_remove = input("Enter the number of the item to remove (or enter 'no' to stop removing): ")

        if where_to_remove.lower() == "no":
            print("Your to-do list:", to_do)
            break
        elif where_to_remove.isdigit():
            where_to_remove = int(where_to_remove)
            if 1 <= where_to_remove <= len(to_do):
                removed_item = to_do.pop(where_to_remove - 1)
                print(f"Removed: {removed_item}")
            else:
                print("Not a spot on the list. Enter a new number")
        else:
            print("Invalid input. Please enter a valid number.")
            continue

to_do_list()
print("Your to-do list:", to_do)