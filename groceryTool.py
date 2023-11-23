what_we_making = (input("What do you want to make? "))
grocery_list = []

def make_mashed_potatoes():
    grocery_list.append("potato")
    grocery_list.append("milk")
    grocery_list.append("butter")
    grocery_list.append("garlic powder")
    grocery_list.append("parmesan cheese")

def make_braised_oxtail():
    grocery_list.append("oxtail")
    grocery_list.append("carrots")
    grocery_list.append("onions")
    grocery_list.append("celery")
    grocery_list.append("red wine")
    grocery_list.append("demiglaze")
    grocery_list.append("salt")
    grocery_list.append("black pepper")

def make_prime_rib():
    grocery_list.append("prime ribeye roast")
    grocery_list.append("garlic")
    grocery_list.append("butter")
    grocery_list.append("butter")
    grocery_list.append("salt")
    grocery_list.append("black pepper")
    grocery_list.append("rosemary")

def load_unload_list():
    if "Y" in (input("Y/N Add item to list? ")):
        if "mashed potatoes" in what_we_making:
            make_mashed_potatoes()
        elif "braised oxtail" in what_we_making:
            make_braised_oxtail()
        elif "prime rib" in what_we_making:
            make_prime_rib()
        else:
            print("I don't have that recipe")
    else:
        print("Nothing added")