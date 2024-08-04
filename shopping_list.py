#1. Write a function that lets the user add items to the list.
#2. Include a function to remove items from the list.
#3. Add a function that prints out the entire list in a formatted way.
#NOTE: The goal of this is to be a program.  Reccomend using a while loop to allow user to continue to add, remove,
# and print off their shopping list until they decide to "quit" (break the loop).

def shopping_list(items=[]):
    while True:
        changes = input("Would you like to make changes to your list? (yes/no)\t").lower()
        while changes == "yes":
            add_or_remove = input("Ok, would you like to add to the list or take items away? (type 'add' or 'remove')\n")
            if add_or_remove == "add":
                add_items = items.append(input("what would you like to add?\t"))
                break
            elif add_or_remove == "remove":
                remove_items = items.remove(input("ok, what would you like to remove?\t"))
                break
            else:
                print("Invalid input, please try again.")
                continue
        else:
            separator = input("How would you like your list formatted? Please type '-', '--', or ', '.\t")
            new_list = separator.join(items)
            break
    print(new_list)

shopping_list(['tomatoes', 'peppers', 'cereal'])