#test data from other file
#will incorporate all features in to full app version

listA = []
listB = []

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

#having trouble getting this one to call
#will attempt to debug
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
    receiving = (input("What did you receive? "))
    while "nothing" not in receiving:
        if "potato" in receiving:
            listA.remove("potato")
            listB.append("potato")
        if "butter" in receiving:
            listA.remove("butter")
            listB.append("butter")
        if "milk" in receiving:
            listA.remove("milk")
            listB.append("milk")
        if "parmesan" in receiving:
            listA.remove("parmesan")
            listB.append("parmesan")
        if "ribeye" in receiving:
            listA.remove("ribeye")
            listB.append("ribeye")
        if "butter" in receiving:
            listA.remove("butter")
            listB.append("butter")
        if "rosemary" in receiving:
            listA.remove("rosemary")
            listB.append("rosemary")
        if "salt" in receiving:
            listA.remove("salt")
            listB.append("salt")


#This is the second file to use modules for grocery list and inventory lists
#Calling all functions to test code worked with exception noted above

future_recipe()
print("Grocery List: ")
print(listA)
print("Inventory: ")
print(listB)

print("## Action Break ##")

for item in listA:
    listB.append(item)
for item in listB:
    listA.remove(item)

print("Grocery List:")
print(listA)
print("Inventory")
print(listB)
available_recipe()
cook_recipe()
print(listB)
print(listA)
