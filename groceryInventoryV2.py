#test data from other file
#will incorporate all features in to full app version

listA = []
listB = []
listC = []

def available_recipe():
    if "potato" and "butter" and "milk" and "parmesan" in listB:
        print("We have all ingredients for Mashed Potatoes")
    if "ribeye" and "butter" and "rosemary" and "salt" in listB:
        print("We have all ingredients for Ribeye Steak")
    else:
        print("Need ingredients")

def cook_recipe():
    if "mashed potatoes" in (input("What did you cook? ")):
        print("Use potato, butter, milk, and parmesan")
        listB.remove("potato")
        listB.remove("butter")
        listB.remove("milk")
        listB.remove("parmesan")
    elif "ribeye steak":
        print("Use ribeye, butter, rosemary, and salt")
        listB.remove("ribeye")
        listB.remove("butter")
        listB.remove("rosemary")
        listB.remove("salt")


def future_recipe():
    if "mashed potatoes" in (input("What do you plan on cooking? ")):
        listA.append("potato")
        listA.append("butter")
        listA.append("milk")
        listA.append("parmesan")
    elif "ribeye steak":
        listA.append("ribeye")
        listA.append("butter")
        listA.append("rosemary")
        listA.append("salt")

def receive_groceries():
    for item in listA:
        if "Y" in (input(item + " Did you receive? Y/N ")):
            listA.remove(item)
            listB.append(item)



