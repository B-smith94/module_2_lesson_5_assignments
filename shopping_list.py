#1. Write a function that lets the user add items to the list.
#2. Include a function to remove items from the list.
#3. Add a function that prints out the entire list in a formatted way.

#NOTE: The goal of this is to be a program.  Reccomend using a while loop to allow user to continue to add,
#remove, and print off their shopping list until they decide to "quit" (break the loop).
shopping_list = []

def add_items(*items):
    items = input("What would you like to add?\t")
    shopping_list.append(items)

def remove_items(*items):
    items = input("What would you like to remove from the list?\t")
    shopping_list.remove(items)

def list_format():
    separator = input("How would you like to separate the items on your list?\t")
    new_list = separator.join(shopping_list)
    print(f"Great, here is your updated list:\n{new_list}")

def make_shopping_list(items):
    while True:
        changes = input("Would you like to make changes to your list? (yes/no)\t").lower()
        while changes == "yes":
            add_or_remove = input("Ok, would you like to add to the list or take items away? (type 'add' or 'remove')\n")
            if add_or_remove == "add":
                add_items()
                break
            elif add_or_remove == "remove":
                remove_items()
                break
            else:
                print("Invalid input, please try again.")
                continue
        else:
            list_format()
            break

make_shopping_list(shopping_list)