from groceryInventory import*

whatarewedoing = (input(" available recipes \n grocery List "
                        "\n future recipes \n receive groceries "
                        "\n see inventory \n cook \n "))

def what_do():
    if "available recipes" in whatarewedoing:
        available_recipe()
    elif "grocery list" in whatarewedoing:
        print(listA)
    elif "future recipe" in whatarewedoing:
        future_recipe()
    elif "receive groceries" in whatarewedoing:
        while listA != listC:
            receive_groceries()
    elif "see inventory" in whatarewedoing:
        print(listB)
    elif "cook" in whatarewedoing:
        cook_recipe()


while "N" not in whatarewedoing:
    what_do()
    whatarewedoing = (input(" available recipes \n grocery List "
                        "\n future recipes \n receive groceries "
                        "\n see inventory \n cook \n "))

#trying to rectify (listA!=listC) solution to receiving while loop
#needs to have a break command to go back to (whatarewedoing) loop
