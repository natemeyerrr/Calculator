to_do = []

def to_do_list():
    choosing = input("Would you like to add or remove from the list? ")

    if choosing.lower() == "add":
        while True:
            add = input("Enter to add to your to-do list:\n(Enter 'no' to end) ")
            if add.lower() == "no":
                break
            else:
                to_do.append(add)
    elif choosing.lower() == "remove":
        print("Your to-do list:", to_do)
        where_to_remove = int(input("Enter the number of the item to remove: "))
        if 1 <= where_to_remove <= len(to_do):
            removed_item = to_do.pop(where_to_remove - 1)
            print(f"Removed: {removed_item}")
        else:
            print("Not a spot on the lsit. Enter a new number")
    else:
        print("Please enter 'add' or 'remove'.")

to_do_list()
print("Your to-do list:", to_do)
