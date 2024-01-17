to_do = []

def to_do_list():
    while True:
        choosing = input("Would you like to add, remove, or stop? ")

        if choosing.lower() == "add":
            add = input("Enter to add to your to-do list (Enter 'no' to end): ")
            if add.lower() == "no":
                break
            else:
                to_do.append(add)
        elif choosing.lower() == "remove":
            print("Your to-do list:")
            for i, item in enumerate(to_do):
                print(f"{i + 1}. {item}")

            if to_do:
                try:
                    where_to_remove = int(input("Enter the number of the item to remove: "))
                    if 1 <= where_to_remove <= len(to_do):
                        removed_item = to_do.pop(where_to_remove - 1)
                        print(f"Removed: {removed_item}")
                    else:
                        print("Invalid index. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("The to-do list is empty.")
        elif choosing.lower() == "stop":
            break
        else:
            print("Invalid choice. Please enter 'add', 'remove', or 'stop'.")

to_do_list()
print("Your final to-do list:", to_do)
